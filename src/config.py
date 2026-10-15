"""Configuration settings for the elections data file."""

from pathlib import Path

from packages.elections.src import utils

BASE_PATH = Path(__file__).parent.parent


if __name__ == "__main__":
    print(BASE_PATH)
    print(utils.get_file_path("eleicoes.csv"))
