## (Run DB)

docker run --name hunting_postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=user -e POSTGRES_DB=irr -p 5432:5432 -d postgres:13.0-alpine
