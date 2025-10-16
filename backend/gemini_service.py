import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# List of known diseases from the dataset (for grounding Gemini)
KNOWN_DISEASES = [
    'Drug Reaction', 'Malaria', 'Allergy', 'Hypothyroidism', 'Psoriasis', 'GERD',
    'Chronic cholestasis', 'hepatitis A', 'Osteoarthristis', '(vertigo) Paroymsal  Positional Vertigo',
    'Hypoglycemia', 'Acne', 'Diabetes', 'Impetigo', 'Hypertension', 'Peptic ulcer diseae',
    'Dimorphic hemmorhoids(piles)', 'Common Cold', 'Chicken pox', 'Cervical spondylosis',
    'Hyperthyroidism', 'Urinary tract infection', 'Varicose veins', 'AIDS', 'Paralysis (brain hemorrhage)',
    'Typhoid', 'Hepatitis B', 'Fungal infection', 'Hepatitis C', 'Migraine', 'Bronchial Asthma',
    'Alcoholic hepatitis', 'Jaundice', 'Hepatitis E', 'Dengue', 'Hepatitis D', 'Heart attack',
    'Pneumonia', 'Arthritis', 'Gastroenteritis', 'Tuberculosis'
]

def extract_disease_name(user_input):
    """Use Gemini to extract a disease name from user input, grounded in known diseases."""
    diseases_list = ', '.join(KNOWN_DISEASES)
    prompt = f"""
    You are a medical entity extractor. Analyze the user's message: "{user_input}"
    
    Identify the most likely disease name mentioned or implied (e.g., from symptoms like 'fever and chills' → 'Malaria').
    Respond ONLY with the exact disease name from this list if confidence is high (80%+): {diseases_list}
    If no clear match, respond with 'NONE'.
    Do not add explanations or extra text—just the disease name or 'NONE'.
    """
    
    response = model.generate_content(prompt)
    extracted = response.text.strip().upper()
    
    # Map to exact dataset names (handle variations)
    if extracted == 'NONE':
        return None
    
    # Simple mapping for common variations (e.g., 'DIABETES' → 'Diabetes')
    for disease in KNOWN_DISEASES:
        if extracted.lower() in disease.lower() or disease.lower() in extracted.lower():
            return disease.strip()  # Return exact dataset name
    
    return None  # Fallback if no match

def generate_conversational_response(disease_name, precautions, user_input):
    """Generate a conversational response using Gemini API based on disease, precautions, and original user input."""
    prompt = f"""
    You are a helpful health advisor. The user said: "{user_input}"
    They have {disease_name}. Key precautions: {precautions}.
    
    Respond in a friendly, empathetic, conversational way. Acknowledge their input, expand slightly on 1-2 precautions with simple tips, but keep concise (under 100 words).
    Always end with: "Remember, this isn't medical advice—consult a doctor for your situation."
    Optional: Suggest one related lifestyle change if it fits naturally.
    """
    
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_general_response(user_input):
    """Generate a general health response for queries without a specific disease match."""
    diseases_list = ', '.join(KNOWN_DISEASES)
    prompt = f"""
    You are a helpful health advisor. The user asked: "{user_input}"
    
    Provide a friendly, empathetic response tailored to their query (e.g., if about symptoms like fever, explain how to check/measure it accurately, common signs, and basic self-care).
    If relevant, suggest 1-2 possible diseases from this list that might match: {diseases_list}, and briefly mention related precautions (e.g., for fever: "It could be a common cold—stay hydrated").
    Keep it concise (under 120 words), general, and safe—focus on when to seek help.
    Always end with: "This isn't medical advice—please consult a doctor for personalized guidance."
    Do not diagnose or prescribe.
    """
    
    response = model.generate_content(prompt)
    return response.text.strip()