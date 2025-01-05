import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
    make_custom_fields()

def make_custom_fields():
    custom_fields = {
        "User": [
            {
                "fieldname": "cost_center",
                "label": "Cost Center",
                "fieldtype": "Link",
                "options": "Cost Center",
                "insert_after": "send_welcome_email",
                "reqd": 0,
            },
            {
                "fieldname": "warehouse",
                "label": "Warehouse",
                "fieldtype": "Link",
                "options": "Warehouse",
                "insert_after": "cost_center",
                "reqd": 0,
            },
        ]
    }

    create_custom_fields(custom_fields)