from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Department(db.Model):
    """Department Model"""

    __tablename__ = "departments"

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)


class Employee(db.Model):
    """Employee Model"""

    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=False, default='TX')
    dept_code = db.Column

    # This is the magic Line!
    # Sets up a dept attribute on each instance of Employee
    # SQLA will populate it with data from the departments table automatically!

    dept = db.relationship('Department', backref='employee')

    def __repr__(self):
        return f"<Employee {self.name} {self.state} {self.dept_code}>"

    def get_directory(self):
        all_emps = Employee.query.all()
        for emp in all_emps:
            if emp.dept is not None:
                print(emp.name, emp.dept.dept_name, emp.dept.phone)
                print(emp.name)
