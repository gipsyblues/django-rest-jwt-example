# Django REST JWT Auth Example
JWT auth and registration example (on top of example from Django REST Framework official website)
- JWT auth using djangorestframework-simplejwt
- API user registration using dj-rest-auth
- Custom User model to replace usernames with emails
- Dockerized

# Run with docker-compose
```
docker-compose up -d --build
docker-compose exec web ./manage.py migrate
docker-compose exec web ./manage.py createsuperuser
```
