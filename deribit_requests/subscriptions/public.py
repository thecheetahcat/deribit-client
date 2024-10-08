import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import (
    Currency,
    Instrument,
    IndexName,
    DepthLevel,
    Resolution,
    Group,
    BookInterval
)


def book_instrument_name_group_depth_interval(instrument_name: str, group: Group, depth: DepthLevel, interval: BookInterval) -> str:
    """https://docs.deribit.com/#book-instrument_name-group-depth-interval"""
    return mg.create_subscription_channel("book", {
        "instrument_name": instrument_name,
        "group": group.value,
        "depth": depth.value,
        "interval": interval.value
    })


def rfq_currency(currency: Currency) -> str:
    """https://docs.deribit.com/#rfq-currency"""
    return mg.create_subscription_channel("rfq", {"currency": currency.value})


def announcements() -> str:
    """https://docs.deribit.com/#announcements"""
    return mg.create_subscription_channel("announcements")


def deribit_price_index_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#deribit_price_index-index_name"""
    return mg.create_subscription_channel("deribit_price_index", {"index_name": index_name.value})


def deribit_price_ranking_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#deribit_price_ranking-index_name"""
    return mg.create_subscription_channel("deribit_price_ranking", {"index_name": index_name.value})


def block_trade_confirmation() -> str:
    """https://docs.deribit.com/#block_trade_confirmations"""
    return mg.create_subscription_channel("block_trade_confirmations")


def ticker_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#ticker-instrument_name-interval"""
    return mg.create_subscription_channel("ticker", {"instrument_name": instrument_name, "interval": interval.value})


def quote_instrument_name(instrument_name: str) -> str:
    """https://docs.deribit.com/#quote-instrument_name"""
    return mg.create_subscription_channel("quote", {"instrument_name": instrument_name})


def perpetual_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#perpetual-instrument_name-interval"""
    return mg.create_subscription_channel("perpetual", {"instrument_name": instrument_name, "interval": interval.value})


def trades_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#trades-instrument_name-interval"""
    return mg.create_subscription_channel("trades", {"instrument_name": instrument_name, "interval": interval.value})


def platform_state_public_methods_state():
    """https://docs.deribit.com/#platform_state-public_methods_state"""
    return mg.create_subscription_channel("platform_state.public_methods_state")


def trades_kind_currency_interval(kind: Instrument, currency: Currency, interval: BookInterval) -> str:
    """https://docs.deribit.com/#trades-kind-currency-interval"""
    return mg.create_subscription_channel("trades", {
        "kind": kind.value,
        "currency": currency.value,
        "interval": interval.value
    })


def mark_price_options_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#markprice-options-index_name"""
    return mg.create_subscription_channel("markprice.options", {"index_name": index_name.value})


def deribit_volatility_index_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#deribit_volatility_index-index_name"""
    return mg.create_subscription_channel("deribit_volatility_index", {"index_name": index_name.value})


def deribit_price_statistics_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#deribit_price_statistics-index_name"""
    return mg.create_subscription_channel("deribit_price_statistics", {"index_name": index_name.value})


def platform_state() -> str:
    """https://docs.deribit.com/#platform_state"""
    return mg.create_subscription_channel("platform_state")


def instrument_state_kind_currency(kind: Instrument, currency: Currency) -> str:
    """https://docs.deribit.com/#instrument-state-kind-currency"""
    return mg.create_subscription_channel("instrument.state", {"kind": kind.value, "currency": currency.value})


def chart_trades_instrument_name_resolution(instrument_name: str, resolution: Resolution) -> str:
    """https://docs.deribit.com/#user-orders-kind-currency-interval"""
    return mg.create_subscription_channel("chart.trades", {"instrument_name": instrument_name, "resolution": resolution.value})


def estimated_expiration_price_index_name(index_name: IndexName) -> str:
    """https://docs.deribit.com/#estimated_expiration_price-index_name"""
    return mg.create_subscription_channel("estimated_expiration_price", {"index_name": index_name.value})


def book_instrument_name_interval(instrument_name: str, interval: BookInterval) -> str:
    """https://docs.deribit.com/#book-instrument_name-interval"""
    return mg.create_subscription_channel("book", {"instrument_name": instrument_name, "interval": interval.value})


def incremental_ticker_instrument_name(instrument_name: str) -> str:
    """https://docs.deribit.com/#incremental_ticker-instrument_name"""
    return mg.create_subscription_channel("incremental_ticker", {"instrument_name": instrument_name})
