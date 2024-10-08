import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import (
    Currency,
    Instrument,
    IndexName,
    BookInterval
)


def user_access_log() -> str:
    """https://docs.deribit.com/#user-access_log"""
    return mg.create_subscription_channel("user.access_log")


def user_mmp_trigger_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#user-mmp_trigger-index_name"""
    return mg.create_subscription_channel("user.mmp_trigger", {"index_name": index_name.value})


def user_changes_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-changes-instrument_name-interval"""
    return mg.create_subscription_channel("user.changes", {"instrument_name": instrument_name, "interval": interval.value})


def user_combo_trades_kind_currency_interval(kind: Instrument, currency: Currency, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-combo_trades-kind-currency-interval"""
    return mg.create_subscription_channel("user.combo_trades", {
        "kind": kind.value,
        "currency": currency.value,
        "interval": interval.value
    })


def user_orders_kind_currency_raw(kind: Instrument, currency: Currency) -> str:
    """https://docs.deribit.com/#user-orders-kind-currency-raw"""
    return mg.create_subscription_channel("user.orders", {"kind": kind.value, "currency": currency.value, "raw": "raw"})


def user_combo_trades_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-combo_trades-instrument_name-interval"""
    return mg.create_subscription_channel("user.combo_trades", {"instrument_name": instrument_name, "interval": interval.value})


def user_lock() -> str:
    """https://docs.deribit.com/#user-lock"""
    return mg.create_subscription_channel("user.lock")


def user_portfolio_currency(currency: Currency) -> str:
    """https://docs.deribit.com/#user-portfolio-currency"""
    return mg.create_subscription_channel("user.portfolio", {"currency": currency.value})


def user_changes_kind_currency_interval(kind: Instrument, currency: Currency, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-changes-kind-currency-interval"""
    return mg.create_subscription_channel("user.changes", {
        "kind": kind.value,
        "currency": currency.value,
        "interval": interval.value
    })


def user_orders_instrument_name_raw(instrument_name: str) -> str:
    """https://docs.deribit.com/#user-orders-instrument_name-raw"""
    return mg.create_subscription_channel("user.orders", {"instrument_name": instrument_name, "raw": "raw"})


def user_trades_kind_currency_interval(kind: Instrument, currency: Currency, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-trades-kind-currency-interval"""
    return mg.create_subscription_channel("user.trades", {
        "kind": kind.value,
        "currency": currency.value,
        "interval": interval.value
    })


def user_orders_kind_currency_interval(kind: Instrument, currency: Currency, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-orders-kind-currency-interval"""
    return mg.create_subscription_channel("user.orders", {
        "kind": kind.value,
        "currency": currency.value,
        "interval": interval.value
    })


def user_orders_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#chart-trades-instrument_name-resolution"""
    return mg.create_subscription_channel("user.orders", {"instrument_name": instrument_name, "interval": interval.value})


def user_trades_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#user-trades-instrument_name-interval"""
    return mg.create_subscription_channel("user.trades", {"instrument_name": instrument_name, "interval": interval.value})
