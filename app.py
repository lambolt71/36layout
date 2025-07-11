import streamlit as st
import random
from PIL import Image
import base64
from io import BytesIO

# Load and rotate images randomly
tiles = list(range(1, 10))
random.shuffle(tiles)
tile_images = []
for i in tiles:
    img = Image.open(f"tiles/t{i}.png")
    img = img.rotate(90 * random.randint(0, 3), expand=True)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    encoded = base64.b64encode(buffered.getvalue()).decode()
    tile_images.append(f'<img src="data:image/png;base64,{encoded}" width="100" style="margin:0;padding:0;border:0;">')

# Create 3x3 HTML table with no gaps
html_grid = """
<style>
table {
    border-spacing: 0;
    border-collapse: collapse;
}
td {
    padding: 0;
}
</style>
<table>
"""
for i in range(3):
    html_grid += "<tr>"
    for j in range(3):
        html_grid += f"<td>{tile_images[i * 3 + j]}</td>"
    html_grid += "</tr>"
html_grid += "</table>"

# Render
st.markdown(html_grid, unsafe_allow_html=True)

# Button to reshuffle
if st.button("🔄 Reshuffle Layout"):
    st.experimental_rerun()
