class MissingParameterError(Exception):
    """Custom exception for missing API parameters."""
    def __init__(self, parameter):
        self.message = f"Missing required parameter: {parameter}"
        super().__init__(self.message)

class InvalidParameterError(Exception):
    """Custom exception for invalid API parameters."""
    def __init__(self, parameter, expected_type):
        self.message = f"Invalid value for '{parameter}'. Expected type: {expected_type.__name__}."
        super().__init__(self.message)

def validate_api_request(params):
    """Validates the parameters of an API request."""
    required_params = {"user_id": int, "email": str}
    
    for param, expected_type in required_params.items():
        if param not in params:
            raise MissingParameterError(param)
        if not isinstance(params[param], expected_type):
            raise InvalidParameterError(param, expected_type)
    
    print("API request is valid.")

# Example usage
try:
    request_params = {"user_id": "123", "email": "user@example.com"}  # user_id should be an integer
    validate_api_request(request_params)
except MissingParameterError as e:
    print(f"Custom exception caught: {e}")
except InvalidParameterError as e:
    print(f"Custom exception caught: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
