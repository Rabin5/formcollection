OAGN COVID Reporting


- For developoment environment:
    - Setup .env.dev as following:
    ```
    DEBUG=1
    ENVIRONMENT=development
    SECRET_KEY=foo
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=oag_covid
    SQL_USER=admin
    SQL_PASSWORD=admin
    SQL_HOST=db
    SQL_PORT=5432

    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_USER='yourmail@gmail.com'
    EMAIL_HOST_PASSWORD='yourpassword'
    EMAIL_PORT=587
    ```

    - Setup .env for non-docker as following:
    ```
    DEBUG=1
    ENVIRONMENT=development
    SECRET_KEY=foo
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=oag_covid
    SQL_USER=admin
    SQL_PASSWORD=admin
    SQL_PORT=5432

    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_USER='yourmail@gmail.com'
    EMAIL_HOST_PASSWORD='yourpassword'
    EMAIL_PORT=587
    ```

- Install fixtures
    python manage.py loaddata master_data