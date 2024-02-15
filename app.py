from flask import Flask, request, redirect, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Department, Employee, get_directory, get_directory_join, get_directory_join_class, Project, EmployeeProject
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///employees_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to tußrn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()
app.app_context().push()


@app.route("/phones")
def phone_list():
    """Get list of users & dept phones.

    This version will be a 'n+1 query' --- it will query once for all
    users, and then for each department.

    There's a way to tell SQLAlchemy to load all the data in a single query,
    but don't worry about this for now.
    """

    emps = Employee.query.all()
    return render_template("phones.html", emps=emps)
