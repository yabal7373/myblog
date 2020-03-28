from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskapp import db



admin = Blueprint('admin', __name__)


# @admin.route("/admin")
# def admin():
#     return render_template('admin.html', form=form)