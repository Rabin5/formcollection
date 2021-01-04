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
    ```