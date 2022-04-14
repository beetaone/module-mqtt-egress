"""
All logic related to the module's main application
Mostly only this file requires changes
"""

from app.config import APPLICATION

def module_main(data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        return data, None
    except Exception:
        return None, "Unable to perform the module logic"
