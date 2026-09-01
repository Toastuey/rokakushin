"""
This file handles opening, reading, and storing data from the input files.
"""
import pandas as pd
from src import constants

def add_seismic_energy(df):
    """
    Calculates the total seismic energy released for each earthquake based on magnitude.
    
    Args:
        param1: The dataframe to utilize.
        
    Returns:
        A dataframe with a new energy related column appended.
        
    Raises:
        None
    """
    df["energy"] = 10 ** (1.5 * df["mag"] + 4.8)
    return df

def select_relevant_columns(df):
    """
    Trim all unimportant data from our dataframe.
    
    Args:
        param1: The dataframe to trim from.
        
    Returns:
        df: A pandas dataframe with data relevant for visualization.
        
    Raises:
        tbd
    """
    return df[["latitude", "longitude", "mag", "place", "time", "year", "depth", "energy"]].rename(
        columns={"latitude": "lat", "longitude": "lon", "mag": "magnitude"})

def load_earthquake_data(years, data_dir=constants.DATA_DIR, pattern="eq{year}.csv"):
    """
    Load the selected years of data into the visualization.

    Args:
        param1: A list of years to load data from.

    Returns:
        A pandas dataframe object that contains ALL data from the selected years.

    Raises:
        FileNotFoundError
    """
    dfs = []
    for year in years:
        path = data_dir / pattern.format(year=year)
        if not path.exists():
            raise FileNotFoundError(f"No data file for year {year}: {path}")
        df = pd.read_csv(path)
        df["year"] = year # broadcasting
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def load_all(year=None, data_dir=constants.DATA_DIR):
    """
    Load all available data into the visualization.
    
    Args:
        tbd
        
    Returns:
        tbd
        
    Raises:
        tbd
    """
    pass


def clear_earthquake_data(year, data_dir=constants.DATA_DIR, pattern="eq{year}.csv"):
    """
    Removes the selected year of data from the visualization.

    Args:
        tbd

    Returns:
        tbd

    Raises:
        FileNotFoundError
    """
    path = data_dir / pattern.format(year=year)
    if not path.exists():
        raise FileNotFoundError(f"No data file for year {year}: {path}")


def clear_all(year=None, data_dir=constants.DATA_DIR):
    """
    Clear all data from the visualization.
    
    Args:
        tbd
        
    Returns:
        tbd
        
    Raises:
        tbd
    """
    pass
