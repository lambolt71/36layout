import streamlit as st
import random
from PIL import Image
import base64
from io import BytesIO

TILE_SIZE = 160
tile_files = [f"tiles/t{i+1}.png" for i in range(9)]

# --- Initialize layout and rotations once ---
if "layout" not in st.session_state:
    st.session_state.layout = random.sample(tile_files, len(tile_files))
    st.session_state.rotations = [random.choice([0, 90, 180, 270]) for _ in range(9)]

# --- Shuffle on button click ---
if st.button("🔁 Shuffle Layout"):
    st.session_state.layout = random.sample(tile_files, len(tile_files))
    st.session_state.rotations = [random.choice([0, 90, 180, 270]) for _ in range(9)]

# --- Convert images to base64 for inline display ---
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- Prepare rotated image HTML blocks ---
img_html_blocks = []
for path, angle in zip(st.session_state.layout, st.session_state.rotations):
    img = Image.open(path).rotate(angle, expand=True).resize((TILE_SIZE, TILE_SIZE))
    img_b64 = image_to_base64(img)
    html_img = f'<img src="data:image/png;base64,{img_b64}" style="width:{TILE_SIZE}px;height:{TILE_SIZE}px;margin:0;padding:0;display:block;" />'
    img_html_blocks.append(html_img)

# --- 3x3 Grid ---
grid_html = f"""
<div style="
    display: grid;
    grid-template-columns: repeat(3, {TILE_SIZE}px);
    grid-template-rows: repeat(3, {TILE_SIZE}px);
    gap: 0;
    padding: 0;
    margin: 0;
">
    {''.join(f'<div>{img}</div>' for img in img_html_blocks)}
</div>
"""

st.markdown("## 🎲 Random Setup for 36 by Néstor Romeral Andrés")
st.markdown(grid_html, unsafe_allow_html=True)
