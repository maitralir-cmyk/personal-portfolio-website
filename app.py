import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-key")

# Set DATABASE_URL to a MySQL connection string for MySQL.
# Example: mysql+pymysql://username:password@localhost/portfolio_db
database_url = os.environ.get("DATABASE_URL", "sqlite:///portfolio.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(250), nullable=False, default="")
    project_url = db.Column(db.String(300), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def seed_projects():
    """Add sample projects once so the portfolio is not empty."""
    if Project.query.count() == 0:
        samples = [
            Project(
                title="SmartCity Connect",
                description="A platform concept that helps citizens discover local services, report issues and stay informed about their city.",
                technologies="HTML, CSS, JavaScript, Flask",
                project_url="#"
            ),
            Project(
                title="Student Welfare Website",
                description="A student-focused website that brings useful campus information and support resources together.",
                technologies="HTML, CSS, JavaScript",
                project_url="#"
            ),
            Project(
                title="Data Analysis Project",
                description="A beginner data analysis project using Python and Pandas to explore and summarize structured data.",
                technologies="Python, Pandas, NumPy",
                project_url="#"
            ),
        ]
        db.session.add_all(samples)
        db.session.commit()


@app.route("/")
def home():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template("index.html", projects=projects)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all contact form fields.", "error")
        return redirect(url_for("home") + "#contact")

    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("home") + "#contact")

    db.session.add(ContactMessage(name=name, email=email, message=message))
    db.session.commit()
    flash("Thank you! Your message has been saved successfully.", "success")
    return redirect(url_for("home") + "#contact")


@app.route("/health")
def health():
    return {"status": "ok"}


with app.app_context():
    db.create_all()
    seed_projects()


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "true").lower() == "true",
            host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
