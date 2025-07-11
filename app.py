import streamlit as st
import random
from PIL import Image
import base64
from io import BytesIO

# --- Load and rotate images ---
tile_files = [f"tiles/t{i+1}.png" for i in range(9)]
layout = random.sample(tile_files, len(tile_files))
rotations = [random.choice([0, 90, 180, 270]) for _ in range(9)]

# --- Convert images to base64 after rotating ---
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

img_html_blocks = []
for path, angle in zip(layout, rotations):
    img = Image.open(path).rotate(angle, expand=True)
    img = img.resize((160, 160))  # Ensure all tiles are same size
    img_b64 = image_to_base64(img)
    html_img = f'<img src="data:image/png;base64,{img_b64}" style="width:160px;height:160px;margin:0;padding:0;display:block;" />'
    img_html_blocks.append(html_img)

# --- Arrange images in a 3x3 CSS Grid ---
grid_html = f"""
<div style="
    display: grid;
    grid-template-columns: repeat(3, 160px);
    grid-template-rows: repeat(3, 160px);
    gap: 0;
    padding: 0;
    margin: 0;
">
    {''.join(f'<div>{img}</div>' for img in img_html_blocks)}
</div>
"""

st.markdown("Random Setup for 36 by Néstor Romeral Andrés)")
st.markdown(grid_html, unsafe_allow_html=True)

# --- Shuffle button ---
if st.button("🔁 Shuffle Layout"):
    st.experimental_rerun()
