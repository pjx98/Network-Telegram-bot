def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi"):
        return "Hey! How's it going?"