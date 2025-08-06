Приложение "Сервис микроблогов".

1. Создаем приложение  FastApi в файле main.py.
2. Создаем приложение файлы Dockerfile и docker-compose.yml
3. Запустить Postgres через docker:
docker run --name skillbox-postgres --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e PGDATA=/var/lib/postgresql/data/pgdata -v /tmp:/var/lib/postgresql/data -p 5432:5432 -it postgres
4. Запустить контейнер: docker run -d --name postgresContainer -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres (postgresContainer - имя контейнера)
5. Запускаем ранее созданный контейнер: docker start feb0951f3505 (id контейнера)
6. В файле models.py создаем модели базы данных.
7. В файле schemas.py описываем схемы для нашего приложения.
8. В файле database.py создаем базу данных postgres (устанавливаем: pip install asyncpg для пути к базе данных).
9. Запустить приложение: uvicorn main:app --reload
10. Создаем ендпоинт '/' для загрузки фронтенда.
11. Ендпоинт '/api/users/me': получение страницы пользователя по api-key.
    Отображаются данные о пользовтеле, если он найден в базе данных по api-key.
    Если пользоваель в базе данных не найден, то отображается надпись "Пользователь по указанному api-key не найден."
    Есть возможность установить новый api-key.
12. 