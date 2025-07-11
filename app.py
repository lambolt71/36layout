import streamlit as st
from PIL import Image
import random
import os

st.set_page_config(layout="wide")
st.title("🧩 3×3 Tile Shuffler")

# --- Configuration ---
tile_folder = "tiles"  # folder containing t1.png through t9.png
tile_filenames = [f"t{i}.png" for i in range(1, 10)]

# --- Reshuffle logic ---
def generate_new_layout():
    tiles = tile_filenames.copy()
    random.shuffle(tiles)
    layout = [(tile, random.choice([0, 90, 180, 270])) for tile in tiles]
    return layout

# --- UI: Button ---
if "layout" not in st.session_state:
    st.session_state.layout = generate_new_layout()

if st.button("🔄 Reshuffle Layout"):
    st.session_state.layout = generate_new_layout()

# --- Display tiles in 3x3 grid ---
cols = st.columns(3, gap="small")
for idx, (filename, angle) in enumerate(st.session_state.layout):
    col = cols[idx % 3]
    path = os.path.join(tile_folder, filename)
    img = Image.open(path).rotate(angle, expand=True)
    col.image(img, use_container_width=True)
