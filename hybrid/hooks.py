app_name = "hybrid"
app_title = "Hybrid"
app_publisher = "rawasrazak"
app_description = "Hybrid Customizations"
app_email = "rawas@sastechnologie.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hybrid/css/hybrid.css"
# app_include_js = "/assets/hybrid/js/hybrid.js"

# include js, css files in header of web template
# web_include_css = "/assets/hybrid/css/hybrid.css"
# web_include_js = "/assets/hybrid/js/hybrid.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hybrid/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    "Sales Invoice": "public/js/sales_vo.js"
    }

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hybrid.utils.jinja_methods",
# 	"filters": "hybrid.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hybrid.install.before_install"
# after_install = "hybrid.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hybrid.uninstall.before_uninstall"
# after_uninstall = "hybrid.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hybrid.utils.before_app_install"
# after_app_install = "hybrid.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hybrid.utils.before_app_uninstall"
# after_app_uninstall = "hybrid.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hybrid.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hybrid.tasks.all"
# 	],
# 	"daily": [
# 		"hybrid.tasks.daily"
# 	],
# 	"hourly": [
# 		"hybrid.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hybrid.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hybrid.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hybrid.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hybrid.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hybrid.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hybrid.utils.before_request"]
# after_request = ["hybrid.utils.after_request"]

# Job Events
# ----------
# before_job = ["hybrid.utils.before_job"]
# after_job = ["hybrid.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hybrid.auth.validate"
# ]

fixtures=[
    {
    	"doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [ 
                    "Sales Invoice-custom_profit_rate",
                    "Sales Invoice Item-custom_valuation_rate",
                    "Sales Invoice-custom_price_list",
                 ]
            ]
        ]
    }
]