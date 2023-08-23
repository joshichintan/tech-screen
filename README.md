# Quorus Tech Screen Project Template

This is the template project for Quorus Tech Screens. Fork this repo and use it as a starting point for your project.

## Project Description

Out of the box there is a wired-up PostgreSQL database, pgAdmin4, and a [FastAPI](https://fastapi.tiangolo.com/) app with a `User` model and a few endpoints.

## Getting Started

### Prerequisites



Having Python installed is helpful primarily for e.g. linting. If you're using VSCode, there are several recommended extensions in [.vscode/extensions.json](.vscode/extensions.json) that I find helpful anyway.

### Running the Project

1. Fork this repo
1. Clone your fork
1. `cd` into the project directory
1. Create a `.env` file in `app/quorus-chorus`. There is a `.env.sample` file there that you can copy and rename.
1. Run `docker-compose up --build`

- The FastAPI app will be available at http://localhost:4000. Visit http://localhost:4000/docs for the interactive FastAPI docs.
- The database will be available at `localhost:5432`
- pgAdmin4 will be available at http://localhost:5050
- The mock "3rd party API" will be available at http://localhost:4001
  - More info on the mock API is available in [external-api/README.md](external-api/README.md)

### Debugging

To enable debugger support, set the `DEBUG` environment variable to `True` in your `app/quorus-chorus/.env` file.

If you're using VSCode, there is a launch configuration in [.vscode/launch.json](.vscode/launch.json) that will allow you to debug the FastAPI app. You can set breakpoints in your code and step through it. The debug client is available on port `5678`.

### Running Migrations

Database migrations are managed with [Alembic](https://alembic.sqlalchemy.org/en/latest/). To create a migration after you've changed a model, run:

```bash
docker-compose exec api alembic revision --autogenerate -m "migration message"
```

This will create a new migration file in `app/quorus_chorus/migrations/versions`. You can then apply the migration with:

```bash
docker-compose exec api alembic upgrade head
```

### Running Tests

**Note:** The tests will fail immediately if the api container was run with `DEBUG=True`. This is because the tests run the app in a separate process, and the debugger can't attach to it if it's already running in another process. If you want to run the tests, first set `DEBUG=False` in your `app/quorus-chorus/.env` file.

You can run the Quorus Chorus tests in the container with:

```bash
docker-compose exec api python -m pytest /app
```
