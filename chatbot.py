def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! Upload your skin image to get started."
    elif "malignant" in user_input:
        return "A malignant result may indicate skin cancer. Please consult a dermatologist."
    elif "benign" in user_input:
        return "A benign result indicates no skin cancer. Still, keep monitoring changes."
    elif "how to prevent" in user_input:
        return "Avoid prolonged sun exposure, use sunscreen, and get regular skin checkups."
    else:
        return "I'm here to guide you on skin cancer detection. Ask me anything related!"