import h3, csv
import pandas as pd
import pydeck as pdk

RESOLUTION = 4
HEIGHT_FLAT_SCALER = 10
lats = []
lons = []
magnitudes = []

with open("eq2023.csv", "r", encoding="utf-8") as eqdata, open("eq2022.csv", "r", encoding="utf-8") as eqdata2, open("eq2021.csv", "r", encoding="utf-8"):
    eqreader = csv.DictReader(eqdata, fieldnames=["time","latitude","longitude",
                                                  "depth","mag","magType","nst","gap","dmin","rms","net","id","updated","place",
                                                  "type","horizontalError","depthError","magError","magNst","status",
                                                  "locationSource","magSource"])
    eqreader2 = csv.DictReader(eqdata2, fieldnames=["time","latitude","longitude",
                                                      "depth","mag","magType","nst","gap","dmin","rms","net","id","updated","place",
                                                      "type","horizontalError","depthError","magError","magNst","status",
                                                      "locationSource","magSource"])
    eqreader3 = csv.DictReader(eqdata2, fieldnames=["time","latitude","longitude",
                                                          "depth","mag","magType","nst","gap","dmin","rms","net","id","updated","place",
                                                          "type","horizontalError","depthError","magError","magNst","status",
                                                          "locationSource","magSource"])
    eqreader.__next__()
    eqreader2.__next__()
    eqreader3.__next__()
    for r in eqreader:
        lats.append(float(r["latitude"]))
        lons.append(float(r["longitude"]))
        magnitudes.append(float(r["mag"]))

    for r in eqreader2:
            lats.append(float(r["latitude"]))
            lons.append(float(r["longitude"]))
            magnitudes.append(float(r["mag"]))

    for r in eqreader3:
                lats.append(float(r["latitude"]))
                lons.append(float(r["longitude"]))
                magnitudes.append(float(r["mag"]))

hex_ids = [h3.latlng_to_cell(lat, lon, RESOLUTION) for lat, lon in zip(lats, lons)]

df = pd.DataFrame({"hex_id": hex_ids, "magnitude": magnitudes})
agg = df.groupby("hex_id", as_index=False).size().rename(columns={"size": "quake_count"})
agg["height_value"] = agg["quake_count"]*HEIGHT_FLAT_SCALER

layer = pdk.Layer(
    "H3HexagonLayer",
    agg,
    get_hexagon="hex_id",
    get_fill_color="[255, 255 - quake_count * 4, 0]",
    get_elevation="height_value",
    elevation_scale=2000,
    extruded=True,
    pickable=True,
    opacity=0.5,
)

view_state = pdk.ViewState(
    latitude=sum(lats) / len(lats),
    longitude=sum(lons) / len(lons),
    zoom=5,
    pitch=40,
)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
deck.to_html("hex_map.html")