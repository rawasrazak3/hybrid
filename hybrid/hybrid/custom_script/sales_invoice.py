import frappe

@frappe.whitelist()
def valuation_rate(item_code):
    results = None
    entries = frappe.get_all(
        'Stock Ledger Entry',
        filters={'item_code': item_code, 'is_cancelled': 0},
        fields=['valuation_rate'],
        order_by='posting_date DESC, posting_time DESC, creation DESC',
        limit=1
    )

    if entries:
        results = entries[0].get('valuation_rate')

    return results
    
# @frappe.whitelist()
# def price_list(item_code,customer, uom=None):
#     print("customer from py3: ",customer)
#     results = {'selling_price_1': False, 'selling_price_2': False, 'selling_price_3': False, 'selling_price_4': False,}

#     exst_1 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Retail Price'})
#     if exst_1:
#         item_price_1 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Retail Price'})
#         results['selling_price_1'] = item_price_1.price_list_rate

#         exst_2 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Special Price'})
#         if exst_2:
#             item_price_2 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Special Price'})
#             results['selling_price_2'] = item_price_2.price_list_rate

#         exst_3 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price'})
#         if exst_3:
#             item_price_3 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price'})
#             results['selling_price_3'] = item_price_3.price_list_rate

    
#         exst_4 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Customer Price','selling':1 ,'customer': customer})
#         if exst_4:
#             item_price_4 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer})
#             results['selling_price_4'] = item_price_4.price_list_rate

#     return results

@frappe.whitelist()
def price_list(item_code, customer, uom=None):
    print("customer from py3: ",customer)
    print("uom is :", uom)
    results = {'selling_price_1': False, 'selling_price_2': False, 'selling_price_3': False, 'selling_price_4': False,}

    exst_1 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Retail Price'})
    ext_12 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': uom})
    if ext_12:
        item_price_1 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': uom})
        results['selling_price_1'] = item_price_1.price_list_rate

    elif exst_1:
        item_price_1 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Retail Price'})
        results['selling_price_1'] = item_price_1.price_list_rate
    else:
        item_price_1 = 0

    exst_2 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Special Price'})
    ext_22 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': uom})
    if ext_22:
        item_price_2 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': uom})
        results['selling_price_2'] = item_price_2.price_list_rate
    elif exst_2:
        item_price_2 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Special Price'})
        results['selling_price_2'] = item_price_2.price_list_rate
    else:
        item_price_2 = 0

    exst_3 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price'})
    ext_32 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': uom})
    if ext_32:
        item_price_3 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': uom})
        results['selling_price_3'] = item_price_3.price_list_rate
        
    elif exst_3:
        item_price_3 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price'})
        results['selling_price_3'] = item_price_3.price_list_rate
    else:
        item_price_3 = 0

    exst_4 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Customer Price','selling':1 ,'customer': customer})
    ext_42 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'uom': uom})
    if ext_42:
        item_price_4 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer, 'uom': uom})
        results['selling_price_4'] = item_price_4.price_list_rate
        
    elif exst_4:
        item_price_4 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer})
        results['selling_price_4'] = item_price_4.price_list_rate
    else:
        item_price_4 = 0

    return results

@frappe.whitelist()
def price_list_item(item_code, customer):
    results = {'selling_price_1': False, 'selling_price_2': False, 'selling_price_3': False, 'selling_price_4': False, 'selling_price_5': False}

    exst_1 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': 'PCS'})
    if exst_1:
        item_price_1 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': 'PCS'})
        results['selling_price_1'] = item_price_1.price_list_rate

    exst_2 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': 'PCS'})
    if exst_2:
        item_price_2 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': 'PCS'})
        results['selling_price_2'] = item_price_2.price_list_rate

    exst_3 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': 'PCS'})
    if exst_3:
        item_price_3 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': 'PCS'})
        results['selling_price_3'] = item_price_3.price_list_rate

    exst_4 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer, 'uom': 'PCS'})
    if exst_4:
        item_price_4 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer, 'uom': 'PCS'})
        results['selling_price_4'] = item_price_4.price_list_rate

    return results

@frappe.whitelist()
def price_list_uom(item_code, customer, uom=None):
    results = {'selling_price_1': False, 'selling_price_2': False, 'selling_price_3': False, 'selling_price_4': False, 'selling_price_5': False}

    exst_1 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': uom})
    if exst_1:
        item_price_1 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Retail Price', 'uom': uom})
        results['selling_price_1'] = item_price_1.price_list_rate

    exst_2 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': uom})
    if exst_2:
        item_price_2 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Special Price', 'uom': uom})
        results['selling_price_2'] = item_price_2.price_list_rate

    exst_3 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': uom})
    if exst_3:
        item_price_3 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Wholesale Price', 'uom': uom})
        results['selling_price_3'] = item_price_3.price_list_rate

    exst_4 = frappe.db.exists('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer, 'uom': uom})
    if exst_4:
        item_price_4 = frappe.get_last_doc('Item Price', {'item_code': item_code, 'price_list': 'Customer Price', 'customer': customer, 'uom': uom})
        results['selling_price_4'] = item_price_4.price_list_rate

    return results

# ///////////////////////////////////////WHAREHOUSE TABLE QTY IN SALES INVOICE///////////////////////////////////////
# @frappe.whitelist()
# def avail_qty(item_code):
#     results = {'warehouse_1': False, 'warehouse_2': False, 'warehouse_3': False}

#     exst_1 = frappe.db.exists('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'KIDSMANIA WAREHOUSE SALMIYAH  - KM', 'is_cancelled': 0})
#     if exst_1:
#         warehouse__1 = frappe.get_last_doc('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'KIDSMANIA WAREHOUSE SALMIYAH  - KM', 'is_cancelled': 0})
#         results['warehouse_1'] = warehouse__1.qty_after_transaction

#     exst_2 = frappe.db.exists('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'OUTLET MUBRAKIYA - KM', 'is_cancelled': 0})
#     if exst_2:
#         warehouse__2 = frappe.get_last_doc('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'OUTLET MUBRAKIYA - KM', 'is_cancelled': 0})
#         results['warehouse_2'] = warehouse__2.qty_after_transaction

#     exst_3 = frappe.db.exists('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'WAREHOUSE 1 MUBARAKIYA - KM', 'is_cancelled': 0})
#     if exst_3:
#         warehouse__3 = frappe.get_last_doc('Stock Ledger Entry', {'item_code': item_code, 'warehouse': 'WAREHOUSE 1 MUBARAKIYA - KM', 'is_cancelled': 0})
#         results['warehouse_3'] = warehouse__3.qty_after_transaction

#     return results
# /////////////////////////////////////WHAREHOUSE TABLE QTY IN SALES INVOICE/////////////////////////////////////////


@frappe.whitelist()
def fetch_item_codes(purchase_invoice):
    items_data = []
    pi_doc = frappe.get_doc('Purchase Invoice', purchase_invoice)
    
    for item in pi_doc.items:
        items_data.append({
            'item_code': item.item_code,
            'item_name': item.item_name 
        })
        
    return items_data

@frappe.whitelist()
def avl_qty(item_code):
    results = None 
    entries = frappe.get_all(
        'Stock Ledger Entry',
        filters={'item_code': item_code, 'is_cancelled': 0},
        fields=['qty_after_transaction'],
        order_by='posting_date DESC, posting_time DESC, creation DESC',
        limit=1 
    )

    if entries:
        results = entries[0].get('qty_after_transaction')

    return results