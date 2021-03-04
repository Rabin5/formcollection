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
    DATABASE=postgres

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

- For non-development (staging / production) environment:
    - Use docker-compose.prod.yml
    - Setup .env.prod as following:
    ```
    DEBUG=0
    ENVIRONMENT=production
    SECRET_KEY=<secretkey>
    DJANGO_ALLOWED_HOSTS=*
    
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=<dbname>
    SQL_USER=<username>
    SQL_PASSWORD=<password>
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres

    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_USER='yourmail@gmail.com'
    EMAIL_HOST_PASSWORD='yourpassword'
    EMAIL_PORT=587
    ```

    - Set up environment file for database: .env.prod.db:
    ```
    POSTGRES_USER=<username>
    POSTGRES_PASSWORD=<password>
    POSTGRES_DB=<dbname>
    ```

- Run project (production):
    - Build and Start Container
    ```
    docker-compose -f docker-compose.prod.yml up --build
    ```
    - Install migrations;
        ```
        docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
        ```
    - Collect static files:
        ```
        docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
        ```
    - Load fixtures:
        ```
        docker-compose -f docker-compose.prod.yml exec web python manage.py loaddata master_data
        ```
    - Project will run on ```http://127.0.0.1:9021```

- For checking logs:
```
docker-compose -f docker-compose.prod.yml logs -f
```

- Bring containers and volumes down
```
docker-compose -f docker-compose.prod.yml down -v
```

- Install fixtures
    ```
    python manage.py loaddata master_data
    ```