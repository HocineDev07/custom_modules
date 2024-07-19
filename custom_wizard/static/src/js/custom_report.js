/** @odoo-module */
import { registry } from "@web/core/registry";
//import { rpcService } from "@web/core/network/rpc_service";
//import { download } from "@web/core/network/download";
import { useService } from "@web/core/utils/hooks";
import { getReportUrl } from "@web/webclient/actions/reports/utils";
import { _t } from "@web/core/l10n/translation";

// messages that might be shown to the user depending on the state of wkhtmltopdf
function getWKHTMLTOPDF_MESSAGES(status) {
    const link = '<br><br><a href="http://wkhtmltopdf.org/" target="_blank">wkhtmltopdf.org</a>';
    const _status = {
        broken: _t("Your installation of Wkhtmltopdf seems to be broken. The report will be shown in html.") + link,
        install: _t("Unable to find Wkhtmltopdf on this system. The report will be shown in html.") + link,
        upgrade: _t("You should upgrade your version of Wkhtmltopdf to at least 0.12.0 in order to get a correct display of headers and footers as well as support for table-breaking between pages.") + link,
        workers: _t("You need to start Odoo with at least two workers to print a pdf version of the reports."),
    };
    return _status[status];
}

function cleanContext(context) {
    // Create a shallow copy of the context object with only non-circular properties
    return {
        lang: context.lang,
        tz: context.tz,
        uid: context.uid,
        user_context: context.user_context,
        allowed_company_ids: context.allowed_company_ids,
    };
}

async function openReportWizard(action, type, userContext) {
    console.log("Custom report wizard function called with action:", action);
    let message;

    const rpc = useService('rpc');

    if (type === "pdf") {
        console.log("is PDF")
        // Cache the wkhtml status on the function. In prod this means is only
        // checked once, but we can reset it between tests to test multiple statuses.
        openReportWizard.wkhtmltopdfStatusProm ||= rpc("/report/check_wkhtmltopdf");
        const status = await openReportWizard.wkhtmltopdfStatusProm;
        message = getWKHTMLTOPDF_MESSAGES(status);
        if (!["upgrade", "ok"].includes(status)) {
            return { success: false, message };
        }
    }
    const url = getReportUrl(action, type);
    // Clean the context to avoid circular references
    const cleanUserContext = cleanContext(userContext);

    try {
        const result = await rpc('/report/open_wizard', {
            data: JSON.stringify([url, action.report_type]),
            context: JSON.stringify(cleanUserContext),
        });
        console.log("Custom report wizard action result:", result);
        return result;
    } catch (error) {
        console.error("Error in openReportWizard:", error);
        return { success: false, message: _t("Failed to open report wizard") };
    }
}

registry.category("ir.actions.report handlers").add("Open Report Wizard", openReportWizard);
console.log("Custom report wizard function registered");
