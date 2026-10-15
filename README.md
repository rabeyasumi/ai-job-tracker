# AI Job Application Tracker

A Django-based web application that helps users manage and track their job applications from one place. Users can organize applications, monitor their status, schedule interviews, and analyze job descriptions with AI.

## YouTube Live Demo

▶️ [Watch the project demo on YouTube](https://www.youtube.com/watch?v=ad2zEBUP2eQ)

## Features

- User registration, login, and logout
- Personal job application dashboard
- Create, view, update, and delete job applications
- Track application statuses
- Search applications by job title or company
- Filter applications by status and location
- Schedule and manage interviews
- View upcoming interviews from the dashboard
- AI-powered job description analysis
- Simple, responsive styling with CSS

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite (local development database; depending on project configuration)

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai-job-tracker
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository's GitHub URL.

### 2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

If the project does not have a `requirements.txt` file yet, create one from your active project environment:

```bash
pip freeze > requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root. Add the environment variables required by your project, for example:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
GROQ_API_KEY=your_groq_api_key
```

Use the exact variable names expected by your Django settings and AI integration. Do not commit `.env` or publish API keys. The `.env` file should remain local and be excluded by `.gitignore`.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```text
ai-job-tracker/
├── jobs/
│   ├── templates/
│   │   └── jobs/
│   ├── static/
│   │   └── jobs/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── .env                 # Local only; do not commit
├── .gitignore
└── requirements.txt
```

The structure above is illustrative. Your actual project may contain additional files and folders.

## Security Notes

- Never commit `.env` files, API keys, passwords, or other secrets.
- Keep `DEBUG=True` only for local development.
- Before deployment, configure production environment variables and set `DEBUG=False`.
- If an API key has been exposed in Git history, revoke it and create a new one.

## Future Improvements

- Add application categories and tags
- Improve dashboard charts and statistics
- Add pagination for large application lists
- Improve form validation and user experience
- Deploy the application for public access

## Author

Developed as a job application tracking project using Django and AI-powered job description analysis.