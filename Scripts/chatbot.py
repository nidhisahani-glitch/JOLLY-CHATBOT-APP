import joblib
import pandas as pd
import numpy as np
import re

# Load the model globally
jolly = joblib.load('jolly.model')

def preprocess_input(text):
    """Preprocess the user input."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text

def chatbot(input_text, intents):
    """Generate a chatbot response."""
    input_text = preprocess_input(input_text)
    try:
        # Predict the intent tag
        tag = jolly.predict([input_text])[0]
        
        # Find the corresponding intent
        for intent in intents:
            if intent['tag'] == tag:
                response = np.random.choice(intent['responses'])
                return response

        # Default response if no intent matches
        return "I'm sorry, I didn't quite understand that. Can you try rephrasing?"
    except Exception as e:
        return f"An error occurred: {str(e)}"
