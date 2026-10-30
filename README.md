# Personal Portfolio Website — Full Stack

A responsive personal portfolio built with **HTML, CSS, JavaScript, Python Flask and SQLAlchemy**. Project information is loaded from a database, and contact form submissions are stored in the database.

## Features

- Responsive home page with navigation
- About, skills and projects sections
- Projects are loaded dynamically from the database
- Contact form with basic validation
- Contact messages are saved to the database
- SQLite works immediately for local development
- MySQL is supported through the `DATABASE_URL` environment variable
- Health-check endpoint at `/health`

## 1. Requirements

- Python 3.10 or newer
- VS Code (recommended)
- Internet connection for the Google Fonts used in the design

## 2. Run on your computer

Open this project folder in VS Code. Open the terminal in the project folder and run:

### Windows

```bash
py -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

If `py` does not work, try `python` instead.

Open this address in your browser:

`http://127.0.0.1:5000`

The first run automatically creates `portfolio.db` and inserts three sample projects.

## 3. Personalize the website

Open `templates/index.html` and replace:
- `Alex Morgan` with your name
- The introduction and About Me paragraphs with your own details
- Skills with the technologies you know
- `Based in India` with your location if you want

Edit the sample project entries in the `seed_projects()` function in `app.py`. If the database already exists, the sample entries will not be inserted again. To reset sample data during development, stop the server, delete `portfolio.db`, and start the app again.

## 4. Database

The app uses SQLAlchemy models:

- `Project`: title, description, technologies and project URL
- `ContactMessage`: visitor name, email, message and date

SQLite is selected by default so the project runs without installing a database server. To use MySQL, create a database named `portfolio_db`, then set the environment variable:

```text
DATABASE_URL=mysql+pymysql://username:password@localhost/portfolio_db
```

Replace `username` and `password` with your MySQL credentials. Never upload real passwords or secret keys to GitHub.

## 5. Push to GitHub

1. Create a new repository on GitHub.
2. Extract this project ZIP.
3. Open the extracted folder in VS Code.
4. Open the terminal and run:

```bash
git init
git add .
git commit -m "Create personal portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own GitHub repository URL.

## 6. Deploy on Render

1. Push the project to GitHub.
2. Sign in to Render and choose **New → Web Service**.
3. Connect your GitHub repository.
4. Use these settings:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Add environment variables:
   - `SECRET_KEY`: a long random secret value
   - `DATABASE_URL`: a persistent MySQL or PostgreSQL database connection string if using an external database

For a real deployed site, use a persistent managed database. The default SQLite database is suitable for local demonstration, but a local SQLite file may not persist across some hosting redeployments or instances.

## 7. Project structure

```text
personal_portfolio_fullstack/
│   app.py
│   requirements.txt
│   Procfile
│   README.md
│   .env.example
│   .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## Assignment explanation

**Frontend:** HTML provides the page structure, CSS provides responsive styling, and JavaScript controls the mobile navigation and footer year.

**Backend:** Flask handles page requests and the contact form.

**Database:** SQLAlchemy stores project details and contact messages in SQLite by default, with MySQL connection support.

**Expected outcome:** A working full-stack portfolio that brings the frontend, backend and database together in one live project.
