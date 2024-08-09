frappe.ui.form.on('Sales Invoice', {
	refresh(frm) {
        //
	}
});



frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    
                }
            };
        };
    }
});


frappe.ui.form.on('Sales Invoice Item', {
    item_code: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var item_code = child.item_code;
        var uom = child.uom;
        var customer = frm.doc.customer;

        console.log("Customer:", customer);

        frappe.call({
            method: 'hybrid.hybrid.custom_script.sales_invoice.price_list_item',
            args: {
                item_code: item_code,
                uom: uom,
                customer : customer,
                
            },
            callback: function(r) {
                if (r.message) {
                    if (!frm.doc.custom_price_list) {
                        frm.add_child('custom_price_list', {});
                    }

                    var last_row = frm.doc.custom_price_list[frm.doc.custom_price_list.length - 1];

                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_1', r.message.selling_price_1);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_2', r.message.selling_price_2);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_3', r.message.selling_price_3);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_4', r.message.selling_price_4);

                    frm.refresh_field('custom_price_list');
                }
            }
        });
    },
    uom: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var item_code = child.item_code;
        var uom = child.uom;
        var customer = frm.doc.customer;

        console.log("Customer:", customer);

        frappe.call({
            method: 'hybrid.hybrid.custom_script.sales_invoice.price_list_uom',
            args: {
                item_code: item_code,
                uom: uom,
                customer : customer,
                
            },
            callback: function(r) {
                if (r.message) {
                    if (!frm.doc.custom_price_list) {
                        frm.add_child('custom_price_list', {});
                    }

                    var last_row = frm.doc.custom_price_list[frm.doc.custom_price_list.length - 1];

                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_1', r.message.selling_price_1);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_2', r.message.selling_price_2);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_3', r.message.selling_price_3);
                    frappe.model.set_value(last_row.doctype, last_row.name, 'price_4', r.message.selling_price_4);

                    frm.refresh_field('custom_price_list');
                }
            }
        });
    }
});


/////////////////////////////////WHAREHOUSE TABLE QTY IN SALES INVOICE////////////////////////////////////

// frappe.ui.form.on('Sales Invoice Item', {
//     item_code: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];
//         var item_code = child.item_code;

//         frappe.call({
//             method: 'sas_new.sas_erp.custom_script.sales_invoice.avail_qty',
//             args: {
//                 item_code: item_code
//             },
//             callback: function(r) {
//                 if (r.message) {
//                     if (!frm.doc.custom_warehouse_qty) {
//                         frm.add_child('custom_warehouse_qty', {});
//                     }

//                     var last_row = frm.doc.custom_warehouse_qty[frm.doc.custom_warehouse_qty.length - 1];

//                     frappe.model.set_value(last_row.doctype, last_row.name, 'warehouse1', r.message.warehouse_1);
//                     frappe.model.set_value(last_row.doctype, last_row.name, 'warehouse2', r.message.warehouse_2);
//                     frappe.model.set_value(last_row.doctype, last_row.name, 'custom_warehouse3', r.message.warehouse_3);

//                     frm.refresh_field('custom_warehouse_qty');
//                 }
//             }
//         });
//     }
// });

/////////////////////////////////WHAREHOUSE TABLE QTY IN SALES INVOICE////////////////////////////////////


frappe.ui.form.on('Sales Invoice', {
    setup: function(frm) {
        var isPromptOpen = false;
        var allowedUsers = ['huzaifa@thekidsmania.com', 'kidsmaniakwt1@gmail.com', 'Administrator']

        frm.fields_dict['custom_profit_rate'].$wrapper.on('click', function() {
            if (!allowedUsers.includes(frappe.session.user)) {
                frappe.msgprint(__('You do not have permission to perform this action.'));
                return;
            }
            if (!isPromptOpen) {
                isPromptOpen = true; 

                var valuationData = [];
                var totalRate = 0;
                var totalValuationRate = 0;
                var totalMargin = 0;
                frm.doc.items.forEach(function(item) {
                    var margin = item.amount - (item.custom_valuation_rate * item.stock_qty);
                    var margin_percentage = ((margin / (item.custom_valuation_rate * item.stock_qty)) * 100).toFixed(3);

                    totalRate += item.amount;
                    totalValuationRate += item.custom_valuation_rate * item.stock_qty;
                    totalMargin += margin;

                    valuationData.push({
                        item_code: item.item_code,
                        rate: item.amount,
                        valuation_rate: item.custom_valuation_rate * item.stock_qty,
                        margin: margin,
                        margin_percentage: margin_percentage
                    });
                });

                var totalRow = {
                    item_code: '<b>Total</b>',
                    rate: totalRate.toFixed(3),
                    valuation_rate: totalValuationRate.toFixed(3),
                    margin: totalMargin.toFixed(3),
                    margin_percentage: ((totalMargin / totalValuationRate) * 100).toFixed(3)
                };
                valuationData.push(totalRow);

                var promptDialog = frappe.prompt([
                    {
                        label: __('Margin Table'),
                        fieldname: 'custom_valuation_table',
                        fieldtype: 'Table',
                        read_only: 1,
                        fields: [
                            {
                                label: __('CODE'),
                                fieldname: 'item_code',
                                fieldtype: 'Data',
                                in_list_view: 1,
                                read_only: 1
                            },
                            {
                                label: __('TOTAL PRICE'),
                                fieldname: 'rate',
                                fieldtype: 'Float',
                                in_list_view: 1,
                                read_only: 1
                            },
                            {
                                label: __('VALUATION RATE'),
                                fieldname: 'valuation_rate',
                                fieldtype: 'Float',
                                in_list_view: 1,
                                read_only: 1
                            },
                            {
                                label: __('MARGIN'),
                                fieldname: 'margin',
                                fieldtype: 'Float',
                                in_list_view: 1,
                                read_only: 1
                            },
                            {
                                label: __('MARGIN %'),
                                fieldname: 'margin_percentage',
                                fieldtype: 'Percent',
                                in_list_view: 1,
                                read_only: 1
                            },
                        ],
                        data: valuationData
                    }
                ], function(values) {
                    isPromptOpen = false;
                }, __('Margin'));

                promptDialog.onhide = function() {
                    isPromptOpen = false;
                };
            }

            frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            };

            frm.trigger('items_refresh');
        });
    }
});

frappe.ui.form.on('Sales Invoice Item', {
    item_code: function (frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        var item_code = child.item_code;

        frappe.call({
            method: 'hybrid.hybrid.doctype.item_prices.item_prices.valuation_rate', 
            args: {
                item_code: item_code
            },
            callback: function (r) {
                if (r.message) {
                    frappe.model.set_value(cdt, cdn, 'custom_valuation_rate', r.message);
                    frm.refresh_field('items');
                }
            }
        });
    }
});
