"""
Validates data received by the module.
"""

allowed_data = [dict, list]

def data_validation(data):
    """Validates the incoming JSON data

    Args:
        data ([JSON Object]): [This is the request body in json format]

    Returns:
        [str, str]: [data, error]
    """
    # check data format
    if not type(data) in allowed_data:
        return None, 'Invalid input data.'
    return data, None
