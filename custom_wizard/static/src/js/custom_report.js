/** @odoo-module */
import { registry } from "@web/core/registry";
//import { getReportUrl, getWKHTMLTOPDF_MESSAGES } from "@web/webclient/actions/reports/utils";
import { _t } from "@web/core/l10n/translation";
import { jsonrpc } from "@web/core/network/rpc_service"; // Import jsonrpc function from rpc_service.js

export function getReportUrl(action, type, userContext) {
    let url = `/report/${type}/${action.report_name}`;
    const actionContext = action.context || {};
    if (action.data && JSON.stringify(action.data) !== "{}") {
        // build a query string with `action.data` (it's the place where reports
        // using a wizard to customize the output traditionally put their options)
        const options = encodeURIComponent(JSON.stringify(action.data));
        const context = encodeURIComponent(JSON.stringify(actionContext));
        url += `?options=${options}&context=${context}`;
    } else {
        if (actionContext.active_ids) {
            url += `/${actionContext.active_ids.join(",")}`;
        }
        if (type === "html") {
            const context = encodeURIComponent(JSON.stringify(userContext));
            url += `?context=${context}`;
        }
    }
    return url;
}

// messages that might be shown to the user dependening on the state of wkhtmltopdf
function getWKHTMLTOPDF_MESSAGES(status) {
    const link = '<br><br><a href="http://wkhtmltopdf.org/" target="_blank">wkhtmltopdf.org</a>'; // FIXME missing markup
    const _status = {
        broken:
            _t(
                "Your installation of Wkhtmltopdf seems to be broken. The report will be shown in html."
            ) + link,
        install:
            _t("Unable to find Wkhtmltopdf on this system. The report will be shown in html.") +
            link,
        upgrade:
            _t(
                "You should upgrade your version of Wkhtmltopdf to at least 0.12.0 in order to get a correct display of headers and footers as well as support for table-breaking between pages."
            ) + link,
        workers: _t(
            "You need to start Odoo with at least two workers to print a pdf version of the reports."
        ),
    };
    return _status[status];
}

// Utility function to clean the context
function cleanContext(context) {
    const cleanContext = {};
    for (const key in context) {
        if (context.hasOwnProperty(key) && typeof context[key] !== 'object') {
            cleanContext[key] = context[key];
        }
    }
    return cleanContext;
}

async function openReportWizard(action, type, userContext) {
    console.log("Custom report wizard function called with action:", action);
    console.log("action report_type: ", action.report_type);

    if (action.report_type === 'qweb-pdf') {
        type = 'pdf';
    } else if (action.report_type === 'qweb-text') {
        type = 'text';
    } else {
        throw new ValueError("Unsupported type: " + type);
    }

    let message;

    if (type === "pdf") {
        console.log("is PDF");
        // Cache the wkhtml status on the function. In prod this means it is only
        // checked once, but we can reset it between tests to test multiple statuses.
        openReportWizard.wkhtmltopdfStatusProm ||= jsonrpc("/report/check_wkhtmltopdf");
        const status = await openReportWizard.wkhtmltopdfStatusProm;
        message = getWKHTMLTOPDF_MESSAGES(status);
        if (!["upgrade", "ok"].includes(status)) {
            return { success: false, message };
        }
    }

    console.log("Type: ", type);
    // Ensure URL is correctly formatted
    const url = getReportUrl(action, type, userContext);
    console.log("Generated Report URL:", url);

    const cleanUserContext = cleanContext(userContext);

    const response = await jsonrpc('/report/open_wizard', {
        data: JSON.stringify([url, action.report_type]),
        context: JSON.stringify(cleanUserContext),
    });

    if (response.error) {
        return { success: false, message: response.error };
    } else {
        return { success: true, message: response.message };
    }
}

// Register the custom report action handler in the correct registry category
registry.category("ir.actions.report handlers").add("Open Report Wizard", openReportWizard);
console.log("Custom report wizard function registered");
