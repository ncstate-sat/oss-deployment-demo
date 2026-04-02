from fastapi import FastAPI
from pydantic import BaseModel
import random

description = """
Generate various random values.

This application demos a public deployment of an application.
It comes complete with a GitHub Actions workflow that runs tests
and then publishes an image to the GitHub Container Registry.
"""

app = FastAPI(
    title="Random Generator",
    description=description
)

class RandomNumberRequestBody(BaseModel):
    bottom: int
    top: int

class DiceRollRequestBody(BaseModel):
    number_of_dice: int


@app.get("/", tags=['About'])
def get_basic_info():
    """
    Return a static string with a helpful tip.
    """
    return "Go to /docs to see what you can do with this app!"


@app.post("/random-number", tags=['Random Values'])
def get_random_number(body: RandomNumberRequestBody):
    """
    Return a random integer within a range.
    """
    return random.randint(body.bottom, body.top)


@app.post("/coin-flip", tags=['Random Values'])
def get_coin_flip_result():
    """
    Return the result of a coin flip.
    """
    random_int = random.randint(0, 1)
    return "Heads" if random_int == 0 else "Tails"


@app.post("/dice-roll", tags=['Random Values'])
def get_dice_roll_results(body: DiceRollRequestBody):
    """
    Return the results of a dice roll.
    """
    dice_roll_results = []
    for _ in range(body.number_of_dice):
        random_dice_value = random.randint(1, 6)
        dice_roll_results.append(random_dice_value)

    return dice_roll_results
