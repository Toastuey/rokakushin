"""
Main Thread of Execution
"""
from src import data_io, hex_processing, visualize, constants

if __name__ == '__main__':
    # First get and trim down the relevant data we want
    df = data_io.load_earthquake_data([2011, 2012, 2013])
    df = data_io.select_relevant_columns(df)

    # Now create the corresponding hexes for each entry based on lat/lon
    df[constants.HEX_ID] = hex_processing.convert_to_hex(df["lat"], df["lon"])
    agg = hex_processing.create_agg(df)

    # Now visualize and create the corresponding HTML
    visualize.render_map(agg, "hex_map.html")
