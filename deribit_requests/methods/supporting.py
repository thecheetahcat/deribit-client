import deribit_requests.helpers.message_generator as mg
from typing import Optional, Dict, Any


def public_get_time() -> Dict[str, Any]:
    """https://docs.deribit.com/#supporting"""
    return mg.generate_message("public/get_time")


def public_hello(client_name: str, client_version: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-hello"""
    return mg.generate_message("public/hello", {"client_name": client_name, "client_version": client_version})


def public_status() -> Dict[str, Any]:
    """https://docs.deribit.com/#public-status"""
    return mg.generate_message("public/status")


def public_test(expected_result: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-test"""
    return mg.generate_message("public/test", mg.clean_params({"expected_result": expected_result}))
