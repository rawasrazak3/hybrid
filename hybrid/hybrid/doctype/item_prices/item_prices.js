// Copyright (c) 2024, rawasrazak and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Prices', {
	refresh(frm) {
		//
	}
});

frappe.ui.form.on('Item Prices', {
    refresh(frm) {
        frm.fields_dict['purchase_invoice'].get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    docstatus: 1,  // Filter for submitted Purchase Invoices
                    // Add any other filters as needed
                }
            };
        };
    },
    purchase_invoice(frm, cdt, cdn) {
        const child = locals[cdt][cdn];
        if (child.purchase_invoice) {
            fetchItemCodes(child.purchase_invoice, frm, cdt, cdn);
        }
    },
    item_prices_table_add(frm, cdt, cdn) {
        const child = locals[cdt][cdn];
        if (child.item_code) {
            fetchItemPrices(child.item_code, frm, cdt, cdn);
        }
        frm.refresh_field('item_prices_table');
    },
});

frappe.ui.form.on('Item Prices Table', {
    refresh(frm, cdt, cdn) {
        frm.trigger('item_code');
    },
    item_code(frm, cdt, cdn) {
        const child = locals[cdt][cdn];
        if (frm.doc.item_prices_table) {
            const fetchPrice = (field, method) => {
                frappe.call({
                    method: `hybrid.hybrid.doctype.item_prices.item_prices.${method}`,
                    args: { item_code: child.item_code },
                    callback: function (r) {
                        const price = r.message;
                        if (price) {
                            child[field] = price;
                            frm.refresh_field('item_prices_table');
                        }
                    }
                });
            };

            fetchPrice('valuation_rate', 'valuation_rate');
            fetchPrice('cost_price', 'incoming_rate');
            fetchPrice('selling_price_1', 'selling_price_1');
            fetchPrice('selling_price_2', 'selling_price_2');
            fetchPrice('selling_price_3', 'selling_price_3');
            fetchPrice('selling_price_4', 'selling_price_4');
            fetchPrice('selling_price_5', 'selling_price_5');
            fetchPrice('selling_price_6', 'selling_price_6');
        }
    }
});

function fetchItemCodes(purchase_invoice, frm, cdt, cdn) {
    frappe.call({
        method: 'hybrid.hybrid.doctype.item_prices.item_prices.fetch_item_codes',
        args: {
            purchase_invoice: purchase_invoice
        },
        callback: function(r) {
            if (r.message) {
                console.log('Fetched Item Codes:', r.message);  // Log fetched data to the console

                frm.fields_dict['item_prices_table'].grid.remove_all();
                $.each(r.message, function(i, item) {
                    const row = frappe.model.add_child(frm.doc, 'Item Prices Table', 'item_prices_table');
                    row.item_code = item.item_code;
                    fetchItemName(item.item_code, row); // Fetch and set item_name
                    fetchItemPrices(item.item_code, frm, 'Item Prices Table', row.name);
                });
                frm.refresh_field('item_prices_table');
            }
        }
    });
}

function fetchItemName(item_code, row) {
    frappe.call({
        method: 'hybrid.hybrid.doctype.item_prices.item_prices.item_name',
        args: {
            item_code: item_code
        },
        callback: function(r) {
            if (r.message) { 
                row.item_name = r.message;
                frm.refresh_field('item_prices_table');
            }
        }
    });
}

function fetchItemPrices(item_code, frm, cdt, cdn) {
    const child = locals[cdt][cdn];
    const fetchPrice = (field, method) => {
        frappe.call({
            method: `hybrid.hybrid.doctype.item_prices.item_prices.${method}`,
            args: { item_code: item_code },
            callback: function (r) {
                const price = r.message;
                if (price) {
                    child[field] = price;
                    frm.refresh_field('item_prices_table');
                }
            }
        });
    };

    fetchPrice('valuation_rate', 'valuation_rate');
    fetchPrice('cost_price', 'incoming_rate');
    fetchPrice('selling_price_1', 'selling_price_1');
    fetchPrice('selling_price_2', 'selling_price_2');
    fetchPrice('selling_price_3', 'selling_price_3');
    fetchPrice('selling_price_4', 'selling_price_4');
    fetchPrice('selling_price_5', 'selling_price_5');
    fetchPrice('selling_price_6', 'selling_price_6');
}