import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import (
    Currency,
    Instrument,
    IndexName,
    SettlementType,
    Sorting,
    DepthLevel,
    IndexType,
    Resolution
)
from typing import Optional, Dict, Any


def public_get_book_summary_by_currency(currency: Currency, kind: Instrument) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_book_summary_by_currency"""
    return mg.generate_message("public/get_book_summary_by_currency", {"currency": currency.value, "kind": kind.value})


def public_get_book_summary_by_instrument(instrument_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_book_summary_by_instrument"""
    return mg.generate_message("public/get_book_summary_by_instrument", {"instrument_name": instrument_name})


def public_get_contract_size(instrument_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_contract_size"""
    return mg.generate_message("public/get_contract_size", {"instrument_name": instrument_name})


def public_get_currencies() -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_currencies"""
    return mg.generate_message("public/get_currencies")


def public_get_delivery_prices(index_name: IndexName, offset: Optional[int] = None, count: Optional[int] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_delivery_prices"""
    return mg.generate_message("public/get_delivery_prices", mg.clean_params({
        "index_name": index_name.value,
        "offset": offset,
        "count": count
    }))


def public_get_funding_chart_data(instrument_name: str, length: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_funding_chart_data"""
    return mg.generate_message("public/get_funding_chart_data", {"instrument_name": instrument_name, "length": length})


def public_get_funding_rate_history(instrument_name: str, start_timestamp: int, end_timestamp: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_funding_rate_history"""
    return mg.generate_message("public/get_funding_rate_history", {
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp
    })


def public_get_funding_rate_value(instrument_name: str, start_timestamp: int, end_timestamp: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_funding_rate_value"""
    return mg.generate_message("public/get_funding_rate_value", {
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp
    })


def public_get_historical_volatility(currency: Currency) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_historical_volatility"""
    return mg.generate_message("public/get_historical_volatility", {"currency": currency.value})


def public_get_index_price(index_name: IndexName) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_index_price"""
    return mg.generate_message("public/get_index_price", {"index_name": index_name.value})


def public_get_index_price_names() -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_index_price_names"""
    return mg.generate_message("public/get_index_price_names")


def public_get_instrument(instrument_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_instrument"""
    return mg.generate_message("public/get_instrument", {"instrument_name": instrument_name})


def public_get_instruments(currency: Currency, kind: Optional[Instrument] = None, expired: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_instruments"""
    return mg.generate_message("public/get_instruments", {
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "expired": False if expired is None else expired
    })


def public_get_last_settlements_by_currency(
        currency: Currency,
        type_: Optional[SettlementType] = None,
        count: Optional[int] = None,
        continuation: Optional[str] = None,
        search_start_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_settlements_by_currency"""
    return mg.generate_message("public/get_last_settlements_by_currency", mg.clean_params({
        "currency": currency.value,
        "type_": None if not type_ else type_.value,
        "count": count,
        "continuation": continuation,
        "search_start_timestamp": search_start_timestamp
    }))


def public_get_last_settlements_by_instrument(
        instrument_name: str,
        type_: Optional[SettlementType] = None,
        count: Optional[int] = None,
        continuation: Optional[str] = None,
        search_start_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_settlements_by_instrument"""
    return mg.generate_message("public/get_last_settlements_by_instrument", mg.clean_params({
        "currency": instrument_name,
        "type_": None if not type_ else type_.value,
        "count": count,
        "continuation": continuation,
        "search_start_timestamp": search_start_timestamp
    }))


def public_get_last_trades_by_currency(
        currency: Currency,
        kind: Optional[Instrument] = None,
        start_id: Optional[str] = None,
        end_id: Optional[str] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_trades_by_currency"""
    return mg.generate_message("public/get_last_trades_by_currency", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "start_id": start_id,
        "end_id": end_id,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def public_get_last_trades_by_currency_and_time(
        currency: Currency,
        kind: Optional[Instrument] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_trades_by_currency_and_time"""
    return mg.generate_message("public/get_last_trades_by_currency_and_time", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def public_get_last_trades_by_instrument(
        instrument_name: str,
        start_seq: Optional[int] = None,
        end_seq: Optional[int] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_trades_by_instrument"""
    return mg.generate_message("public/get_last_trades_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "start_seq": start_seq,
        "end_seq": end_seq,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def public_get_last_trades_by_instrument_and_time(
        instrument_name: str,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_last_trades_by_instrument_and_time"""
    return mg.generate_message("public/get_last_trades_by_instrument_and_time", mg.clean_params({
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def public_get_mark_price_history(instrument_name: str, start_timestamp: int, end_timestamp: int) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_mark_price_history"""
    return mg.generate_message("public/get_mark_price_history", {
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp
    })


def public_get_order_book(instrument_name: str, depth: Optional[DepthLevel] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_order_book"""
    return mg.generate_message("public/get_order_book", mg.clean_params({
        "instrument_name": instrument_name,
        "depth": None if not depth else depth.value
    }))


def public_get_order_book_by_instrument_id(instrument_id: str, depth: Optional[DepthLevel] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_order_book_by_instrument_id"""
    return mg.generate_message("public/get_order_book_by_instrument_id", mg.clean_params({
        "instrument_id": instrument_id,
        "depth": None if not depth else depth.value
    }))


def public_get_rfqs(currency: Currency, kind: Optional[Instrument] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_rfqs"""
    return mg.generate_message("public/get_rfqs", mg.clean_params({"currency": currency.value, "kind": None if not kind else kind.value}))


def public_get_supported_index_names(type_: IndexType) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_supported_index_names"""
    return mg.generate_message("public/get_supported_index_names", {"type": type_.value})


def public_get_trade_volumes(extended: Optional[bool] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_trade_volumes"""
    return mg.generate_message("public/get_trade_volumes", mg.clean_params({"extended": extended}))


def public_get_tradingview_chart_data(instrument_name: str, start_timestamp: int, end_timestamp: int, resolution: Resolution) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_tradingview_chart_data"""
    return mg.generate_message("public/get_tradingview_chart_data", {
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "resolution": resolution.value
    })


def public_get_volatility_index_data(currency: Currency, start_timestamp: int, end_timestamp: int, resolution: Resolution) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-get_volatility_index_data"""
    return mg.generate_message("public/get_volatility_index_data", {
        "currency": currency.value,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "resolution": resolution.value
    })


def public_ticker(instrument_name: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#public-ticker"""
    return mg.generate_message("public/ticker", {"instrument_name": instrument_name})
