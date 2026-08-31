from pathlib import Path

# Hex Related Constants
RESOLUTION = 4
HEIGHT_FLAT_SCALER = 10

# Data Related Constants
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# Map Related Constants
HEX_NAME = "quake_count"
HEX_ID = "hex_id"
HEIGHT_VALUE = "height_value"
ELEVATION_SCALE = 2000
COLOR_SENSITIVITY = 4
COLOR_R = 255
COLOR_B = 0
COLOR_OPACITY = 0.6