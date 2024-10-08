from typing import Optional, Dict, Any


def generate_message(method: str, params: Optional[Dict[str, Any]] = None, id_: int = 0) -> Dict[str, Any]:
    """
    Generate the dictionary message for a request.

    :param method: Endpoint of the request
    :param params: Parameters of the request
    :param id_: Optional ID for request
    :return: Dictionary message
    """
    message = {"jsonrpc": "2.0", "method": method, "id": id_, "params": {}}
    if params:
        message["params"] = params
    return message


def create_subscription_channel(subscription_type: str, params: Optional[Dict[str, Any]] = None) -> str:
    if params is None:
        return subscription_type
    return f"{subscription_type}{''.join([f'.{value}' for key, value in params.items()])}"


def clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in params.items() if value is not None}
