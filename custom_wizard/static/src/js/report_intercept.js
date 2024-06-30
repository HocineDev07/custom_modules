odoo.define('custom_wizard.report_intercept', [], function (require) {
    'use strict';

    const ajax = require('web.ajax');
    const core = require('web.core');
    const ActionManager = require('web.ActionManager');
    // const _t = core._t;

    $(document).on('click', '.o_report_action', function (e) {
        e.preventDefault();
        const $el = $(this);
        ajax.jsonRpc('/custom_wizard/trigger_wizard', 'call', {})
            .then(function (action) {
                // Get the ActionManager instance
                const action_manager = new ActionManager(core.bus);
                action_manager.do_action(action).then(function () {
                    // Rebind the click event after the wizard is closed
                    $el.off('click').click();
                });
            });
    });
});
