# Quorus Tech Screen Project

## Project Description

This project comes with everything you'll need out of the box.
There are 3 containers in this repo:
 1. The FastAPI Application (`app/`)

 2. An External API you'll be pulling data from (`external-api/`)

 3. A PostgreSQL database with a default `User` model, a premade
    `Song` model, and an empty table containing a `Payout` model.
    (The `Payout` model only has the minimum required fields to run 
    and will be filled in as part of the tech screen.)

## Tech Screen Description

This tech screen is composed of two different problems designed to 
gauge your ability to write clean, human-readable code, see how you 
normally solve programming problems, and get an idea of what it's like
to work with you. We've made this test intentionally difficult, so there's
really no expectation to finish all of it or have it all run. We're mostly
focusing on how you approach a problem and what programming strategies you 
use to solve the problem. 

Here are the two features we'd like you to implement:

1. Data ingestion - Read and parse data from a flat file (`data_ingest/data_ingest.ira`) 
    and an "external" API (`http://localhost:4001/api/songs/{ISRC}`),
    use that data to fill out and save `Songs` to the database. 
    Put your solution in `src/crud/crud_song.py`. Additional details 
    about this problem can be found there. 
    
    - The `Song` model (`src/models/song.py`) has all the default fields
    we expect, but this model can be modified as you see fit 

2. Calculate Song Payouts - Using the data from question 1, create an     
   endpoint that, when given a song's ISRC along with some optional dates,
   returns the payout per play of that artist.  

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the project
 
1. Clone this repo
3. run `docker compose up --build`

### Running Tests

Tests can be run using `docker compose exec api python -m pytest`











