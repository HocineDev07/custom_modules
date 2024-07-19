/** @odoo-module */
import { registry } from "@web/core/registry";
import { getReportUrl, getWKHTMLTOPDF_MESSAGES } from "@web/webclient/actions/reports/utils";
import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

class CustomReportComponent extends Component {
    setup() {
        this.rpc = useService("rpc");
    }

    cleanContext(context) {
        const cleanContext = {};
        for (const key in context) {
            if (context.hasOwnProperty(key) && typeof context[key] !== 'object') {
                cleanContext[key] = context[key];
            }
        }
        return cleanContext;
    }

    async openReportWizard(action, type, userContext) {
        console.log("Custom report wizard function called with action:", action);
        let message;

        if (type === "pdf") {
            console.log("is PDF");
            // Cache the wkhtml status on the function. In prod this means it is only
            // checked once, but we can reset it between tests to test multiple statuses.
            CustomReportComponent.wkhtmltopdfStatusProm ||= rpc("/report/check_wkhtmltopdf");
            const status = await CustomReportComponent.wkhtmltopdfStatusProm;
            message = getWKHTMLTOPDF_MESSAGES(status);
            if (!["upgrade", "ok"].includes(status)) {
                return { success: false, message };
            }
        }

        const url = getReportUrl(action, type);
        const cleanUserContext = this.cleanContext(userContext);

        try {
            const result = await rpc("/report/open_wizard", {
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
}

// Register the custom report action handler in the correct registry category
registry.category("ir.actions.report handlers").add("Open Report Wizard", async (action, type, userContext) => {
    const component = new CustomReportComponent();
    return component.openReportWizard(action, type, userContext);
});
console.log("Custom report wizard function registered");
