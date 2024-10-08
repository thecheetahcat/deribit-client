import deribit_requests.helpers.message_generator as mg
from typing import Optional, Dict, Any


def public_set_heartbeat(interval: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-set_heartbeat"""
    return mg.generate_message("public/set_heartbeat", {"interval": interval})


def public_disable_heartbeat() -> Dict[str, Any]:
    """https://docs.deribit.com/#public-disable_heartbeat"""
    return mg.generate_message("public/disable_heartbeat")


def private_enable_cancel_on_disconnect(scope: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-enable_cancel_on_disconnect"""
    return mg.generate_message("private/enable_cancel_on_disconnect", mg.clean_params({"scope": scope}))


def private_disable_cancel_on_disconnect(scope: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-disable_cancel_on_disconnect"""
    return mg.generate_message("private/disable_cancel_on_disconnect", mg.clean_params({"scope": scope}))


def private_get_cancel_on_disconnect(scope: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_cancel_on_disconnect"""
    return mg.generate_message("private/get_cancel_on_disconnect", mg.clean_params({"scope": scope}))
