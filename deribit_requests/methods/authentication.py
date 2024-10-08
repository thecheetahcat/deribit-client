import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import CLIENT_ID, CLIENT_SECRET
from typing import Optional, Dict, Any


def public_auth_credentials(state: Optional[str] = None, scope: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-auth"""
    return mg.generate_message("public/auth", mg.clean_params({
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "state": state,
        "scope": scope
    }))


def public_auth_client_signature(
        timestamp: int,
        signature: str,
        nonce: Optional[str] = None,
        data: Optional[str] = None,
        state: Optional[str] = None,
        scope: Optional[str] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-auth"""
    return mg.generate_message("public/auth", mg.clean_params({
        "grant_type": "client_signature",
        "client_id": CLIENT_ID,
        "timestamp": timestamp,
        "signature": signature,
        "nonce": nonce,
        "data": data,
        "state": state,
        "scope": scope
    }))


def public_auth_refresh_token(refresh_token: str, state: Optional[str] = None, scope: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-auth"""
    return mg.generate_message("public/auth", mg.clean_params({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "state": state,
        "scope": scope
    }))


def public_exchange_token(refresh_token: str, subject_id: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-exchange_token"""
    return mg.generate_message("public/exchange_token", {"refresh_token": refresh_token, "subject_id": subject_id})


def public_fork_token(refresh_token: str, session_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-fork_token"""
    return mg.generate_message("public/fork_token", {"refresh_token": refresh_token, "session_name": session_name})


def private_logout(access_token: str, invalidate_token: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-logout"""
    return mg.generate_message("/private/logout", mg.clean_params({"access_token": access_token, "invalidate_token": invalidate_token}))
