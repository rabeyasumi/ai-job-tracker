# AI Job Application Tracker

A full-stack Django web application that helps users manage and track their job applications from one place. Featuring an **AI-driven, gamified analysis dashboard** that compares user profiles against job descriptions to generate visual performance match percentages, skill breakdown tags, and personalized learning paths.

## 🚀 Features

- **User Authentication**: Secure user registration, login, and logout.
- **Interactive Dashboard**: Real-time summary statistics of application statuses and upcoming interview timelines.
- **Job Application CRUD**: Create, view, update, and delete job applications effortlessly.
- **Advanced Search & Filter**: Search applications by job title or company name, and filter by status and location.
- **Interview Management**: Schedule, track, and manage upcoming interviews directly from the dashboard.
- **AI-Powered Skill Analysis**: Integrates with Groq AI (`gpt-oss-20b`) to perform deep job description evaluations.
- **Gamified Visual Feedback**: Dynamic circular progress rings, matched vs. missing skill tags, and comprehensive step-by-step learning paths.
- **Online Judge Aesthetic**: Custom CSS system featuring glassmorphism, translucent gradients, and polished UI variables.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **AI Integration**: Groq API (`gpt-oss-20b`)
- **Frontend**: HTML5, Vanilla JavaScript (DOM animations), Custom CSS (Online Judge inspired themes)
- **Database**: SQLite (Local development)

---

## 📂 Project Structure

```text
ai-job-tracker/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jobs/
│   ├── migrations/
│   ├── templates/
│   │   └── jobs/
│   │       ├── ai_analysis.html
│   │       ├── application_detail.html
│   │       ├── application_form.html
│   │       ├── application_list.html
│   │       ├── dashboard.html
│   │       └── ...
│   ├── ai_service.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── jobs/
│       └── style.css
├── manage.py
├── .env                  # Local only; do not commit
├── .gitignore
└── requirements.txt