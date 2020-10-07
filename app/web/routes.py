from flask import Blueprint, render_template

site = Blueprint(
    "site", __name__,
    url_prefix="/",
    static_folder="web_static",
    template_folder="web_templates")
