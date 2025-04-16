def format_data(data):
    # Format the data for display or transmission
    return str(data).strip()

def log_message(message):
    # Log a message to the console or a file
    print(f"LOG: {message}")

def validate_input(input_value, expected_type):
    # Validate the input against the expected type
    return isinstance(input_value, expected_type)