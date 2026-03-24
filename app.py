from flask import Flask, render_template, request, send_file
import os
from enhancement import enhance_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🟢 PAGE 1 → Landing Page
@app.route('/')
def home():
    return render_template('home.html')

# 🔵 PAGE 2 → Main App
@app.route('/app')
def index():
    return render_template('index.html')

# ⚡ Upload + Enhancement
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        output_path = os.path.join(UPLOAD_FOLDER, "enhanced_" + file.filename)

        enhance_image(filepath, output_path)

        return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)