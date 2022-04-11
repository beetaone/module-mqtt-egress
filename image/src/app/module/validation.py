"""
Validates data received by the module.
"""
from app.config import APPLICATION

allowed_data = [dict, list]

def data_validation(data):
    """Validates the incoming JSON data

    Args:
        data ([JSON Object]): [This is the request body in json format]

    Returns:
        [str, str]: [data, error]
    """
    try:
        # check data format
        if not type(data) in allowed_data:
            return None, 'Invalid Input data'
        return data, None
    except Exception:
        return None, 'Invalid INPUT_LABEL'
