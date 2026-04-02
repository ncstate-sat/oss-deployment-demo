# Open Source CI/CD Demo - Random Value Generator

This project demonstrates the lifecycle of an open-source application, from
raw Python code to a publicly available container image via a standardized CI/CD pipeline.

When code is merged into the main branch, a GitHub Actions workflow is triggered to:

1. Execute a test suite.
2. Build the application into a Docker image (only if tests pass).
3. Publish that image to the GitHub Container Registry (GHCR).

The demo app is a random value generator built with FastAPI. Once running, you can
see the API documentation in your browser at `/docs`.

## Getting Started

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Run locally:** `fastapi dev`
3. **Run tests:** `pytest`

#### Running in a Container

1. **Build an image:** `docker build -t random-value-generator .`
2. **Run a container:** `docker run --name generator -p 8000:8000 random-value-generator`
3. **Run tests:** `docker exec -it generator bash` then `pytest`

## CI/CD Workflow Jobs

- **Run Tests:** Triggers `pytest` in a GitHub runner.
- **Build & Push:** On successful tests, an image is built and pushed to the GitHub Container Registry.

## API Endpoints

- `GET /`: Basic info.
- `POST /random-number`: Returns a random int between `bottom` and `top`.
- `POST /coin-flip`: Returns Heads or Tails.
- `POST /dice-roll`: Returns a list of results based on `number_of_dice`.
