"""Processed data module for extracting election data from CSV files."""

import pandas as pd

from packages.elections.src import utils


def extraction(file_path: str) -> pd.DataFrame:
    """Extraction data from CSV file.

    Args:
        file_path (str): Path to the CSV file containing the election data.

    Returns:
        pd.DataFrame: DataFrame containing the election data with appropriate data types.
    """

    # Define the columns and their respective names and data types for the CSV file.
    columns: dict[str, tuple[str, str]] = {
        "ano": ("ano", "int64"),
        "estado": ("estado", "category"),
        "cidade": ("cidade", "category"),
        "zona": ("zona", "category"),
        "secao": ("secao", "category"),
        "cargo": ("cargo", "category"),
        "candidato": ("candidato", "category"),
        "partido": ("partido", "category"),
        "numero": ("numero", "category"),
        "votos": ("votos", "int64"),
    }
    columns_dtype: dict[str, str] = {col: dtype for col, dtype in columns.values()}

    dataframe: pd.DataFrame = pd.read_csv(file_path, dtype=columns_dtype)
    return dataframe


def save_to_csv(data: pd.DataFrame, file_name: str) -> bool:
    """Save the election data to a CSV file.

    If the file already exists, asks the user whether it should be overwritten.

    Args:
        data (pd.DataFrame): The election data to save.
        file_name (str): The name of the CSV file.

    Returns:
        bool: True if the file was saved, False if the user cancelled the overwrite.
    """
    try:
        file_path = utils.set_file_path(file_name)
    except FileExistsError as e:
        print(e)
        option = input("Sobrescrever? [s/N]: ")
        if option.strip().casefold() not in {"s", "sim", "y", "yes"}:
            return False
        file_path = utils.get_file_path(utils.normalize_file_name(file_name))
    data.to_csv(file_path, index=False)
    return True


def run():
    """Run the data extraction process and return the election data as a DataFrame."""
    dataframe = extraction(str(utils.get_file_path("eleicoes.csv")))
    return dataframe


if __name__ == "__main__":
    print(run().head())

    print(f"Memory usage: {run().memory_usage(deep=True).sum()} bytes")
