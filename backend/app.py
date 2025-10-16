from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from data_handler import load_disease_data, find_precautions
from gemini_service import generate_conversational_response, extract_disease_name, generate_general_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message', '').strip()
        
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        # Use Gemini to extract disease name from user input
        disease_name = extract_disease_name(user_input)
        
        if disease_name:
            # Specific disease found: Get precautions and generate response
            precautions = find_precautions(disease_name)
            if not precautions:
                return jsonify({'response': f'I found info on {disease_name}, but no specific precautions available right now. Please consult a doctor for personalized advice.'}), 200
            
            response = generate_conversational_response(disease_name, precautions, user_input)
            return jsonify({'response': response})
        else:
            # No specific disease: Generate general response based on query
            response = generate_general_response(user_input)
            return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Backend is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)