# 1. Base image
FROM python:3.12-slim

# 2. Environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project files
COPY . .

# 6. Collect static files
RUN python manage.py collectstatic --noinput

# 7. Install NGINX
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# 8. Copy NGINX config
COPY nginx/default.conf /etc/nginx/sites-available/default

# 9. Expose port (Railway uchun)
EXPOSE 8000

# 10. Start Gunicorn + NGINX
CMD service nginx start && gunicorn root.wsgi:application --bind 0.0.0.0:8080
