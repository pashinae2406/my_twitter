Приложение сервис микроблогов.

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
10. 