# Docker Compose Flask and MySQL App

A small Flask API connected to MySQL with Docker Compose. The MySQL image is initialized with a `students` table and sample records on its first start.

## Project Structure

```text
.
├── .dockerignore
├── .gitignore
├── .env
├── docker-compose.yaml
├── README.md
├── mysql/
│   ├── Dockerfile
│   └── database_students.sql
└── python/
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

## Prerequisites

- Docker Desktop with Docker Compose support
- A free host port `8000`

## Repository Files

- `.gitignore` excludes local environment files, Python-generated files, editor metadata, and logs from Git.
- `.dockerignore` excludes secrets, repository metadata, documentation, caches, and logs when the repository root is used as a Docker build context.

The Compose services currently use `mysql/` and `python/` as separate build contexts, so only files in those directories are sent to their respective Docker builds.

## Configuration

Create a `.env` file beside `docker-compose.yaml`. It is ignored by Git because it contains credentials:

```env
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=students
MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=root
```

`MYSQL_HOST` must be `mysql`, which is the MySQL service name on the Compose network. Do not commit real passwords or other secrets to source control.

## Run the Application

Build and start both containers in the background:

```bash
docker compose up --build -d
```

Check container status:

```bash
docker compose ps
```

The Flask API is available at `http://localhost:8000`.

## API Endpoints

### Health check

```http
GET /
```

Returns:

```text
Welcome to the Flask MySQL App!
```

### List students

```http
GET /students
```

Example:

```bash
curl http://localhost:8000/students
```

The response is a JSON array containing the sample students loaded from `mysql/database_students.sql`.

## Logs and Shutdown

View application logs:

```bash
docker compose logs -f python
```

Stop the services:

```bash
docker compose down
```

Stop the services and delete the MySQL data volume:

```bash
docker compose down -v
```

Deleting the volume removes the database data. The SQL initialization script runs again the next time the MySQL container is created with an empty data directory.

## Troubleshooting

- If `/students` fails immediately after startup, MySQL may still be initializing. Check `docker compose logs mysql` and retry once the database is ready.
- If port `8000` is already in use, change the host side of the mapping in `docker-compose.yaml`, for example `8001:5000`, and use `http://localhost:8001`.
- If the database was initialized with incorrect credentials, run `docker compose down -v` and start the stack again after correcting `.env`.

## Stop and Remove Containers

To stop and remove the containers and network while preserving the database volume:

```bash
docker compose down
```
