"""Utility functions for formatting numbers according to Brazilian conventions."""

from pathlib import Path

from packages.elections.src.config import BASE_PATH


def br_number(number: float | str, decimals: int = 2) -> str:
    """Format a number according to Brazilian conventions.

    Args:
        number (float | str): The number to be formatted.
        decimals (int): The number of decimal places to format the number with. Default is 2.

    Returns:
        str: The formatted number as a string with thousands separator. Example: 1.234.567,89
    """
    # Deve coverter formatos como "1234567,59" para "1.234.567,59" ou "1234567.59" para "1.234.567,59"
    if isinstance(number, str):
        number = number.replace(",", ".")
        number = float(number)
    formatted_number = (
        f"{number:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    return str(formatted_number)


def get_file_path(file: str) -> Path:
    """Get the full file path for the election data CSV file."""
    file_path: Path = BASE_PATH.joinpath("data", file)
    if not file_path.is_file():
        raise FileNotFoundError(f"The file < {file} > does not exist.")
    return file_path


def normalize_file_name(file_name: str) -> str:
    """Remove surrounding spaces and replace inner spaces with underscores."""
    return file_name.strip().replace(" ", "_")


def set_file_path(file_name: str) -> Path:
    """Set the full file path for the election data CSV file."""
    normalized_file_name = normalize_file_name(file_name)
    file_path: Path = BASE_PATH.joinpath("data", normalized_file_name)
    if file_path.is_file():
        raise FileExistsError(f"O arquivo < {normalized_file_name} > já existe.")
    return file_path


if __name__ == "__main__":
    N_SAMPLE_01 = "123456"
    N_SAMPLE_02 = "123456,56"
    N_SAMPLE_03 = "123456.56"

    formatted_number_01 = br_number(N_SAMPLE_01, 0)
    formatted_number_02 = br_number(N_SAMPLE_02, 2)
    formatted_number_03 = br_number(N_SAMPLE_03, 2)

    print(formatted_number_01)
    print(formatted_number_02)
    print(formatted_number_03)
