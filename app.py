from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from enhancement import process_all

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🟢 Landing Page
@app.route('/')
def home():
    return render_template('home.html')

# 🔵 Main App Page
@app.route('/app')
def index():
    return render_template('index.html')

# 🔥 IMPORTANT: Serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ⚡ Upload + Process
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Process images
        process_all(filepath, UPLOAD_FOLDER)

        # 🔥 Return correct URLs (IMPORTANT FIX)
        return jsonify({
            "original": "/uploads/original.jpg",
            "clahe": "/uploads/clahe.jpg",
            "gamma": "/uploads/gamma.jpg",
            "face": "/uploads/face.jpg"
        })

if __name__ == '__main__':
    app.run(debug=True)