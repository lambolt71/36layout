import streamlit as st
from PIL import Image
import random
import os

st.set_page_config(layout="wide")
st.title("🧩 3×3 Tile Shuffler")

# --- Configuration ---
tile_folder = "tiles"  # This folder must exist and contain t1.png to t9.png
tile_filenames = [f"t{i}.png" for i in range(1, 10)]

# --- Utility: Load and shuffle layout ---
def generate_new_layout():
    tiles = tile_filenames.copy()
    random.shuffle(tiles)
    return [(tile, random.choice([0, 90, 180, 270])) for tile in tiles]

# --- Safety: Ensure files exist ---
missing_files = [f for f in tile_filenames if not os.path.exists(os.path.join(tile_folder, f))]
if missing_files:
    st.error(f"Missing image files: {', '.join(missing_files)} in folder '{tile_folder}'")
    st.stop()

# --- Initialize or reshuffle ---
if "layout" not in st.session_state:
    st.session_state.layout = generate_new_layout()

if st.button("🔄 Reshuffle Layout"):
    st.session_state.layout = generate_new_layout()

# --- Display tiles in 3x3 grid ---
cols = st.columns(3, gap="small")
for idx, (filename, angle) in enumerate(st.session_state.layout):
    path = os.path.join(tile_folder, filename)
    img = Image.open(path).rotate(angle, expand=True)
    cols[idx % 3].image(img, width=160)  # Fixed width for each tile
