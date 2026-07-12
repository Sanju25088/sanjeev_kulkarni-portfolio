# Personal Portfolio

A modern, responsive personal portfolio website built using Django. It showcases my profile, skills, projects, and provides a contact form for visitors.

## Features

- Responsive design
- About Me section
- Skills section
- Projects showcase
- Contact form
- Admin dashboard for managing portfolio content

## Tech Stack

- Python
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Git & GitHub

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/portfolio.git
cd portfolio
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## Project Structure

```
portfolio/
│── manage.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md
│── portfolio/
│── static/
│── media/
│── templates/
```

## Contact

**Sanjeev Kulkarni**

- Email: sanjeev@klebca.in
- LinkedIn: https://linkedin.com/in/sanjeev-kulkarni-9610a225b

## License

This project is for learning and portfolio purposes.