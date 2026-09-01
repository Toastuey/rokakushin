"""
Main Thread of Execution
"""
from src import data_io, hex_processing, visualize, constants

if __name__ == '__main__':
    # First get and trim down the relevant data we want
    df = data_io.load_earthquake_data([2023])
    df = data_io.add_seismic_energy(df)
    df = data_io.select_relevant_columns(df)

    # Select sorting mode
    sorting_mode = constants.FREQUENCY_MODE

    # Now create the corresponding hexes for each entry based on lat/lon
    df[constants.HEX_ID] = hex_processing.convert_to_hex(df["lat"], df["lon"])
    agg = hex_processing.create_agg(df, sorting_mode)

    # Now visualize and create the corresponding HTML
    visualize.render_map(agg, "hex_map.html", sorting_mode)
