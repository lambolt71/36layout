import streamlit as st
from PIL import Image
import random
import os

st.set_page_config(layout="centered")
st.title("🎲 Random 3×3 Tile Grid")

# Load tile images
TILE_DIR = "tiles"  # Make sure you have a folder named 'tiles' with 9 PNGs
tile_filenames = [f"tile_{i}.png" for i in range(9)]
tiles = [Image.open(os.path.join(TILE_DIR, fname)) for fname in tile_filenames]

# Create a reshuffle button
if st.button("🔄 Reshuffle Tiles"):
    st.session_state.shuffled = True

# Ensure we always have a state
if "shuffled" not in st.session_state:
    st.session_state.shuffled = True

if st.session_state.shuffled:
    # Randomly shuffle tile indices and rotations
    tile_indices = list(range(9))
    random.shuffle(tile_indices)
    rotations = [random.choice([0, 90, 180, 270]) for _ in range(9)]

    # Arrange and show tiles in 3 rows
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            tile_image = tiles[tile_indices[idx]].rotate(rotations[idx])
            cols[col].image(tile_image, use_column_width=True)

    st.session_state.shuffled = False
