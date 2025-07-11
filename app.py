import streamlit as st
from PIL import Image
import random
import os

st.set_page_config(layout="centered")
st.title("🎲 Random 3×3 Tile Grid")

# --- Setup ---
TILE_DIR = "tiles"  # Folder where your tile PNGs are stored
tile_filenames = [f"t{i}.png" for i in range(1, 10)]  # t1.png to t9.png

# Load images
tiles = []
for fname in tile_filenames:
    try:
        img = Image.open(os.path.join(TILE_DIR, fname))
        tiles.append(img)
    except FileNotFoundError:
        st.error(f"Missing file: {fname}")
        st.stop()

# --- Shuffle button ---
if st.button("🔄 Reshuffle Tiles"):
    st.session_state.shuffled = True

if "shuffled" not in st.session_state:
    st.session_state.shuffled = True

if st.session_state.shuffled:
    # Randomize tile order and rotations
    tile_indices = list(range(9))
    random.shuffle(tile_indices)
    rotations = [random.choice([0, 90, 180, 270]) for _ in range(9)]

    # Display 3×3 grid
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            tile = tiles[tile_indices[idx]].rotate(rotations[idx])
            cols[col].image(tile, use_container_width=True)

    st.session_state.shuffled = False
