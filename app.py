import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import re
import json

# Load environment variables
load_dotenv()

# Set up the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-1.5-pro')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get symptoms from the request
    symptoms = request.json.get('symptoms', '')
    
    if not symptoms:
        return jsonify({
            'disease': 'No symptoms provided',
            'description': 'Please provide symptoms for diagnosis.',
            'medications': [],
            'tips': 'N/A'
        }), 400
    
    # Prompt for the Gemini model
    prompt = f"""
    You are a medical assistant providing information about common ailments and over-the-counter medications.
    
    Based on these symptoms: "{symptoms}"
    
    Provide the following information:
    1. Most likely common condition (only provide information about non-serious conditions that can be treated with OTC medications)
    2. Brief description of the condition
    3. Recommended over-the-counter medications and treatments (provide as a list of specific medication names)
    4. Tips or advice for managing the condition at home
    
    If the symptoms suggest a potentially serious condition that requires professional medical attention, 
    state that a doctor should be consulted and do not provide specific diagnosis or treatment recommendations.
    
    Format your response as a JSON object with these keys:
    - "disease": string with condition name
    - "description": string with condition description
    - "medications": array of strings, each with a specific medication name
    - "tips": string with home care advice
    """
    
    try:
        # Generate response from Gemini
        response = model.generate_content(prompt)
        result = response.text
        
        # Try to parse the response as JSON
        try:
            # The model might wrap the JSON in code blocks
            json_match = re.search(r'```(?:json)?\s*({[\s\S]*?})\s*```', result)
            if json_match:
                result = json_match.group(1)
            
            data = json.loads(result)
            
            # Ensure all required fields are present
            required_fields = ['disease', 'description', 'medications', 'tips']
            for field in required_fields:
                if field not in data:
                    if field == 'medications':
                        data[field] = []
                    else:
                        data[field] = f"No {field} information provided"
            
            # Ensure medications is always a list
            if not isinstance(data['medications'], list):
                if data['medications']:
                    # Convert string to list if it's not already
                    data['medications'] = [data['medications']]
                else:
                    data['medications'] = []
            
            return jsonify(data)
            
        except json.JSONDecodeError:
            # If parsing fails, attempt to extract structured data
            disease_match = re.search(r'disease"?\s*:?\s*"?([^"]+)"?', result, re.IGNORECASE)
            desc_match = re.search(r'description"?\s*:?\s*"?([^"]+)"?', result, re.IGNORECASE)
            
            # Format a fallback response
            return jsonify({
                'disease': disease_match.group(1) if disease_match else 'Processing Error',
                'description': desc_match.group(1) if desc_match else 'Could not parse the AI response. Please try again with more specific symptoms.',
                'medications': [],
                'tips': 'Please consult a healthcare professional.'
            }), 500
    
    except Exception as e:
        # Handle API errors
        return jsonify({
            'disease': 'Service Error',
            'description': f'An error occurred: {str(e)}',
            'medications': [],
            'tips': 'Please try again later.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)