import frappe

def set_session_defaults(login_manager):
    user = frappe.session.user
    user_doc = frappe.get_doc("User", user)

    cost_center = user_doc.get("cost_center")
    warehouse = user_doc.get("warehouse")

    frappe.defaults.set_user_default("cost_center", cost_center)
    frappe.defaults.set_user_default("warehouse", warehouse)
