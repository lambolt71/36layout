import streamlit as st
from PIL import Image
import random
import base64
from io import BytesIO
import os

# --- Settings ---
TILE_FOLDER = "tiles"
TILE_FILENAMES = [f"t{i}.png" for i in range(1, 10)]
ROTATIONS = [0, 90, 180, 270]

# --- Shuffle on first load or button press ---
if "layout" not in st.session_state or st.button("🔄 Reshuffle Layout"):
    st.session_state.layout = random.sample(TILE_FILENAMES, 9)
    st.session_state.rotations = [random.choice(ROTATIONS) for _ in range(9)]

# --- Helper to convert image to base64 ---
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- Build the HTML table ---
html = "<table cellspacing='0' cellpadding='0' style='border-collapse: collapse;'>"

for row in range(3):
    html += "<tr>"
    for col in range(3):
        index = row * 3 + col
        filename = st.session_state.layout[index]
        rotation = st.session_state.rotations[index]

        img_path = os.path.join(TILE_FOLDER, filename)
        img = Image.open(img_path).rotate(rotation, expand=True)
        img = img.resize((128, 128))  # size in pixels

        img_b64 = image_to_base64(img)
        html += f"<td><img src='data:image/png;base64,{img_b64}' width='128' height='128'></td>"
    html += "</tr>"

html += "</table>"

# --- Display the result ---
st.markdown(html, unsafe_allow_html=True)
