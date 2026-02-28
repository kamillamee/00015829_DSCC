# Task Manager - Distributed Systems & Cloud Computing

A Django web application for managing projects and tasks, containerized with Docker and deployed via CI/CD pipeline.

## Features

- **User Authentication**: Login, logout, registration
- **Projects & Tasks**: Create, read, update, delete projects and tasks
- **Database Models**: Project (many-to-one User), Task (many-to-one Project, many-to-many Tag), Tag
- **Admin Panel**: Full Django admin configuration
- **5+ Functional Pages**: Home, Login, Register, Project List, Project Detail, Task CRUD

## Technologies Used

- **Backend**: Django 4.2, Python 3.11
- **Database**: PostgreSQL 15
- **Web Server**: Nginx, Gunicorn
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions

## Local Setup

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Development without Docker

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
cp .env.example .env
# Edit .env with your settings

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Development with Docker

```bash
cp .env.example .env
# Set DOCKERHUB_USERNAME=local in .env for local builds

docker compose up --build
# Access at http://localhost
```

### Run Tests

```bash
pytest tasks/ -v
```

## Deployment

### Server Setup (Eskiz/Ubuntu)

1. Install Docker and Docker Compose
2. Clone repository to `/opt/cloudcomputing`
3. Configure `.env` with production values
4. Configure UFW: `ufw allow 22,80,443`
5. For HTTPS: Use Let's Encrypt (certbot) and place certs in `nginx/ssl/`

### GitHub Actions Deployment

Required GitHub Secrets:

| Secret | Description |
|--------|-------------|
| DOCKERHUB_USERNAME | Docker Hub username |
| DOCKERHUB_TOKEN | Docker Hub access token |
| SSH_HOST | Server IP or hostname |
| SSH_USERNAME | SSH user (e.g. root) |
| SSH_PRIVATE_KEY | Private key for SSH |
| DEPLOY_PATH | (Optional) Server path, default `/opt/cloudcomputing` |

Pipeline triggers on push to `main` branch.

### Manual Deployment

```bash
# On server
cd /opt/cloudcomputing
git pull
docker compose pull
docker compose up -d
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | (required) |
| DEBUG | Debug mode | False |
| ALLOWED_HOSTS | Comma-separated hosts | localhost |
| POSTGRES_DB | Database name | cloudcomputing_db |
| POSTGRES_USER | DB user | postgres |
| POSTGRES_PASSWORD | DB password | (required) |
| POSTGRES_HOST | DB host | db (Docker) |
| DOCKERHUB_USERNAME | For image tagging | local |

## Project Structure

```
├── config/          # Django settings
├── tasks/           # Main application
├── nginx/           # Nginx configuration
├── .github/         # GitHub Actions workflows
├── Dockerfile       # Multi-stage build
├── docker-compose.yml
└── requirements.txt
```

## Screenshots

*(Add screenshots of your running application here)*

## License

Educational project - WIUT DSCC Coursework.
