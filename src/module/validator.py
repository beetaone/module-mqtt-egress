from typing import Union
from logging import getLogger

log = getLogger("validator")

def data_validation(data: any) -> Union[str, None]:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """
    log.debug("Validating...")
    try:
        allowed_data_types = (dict, list)
        if not isinstance(data, allowed_data_types):
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"
    except Exception as e:
        log.error("Error in validation: " + str(e))
        return f"Error when validating module input data: {e}"
    return None
