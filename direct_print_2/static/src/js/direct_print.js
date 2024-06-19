odoo.define('direct_print_2.DirectPrint', function (require) {
    "use strict";

    var ActionManager = require('web.ActionManager');
    var core = require('web.core');

    var _t = core._t;

    ActionManager.include({
        _executeReportAction: function (action, options) {
            var self = this;
            if (action.report_type === 'qweb-pdf') {
                return this._downloadReport(action).then(function () {
                    // Download complete, open the report in a wizard
                    return self.do_action({
                        type: 'ir.actions.act_window',
                        res_model: 'direct.print.wizard',  // Replace with your wizard model
                        target: 'new',
                        context: {
                            'report_name': action.report_name,
                            'active_id': action.context.active_ids[0],
                        },
                    });
                });
            }
            // For other report types, fall back to default behavior
            return this._super(action, options);
        },
    });

    return {
        DirectPrint: true
    };
});
