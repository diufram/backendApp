from flask import Blueprint, request, jsonify, send_file
from .utils.text_to_audio import text_to_audio
#from .utils.dialogflow_utils import process_dialogflow
#from .utils.image_classifier import classify_image

main_bp = Blueprint('main', __name__)

@main_bp.route('/text', methods=['POST'])
def text():
    data = request.get_json()
    text = data.get('text')
    if text:
        audio_file = text_to_audio(text)
        return send_file(audio_file, as_attachment=True)
    else:
        return jsonify({"error": "Text not provided"}), 400


@main_bp.route('/audio', methods=['POST'])
def audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file found'}), 400

    file = request.files['audio']
    
    # Guardar el archivo en el servidor
    file.save(f"./uploaded_audio/{file.filename}")
    
    return jsonify({'message': 'Audio uploaded successfully'}), 200

    


""" @main_bp.route('/dialogflow', methods=['POST'])
def handle_dialogflow():
    data = request.get_json()
    text = data.get('text')
    if text:
        response_text = process_dialogflow(text)
        return jsonify({"response": response_text}), 200
    else:
        return jsonify({"error": "Text not provided"}), 400

@main_bp.route('/classify-image', methods=['POST'])
def classify_image_route():
    file = request.files['image']
    if file:
        image_path = file.filename
        file.save(image_path)
        result = classify_image(image_path)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Image not provided"}), 400
 """