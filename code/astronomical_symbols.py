import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# Constants
DPI = 300
INCH = 3
SYMBOL_SIZE = DPI * INCH  # 3 inches at 300 DPI
PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Ceres", "Pluto"]
OUTPUT_FILE = "planet_symbols_grid.png"

# Scrape symbols from Wikipedia page
URL = "https://en.wikipedia.org/wiki/Astronomical_symbol"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# Find image URLs
symbols = {}
for name in PLANETS:
    img_tag = soup.find("img", alt=lambda alt: alt and name in alt)
    if img_tag:
        img_url = "https:" + img_tag["src"]
        symbols[name] = img_url

# Download and resize images
images = []
for name in PLANETS:
    if name in symbols:
        img_response = requests.get(symbols[name])
        img = Image.open(BytesIO(img_response.content)).convert("RGBA")
        img = img.resize((SYMBOL_SIZE, SYMBOL_SIZE), Image.LANCZOS)
        images.append((name, img))
    else:
        print(f"Symbol for {name} not found.")

# Create a blank white canvas (grid: 5 x 2 layout)
cols = 5
rows = 2
canvas_width = cols * SYMBOL_SIZE
canvas_height = rows * SYMBOL_SIZE
canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

# Paste symbols on the canvas
for i, (name, img) in enumerate(images):
    x = (i % cols) * SYMBOL_SIZE
    y = (i // cols) * SYMBOL_SIZE
    canvas.paste(img, (x, y), mask=img)

# Save the final image
canvas.save(OUTPUT_FILE)
print(f"Saved {OUTPUT_FILE}")
