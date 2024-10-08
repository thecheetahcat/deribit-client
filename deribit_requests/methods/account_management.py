import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import (
    Currency,
    Instrument,
    MarginModel,
    Mode
)
from typing import Optional, List, Dict, Any


def public_get_announcements(start_timestamp: Optional[int] = None, count: Optional[int] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_announcements"""
    return mg.generate_message("public/get_announcements", mg.clean_params({"start_timestamp": start_timestamp, "count": count}))


def public_get_portfolio_margins(currency: Currency, simulated_positions: Optional[Dict] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_portfolio_margins"""
    return mg.generate_message("public/get_portfolio_margins", mg.clean_params({
        "currency": currency.value,
        "simulated_positions": simulated_positions
    }))


def private_change_api_key_name(id_: int, name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-change_api_key_name"""
    return mg.generate_message("private/change_api_key_name", {"id": id_, "name": name})


def private_change_margin_model(margin_model: MarginModel, user_id: Optional[int] = None, dry_run: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-change_margin_model"""
    return mg.generate_message("private/change_margin_model", mg.clean_params({
        "margin_model": margin_model.value,
        "user_id": user_id,
        "dry_run": dry_run
    }))


def private_change_scope_in_api_key(max_scope: str, id_: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-change_scope_in_api_key"""
    return mg.generate_message("private/change_scope_in_api-key", {"max_scope": max_scope, "id": id_})


def private_change_subaccount_name(sid: int, name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-change_subaccount_name"""
    return mg.generate_message("private/change_subaccount_name", {"sid": sid, "name": name})


def private_create_api_key(
        max_scope: str,
        name: Optional[str] = None,
        public_key: Optional[str] = None,
        enabled_features: Optional[List[str]] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-create_api_key"""
    return mg.generate_message("private/create_api_key", mg.clean_params({
        "max_scope": max_scope,
        "name": name,
        "public_key": public_key,
        "enabled_features": enabled_features
    }))


def private_create_subaccount() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-create_subaccount"""
    return mg.generate_message("private/create_subaccount")


def private_disable_api_key(id_: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-disable_api_key"""
    return mg.generate_message("private/disable_api_key", {"id": id_})


def private_edit_api_key(
        id_: int,
        max_scope: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        enabled_features: Optional[List[str]] = None,
        ip_whitelist: Optional[List[str]] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-edit_api_key"""
    return mg.generate_message("private/edit_api_key", mg.clean_params({
        "id": id_,
        "max_scope": max_scope,
        "name": name,
        "enabled": enabled,
        "enabled_features": enabled_features,
        "ip_whitelist": ip_whitelist
    }))


def private_enable_affiliate_program() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-enable_affiliate_program"""
    return mg.generate_message("private/enable_affiliate_program")


def private_enable_api_key(id_: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-enable_api_key"""
    return mg.generate_message("private/enable_api_key", {"id": id_})


def private_get_access_log(offset: Optional[int] = None, count: Optional[int] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_access_log"""
    return mg.generate_message("private/get_access_log", mg.clean_params({"offset": offset, "count": count}))


def private_get_account_summaries(subaccount_id: Optional[int] = None, extended: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_account_summaries"""
    return mg.generate_message("private/get_account_summaries", mg.clean_params({"subaccount_id": subaccount_id, "extended": extended}))


def private_get_account_summary(
        currency: Currency,
        subaccount_id: Optional[int] = None,
        extended: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_account_summary"""
    return mg.generate_message("private/get_account_summary", mg.clean_params({
        "currency": currency.value,
        "subaccount_id": subaccount_id,
        "extended": extended
    }))


def private_get_affiliate_program_info() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_affiliate_program_info"""
    return mg.generate_message("private/get_affiliate_program_info")


def private_get_email_language() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_email_language"""
    return mg.generate_message("private/get_email_language")


def private_get_new_announcements() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_new_announcements"""
    return mg.generate_message("private/get_new_announcements")


def private_get_portfolio_margins(
        currency: Currency,
        add_positions: Optional[bool] = None,
        simulated_positions: Optional[Dict] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_portfolio_margins"""
    return mg.generate_message("private/get_portfolio_margins", mg.clean_params({
        "currency": currency.value,
        "add_positions": add_positions,
        "simulated_positions": simulated_positions
    }))


def private_get_position(instrument_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_position"""
    return mg.generate_message("private/get_position", {"instrument_name": instrument_name})


def private_get_positions(
        currency: Optional[Currency] = None,
        kind: Optional[Instrument] = None,
        subaccount_id: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_positions"""
    return mg.generate_message("private/get_positions", mg.clean_params({
        "currency": None if not currency else currency.value,
        "kind": None if not kind else kind.value,
        "subaccount_id": subaccount_id,
    }))


def private_get_subaccounts(with_portfolio: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_subaccounts"""
    return mg.generate_message("private/get_subaccounts", mg.clean_params({"with_portfolio": with_portfolio}))


def private_get_subaccounts_details(currency: Currency, with_open_orders: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_subaccounts_details"""
    return mg.generate_message("private/get_subaccounts_details", mg.clean_params({
        "currency": currency.value,
        "with_open_orders": with_open_orders
    }))


def private_get_transaction_log(
        currency: Currency,
        start_timestamp: int,
        end_timestamp: int,
        query: Optional[str] = None,
        count: Optional[int] = None,
        continuation_token: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_transaction_log"""
    return mg.generate_message("private/get_transaction_log", mg.clean_params({
        "currency": currency.value,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "query": query,
        "count": count,
        "continuation_token": continuation_token
    }))


def private_get_user_locks() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_locks"""
    return mg.generate_message("private/get_user_locks")


def private_list_api_keys() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-list_api_keys"""
    return mg.generate_message("private/list_api_keys")


def private_list_custody_accounts(currency: Currency) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-list_custody_accounts"""
    return mg.generate_message("private/list_custody_accounts", {"currency": currency.value})


def private_pme_simulate(currency: Currency) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-pme-simulate"""
    return mg.generate_message("private/pme/simulate", {"currency": currency.value})


def private_remove_api_key(id_: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-remove_api_key"""
    return mg.generate_message("private/remove_api_key", {"id": id_})


def private_remove_subaccount(subaccount_id: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-remove_subaccount"""
    return mg.generate_message("private/remove_subaccount", {"subaccount_id": subaccount_id})


def private_reset_api_key(id_: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-reset_api_key"""
    return mg.generate_message("private/reset_api_key", {"id": id_})


def private_set_announcement_as_read(announcement_id: float) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_announcement_as_read"""
    return mg.generate_message("private/set_announcement_as_read", {"announcement_id": announcement_id})


def private_set_disabled_trading_products(user_id: int, trading_products: List[str]) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_disabled_trading_products"""
    return mg.generate_message("private/set_disabled_trading_products", {"user_id": user_id, "trading_products": trading_products})


def private_set_email_for_subaccount(sid: int, email: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_email_for_subaccount"""
    return mg.generate_message("private/set_email_for_subaccount", {"sid": sid, "email": email})


def private_set_email_language(language: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_email_language"""
    return mg.generate_message("private/set_email_language", {"language": language})


def private_set_self_trading_config(mode: Mode, extended_to_subaccounts: bool) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_self_trading_config"""
    return mg.generate_message("private/set_self_trading_config", {
        "mode": mode.value,
        "extended_to_subaccounts": extended_to_subaccounts
    })


def private_simulate_portfolio(
        currency: Currency,
        add_positions: Optional[bool] = None,
        simulated_positions: Optional[Dict] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-simulate_portfolio"""
    return mg.generate_message("private/simulate_portfolio", mg.clean_params({
        "currency": currency.value,
        "add_positions": add_positions,
        "simulated_positions": simulated_positions
    }))


def private_toggle_notifications_from_subaccount(sid: int, state: bool) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-toggle_notifications_from_subaccount"""
    return mg.generate_message("private/toggle_notifications_from_subaccount", {"sid": sid, "state": state})


def private_toggle_portfolio_margining(
        enabled: bool,
        user_id: Optional[int] = None,
        dry_run: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-toggle_portfolio_margining"""
    return mg.generate_message("private/toggle_portfolio_margining", mg.clean_params({
        "enabled": enabled,
        "user_id": user_id,
        "dry_run": dry_run
    }))


def private_toggle_subaccount_login(sid: int, state: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-toggle_subaccount_login"""
    return mg.generate_message("private/toggle_subaccount_login", {"sid": sid, "state": state})
