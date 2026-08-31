"""
This file is responsible for converting map data into h3 hexes and creating a pandas dataframe to be used.
"""
from src import constants
import h3

def convert_to_hex(inlat, inlon):
    """
    Convert the provided longitude/latitude pairs into h3 hexes

    Args:
        tbd

    Returns:
        tbd

    Raises:
        tbd
    """
    return [h3.latlng_to_cell(lat, lon, constants.RESOLUTION) for lat, lon in zip(inlat, inlon)]


def create_agg(df):
    """
    Creates a correct aggregate based on the data
    
    Args:
        tbd
    
    Returns:
        tbd
        
    Raises:
        tbd
    """
    agg = df.groupby(constants.HEX_ID, as_index=False).size().rename(columns={"size": constants.HEX_NAME})
    agg[constants.HEIGHT_VALUE] = agg[constants.HEX_NAME]*constants.HEIGHT_FLAT_SCALER
    return agg
