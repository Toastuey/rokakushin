"""
This file is responsible for converting map data into h3 hexes and creating a pandas dataframe to be used.
"""
from src import constants
import h3
import numpy as np

def convert_to_hex(inlat, inlon):
    """
    Convert the provided longitude/latitude pairs into h3 hexes.

    Args:
        param1: A column from a dataframe corresponding to all latitudes.
        param2: A column from a dataframe corresponding to all longitudes.

    Returns:
        A list of all hex ids for every entry in the provided dataframe.

    Raises:
        None
    """
    return [h3.latlng_to_cell(lat, lon, constants.RESOLUTION) for lat, lon in zip(inlat, inlon)]


def normalize_colors(agg, value_col):
    min_val = agg[value_col].min()
    max_val = agg[value_col].max()
    
    if max_val == min_val:
        # avoid divide-by-zero if every hex has the same value
        agg[constants.COLOR_VALUE] = 0
    else:
        agg[constants.COLOR_VALUE] = (
            (agg[value_col] - min_val) / (max_val - min_val) * 255
        )
    return agg


def create_agg(df, sortby=constants.FREQUENCY_MODE):
    """
    Creates a correct aggregate based on the data.
    
    Args:
        param1: The working dataframe.
        param2: The aggregate mode requested for data visualization. | Defaults: constants.FREQUENCY_MODE
    
    Returns:
        An aggregate of the given data frame relative to the sorting mode provided.
        
    Raises:
        tbd
    """
    agg = None
    match sortby:
        case constants.MEAN_MAGNITUDE_MODE:
            agg = df.groupby(constants.HEX_ID, as_index=False)["magnitude"].mean().rename(columns={"magnitude": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = agg[constants.VALUE_COLUMN] * constants.HEIGHT_FLAT_SCALER
        case constants.MAX_MAGNITUDE_MODE:
            agg = df.groupby(constants.HEX_ID, as_index=False)["magnitude"].max().rename(columns={"magnitude": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = agg[constants.VALUE_COLUMN] * constants.HEIGHT_FLAT_SCALER
        case constants.MEAN_DEPTH_MODE:
            agg = df.groupby(constants.HEX_ID, as_index=False)["depth"].mean().rename(columns={"depth": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = agg[constants.VALUE_COLUMN] * constants.HEIGHT_FLAT_SCALER
        case constants.MIN_DEPTH_MODE:
            agg = df.groupby(constants.HEX_ID, as_index=False)["depth"].min().rename(columns={"depth": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = agg[constants.VALUE_COLUMN] * constants.HEIGHT_FLAT_SCALER
        case constants.TOTAL_SEISMIC_MODE:
            agg = df.groupby(constants.HEX_ID, as_index=False)["energy"].sum().rename(columns={"energy": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = np.log1p(agg[constants.VALUE_COLUMN]) * constants.HEIGHT_FLAT_SCALER # Take log here, numbers are HUGE
        case _: # Default case is frequency 
            agg = df.groupby(constants.HEX_ID, as_index=False).size().rename(columns={"size": constants.VALUE_COLUMN})
            agg[constants.HEIGHT_VALUE] = agg[constants.VALUE_COLUMN]*constants.HEIGHT_FLAT_SCALER

    return agg
