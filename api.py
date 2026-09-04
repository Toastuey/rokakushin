# api.py
from fastapi import FastAPI, Query
from typing import List
from src import data_io, hex_processing, constants
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/hexdata")
def get_hex_data(years: List[int] = Query(...), sorting_mode=constants.FREQUENCY_MODE):
        df = data_io.load_earthquake_data(years)
        df = data_io.add_seismic_energy(df)
        df = data_io.select_relevant_columns(df)
        df[constants.HEX_ID] = hex_processing.convert_to_hex(df["lat"], df["lon"])
        agg = hex_processing.create_agg(df, sorting_mode)
        agg = hex_processing.normalize_colors(agg, constants.VALUE_COLUMN)
        return agg.to_dict(orient="records")