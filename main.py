from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_image():
    text = request.args.get('text', 'Default Text')
    image = create_image(text)
    return send_file(image, mimetype='image/png')

def create_image(text):
    # Create a new image with a green background
    img = Image.new('RGB', (500, 500), color='#8ACF00')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('path_to_font.ttf', size=150)

    # Calculate text bounding box
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate position to center text
    x = (500 - text_width) // 2
    y = (500 - text_height) // 2

    # Add text to image
    draw.text((x, y), text, fill='black', font=font)

    # Apply a slight blur to the text
    img = img.filter(ImageFilter.GaussianBlur(radius=2.1))

    # Save image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

if __name__ == '__main__':
    app.run(debug=True)
