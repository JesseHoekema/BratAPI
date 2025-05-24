from flask import Flask, request, send_file, abort, render_template
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('generate.html')

@app.route('/generate', methods=['GET'])
def generate_image():
    text = request.args.get('text', 'Default Text')
    try:
        image = create_image(text)
        return send_file(image, mimetype='image/png')
    except Exception as e:
        return {'error': str(e)}, 500

def create_image(text):
    # Create image with background
    img = Image.new('RGB', (500, 500), color='#8ACF00')
    draw = ImageDraw.Draw(img)

    # Font path setup
    font_path = os.path.join(os.path.dirname(__file__), 'path_to_font.ttf')
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found at {font_path}")

    # Load font
    font = ImageFont.truetype(font_path, size=70)

    # Center text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (500 - text_width) // 2
    y = (500 - text_height) // 2

    # Draw text
    draw.text((x, y), text, fill='black', font=font)

    # Optional: blur the entire image
    img = img.filter(ImageFilter.GaussianBlur(radius=2.1))

    # Convert to BytesIO
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

# For local development
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7856)))

# For Vercel
app.debug = True
