import deribit_requests.helpers.message_generator as mg
from typing import Optional, List, Dict, Any


def public_subscribe(channels: List[str]) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-subscribe"""
    return mg.generate_message("public/subscribe", {"channels": channels})


def public_unsubscribe(channels: List[str]) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-unsubscribe"""
    return mg.generate_message("public/unsubscribe", {"channels": channels})


def public_unsubscribe_all() -> Dict[str, Any]:
    """https://docs.deribit.com/#public-unsubscribe_all"""
    return mg.generate_message("public/unsubscribe_all")


def private_subscribe(channels: List[str], label: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-subscribe"""
    return mg.generate_message("private/subscribe", mg.clean_params({"channels": channels, "label": label}))


def private_unsubscribe(channels: List[str]) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-unsubscribe"""
    return mg.generate_message("private/unsubscribe", {"channels": channels})


def private_unsubscribe_all() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-unsubscribe_all"""
    return mg.generate_message("private/unsubscribe_all")
