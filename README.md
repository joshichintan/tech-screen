# Quorus Tech Screen Project

## Project Description

This project comes with everything you'll need out of the box.
There are 3 containers in this repo:

1.  The FastAPI Application (`app/`)

1.  An External API you'll be pulling data from (`external-api/`)

1.  A PostgreSQL database with a default `User` model, a premade
    `Song` model, and an empty table containing a `Payout` model.
    (The `Payout` model only has the minimum required fields to run
    and will be filled in as part of the tech screen.)

## Tech Screen Description

This tech screen is composed of three different problems designed to
gauge your ability to write clean, human-readable code, see how you
normally solve programming problems, and get an idea of what it's like
to work with you. We've made this test intentionally difficult, so there's
really no expectation to finish all of it or have it all run. We're mostly
focusing on how you approach a problem and what programming strategies you
use to solve the problem.

Here are the two features we'd like you to implement:

1. Data ingestion - Read and parse data from a flat file (`data_ingest/data_ingest.ira`)
   and an "external" API (`http://localhost:4001/api/songs/{ISRC-slug}`),
   use that data to fill out and save `Songs` to the database.
   Put your solution in `src/crud/crud_song.py`. Additional details
   about this problem can be found there.

   - The `Song` model (`src/models/song.py`) has all the default fields
     we expect, but this model can be modified as you see fit

1. Calculate Song Payouts - Using the data from question 1, create an
   endpoint that, when given a song's ISRC along with some optional dates,
   returns the payout per play of that artist.

1. Order-Trade Matching - Update `order-trade-matching/domain/matcher.py::match_orders_trades`
   so that given a list of `Orders` and `Trades`, the function returns a list of `Matches` which associates
   an `Order` with a `Trade`.

   For example:

   - Order: Buy 50 AAPL on 2023-01-10 matches
     Trade: Buy 50 AAPL on 2023-01-10
   - Order1: Sell 1 BTC on 2023-02-20, Order2: Sell 0.5 BTC on 2023-02-20
     matches Trade: Sell 1.5 BTC @ $30001.48 on 2023-02-20
   - Order: Buy 100 USBOND on 2023-03-15 matches
     Trade1: Buy 50 USBOND @ $518.5 on 2023-03-15,
     Trade 2: Buy 50 USBOND @ $518.7 on 2023-03-15

   Models are defined in `./order-trade-matching/domain/models.py`, and sample data that is used in the test case is defined in `./order-trade-matching/domain/data.py`.

   Run the test case with `python order-trade-matching/main.py` to see if your implementation passes the test.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the project

1. Clone this repo
1. Create a `.env` file in `app/quorus-chorus`. There is a `.env.sample` file there that you can copy and rename.
1. run `docker compose up --build`

- The FastAPI app will be available at http://localhost:4000. Visit http://localhost:4000/docs for the interactive FastAPI docs.
- The database will be available at `localhost:5432`
- The mock "3rd party API" will be available at http://localhost:4001
  - More info on the mock API is available in [external-api/README.md](external-api/README.md)

### Debugging

To enable debugger support, set the `DEBUG` environment variable to `True` in your `app/quorus-chorus/.env` file.

If you're using VSCode, there is a launch configuration in [.vscode/launch.json](.vscode/launch.json) that will allow you to debug the FastAPI app. You can set breakpoints in your code and step through it. The debug client is available on port `5678`.

### Running Tests

**Note:** The tests will fail immediately if the api container was run with `DEBUG=True`. This is because the tests run the app in a separate process, and the debugger can't attach to it if it's already running in another process. If you want to run the tests, first set `DEBUG=False` in your `app/quorus-chorus/.env` file.

Tests can be run using `docker compose exec api python -m pytest`

### Running Migrations

Database migrations are managed with [Alembic](https://alembic.sqlalchemy.org/en/latest/). To create a migration after you've changed a model, run:

```bash
docker-compose exec api alembic revision --autogenerate -m "migration message"
```

This will create a new migration file in `app/quorus_chorus/migrations/versions`. You can then apply the migration with:

```bash
docker-compose exec api alembic upgrade head
```
