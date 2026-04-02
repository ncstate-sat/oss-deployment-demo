# Public CI/CD Demo - Random Value Generator

A simple FastAPI application demonstrating automated testing and deployment via GitHub Actions.

## Getting Started

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Run locally:** `fastapi dev`
3. **Run tests:** `pytest`

#### Running in a Container

1. **Build an image:** `docker build -t random-generator .`
2. **Run a container:** `docker run --name generator -p 8000:8000 random-generator`
3. **Run tests:** `docker exec -it generator bash` then `pytest`

## CI/CD Workflow Jobs

- **Run Tests:** Triggers `pytest` in a GitHub runner.
- **Build & Push:** On successful tests, an image is built and pushed to the GitHub Container Registry.

## API Endpoints

- `GET /`: Basic info.
- `POST /random-number`: Returns a random int between `bottom` and `top`.
- `POST /coin-flip`: Returns Heads or Tails.
- `POST /dice-roll`: Returns a list of results based on `number_of_dice`.
