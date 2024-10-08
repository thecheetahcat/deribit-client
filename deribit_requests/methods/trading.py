import deribit_requests.helpers.message_generator as mg
from deribit_requests.helpers.constants import (
    Currency,
    Instrument,
    IndexName,
    SettlementType,
    Sorting,
    OrderType,
    TimeInForce,
    TriggerType,
    Advanced,
    LinkedOrderType,
    TriggerFillCondition,
    OrderSide,
    CancelType,
    QuotesRequest
)
from typing import Optional, List, Dict, Any


def private_order(
        side: OrderSide,
        instrument_name: str,
        amount: Optional[float] = None,
        contracts: Optional[float] = None,
        order_type: Optional[OrderType] = None,
        label: Optional[str] = None,
        price: Optional[float] = None,
        time_in_force: Optional[TimeInForce] = None,
        max_show: Optional[float] = None,
        post_only: Optional[bool] = None,
        reject_post_only: Optional[bool] = None,
        reduce_only: Optional[bool] = None,
        trigger_price: Optional[float] = None,
        trigger_offset: Optional[float] = None,
        trigger: Optional[TriggerType] = None,
        advanced: Optional[Advanced] = None,
        mmp: Optional[bool] = None,
        valid_until: Optional[int] = None,
        linked_order_type: Optional[LinkedOrderType] = None,
        trigger_fill_condition: Optional[TriggerFillCondition] = None,
        otoco_config: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    https://docs.deribit.com/#private-buy / https://docs.deribit.com/#private-sell

    Combined /private/buy and /private/sell. They have identical parameters except the method changes.
    """
    return mg.generate_message(f"private/{side.value}", mg.clean_params({
        "instrument_name": instrument_name,
        "amount": amount,
        "contracts": contracts,
        "type": None if not order_type else order_type.value,
        "label": label,
        "price": price,
        "time_in_force": None if not time_in_force else time_in_force.value,
        "max_show": max_show,
        "post_only": post_only,
        "reject_post_only": reject_post_only,
        "reduce_only": reduce_only,
        "trigger_price": trigger_price,
        "trigger_offset": trigger_offset,
        "trigger": None if not trigger else trigger.value,
        "advanced": None if not advanced else advanced.value,
        "mmp": mmp,
        "valid_until": valid_until,
        "linked_order_type": None if not linked_order_type else linked_order_type.value,
        "trigger_fill_condition": None if not trigger_fill_condition else trigger_fill_condition.value,
        "otoco_config": otoco_config,
    }))


def private_edit(
        order_id: Optional[str] = None,
        label: Optional[str] = None,
        amount: Optional[float] = None,
        contracts: Optional[float] = None,
        price: Optional[float] = None,
        post_only: Optional[bool] = None,
        reduce_only: Optional[bool] = None,
        reject_post_only: Optional[bool] = None,
        advanced: Optional[Advanced] = None,
        trigger_price: Optional[float] = None,
        trigger_offset: Optional[float] = None,
        mmp: Optional[bool] = None,
        valid_until: Optional[int] = None,
) -> Dict[str, Any]:
    """
    https://docs.deribit.com/#private-edit / https://docs.deribit.com/#private-edit_by_label

    Combined /private/edit and /private/edit_by_label. They are identical calls except one uses the order ID and one uses the label.
    Make sure to only provide one of order_id and label. If both are provided, this will return an empty dictionary.
    """
    if order_id is not None and label is not None:
        return {}  # only one of these can be provided
    method = "edit" if order_id else "edit_by_label"
    return mg.generate_message(f"private/{method}", mg.clean_params({
        "order_id": order_id,
        "label": label,
        "amount": amount,
        "contracts": contracts,
        "price": price,
        "post_only": post_only,
        "reduce_only": reduce_only,
        "reject_post_only": reject_post_only,
        "advanced": None if not advanced else advanced.value,
        "trigger_price": trigger_price,
        "trigger_offset": trigger_offset,
        "mmp": mmp,
        "valid_until": valid_until,
    }))


def private_cancel(order_id: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel"""
    return mg.generate_message("private/cancel", {"order_id": order_id})


def private_cancel_all() -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_all"""
    return mg.generate_message("private/cancel_all")


def private_cancel_all_by_currency(
        currency: Currency,
        kind: Optional[Instrument] = None,
        order_type: Optional[OrderType] = None,
        detailed: Optional[bool] = None,
        freeze_quotes: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_all_by_currency"""
    return mg.generate_message("private/cancel_all_by_currency", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "order_type": None if not order_type else order_type.value,
        "detailed": detailed,
        "freeze_quotes": freeze_quotes
    }))


def private_cancel_all_by_currency_pair(
        currency_pair: IndexName,
        kind: Optional[Instrument] = None,
        order_type: Optional[OrderType] = None,
        detailed: Optional[bool] = None,
        freeze_quotes: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_all_by_currency_pair"""
    return mg.generate_message("private/cancel_all_by_currency_pair", mg.clean_params({
        "currency_pair": currency_pair.value,
        "kind": None if not kind else kind.value,
        "order_type": None if not order_type else order_type.value,
        "detailed": detailed,
        "freeze_quotes": freeze_quotes
    }))


def private_cancel_all_by_instrument(
        instrument_name: str,
        order_type: Optional[OrderType] = None,
        detailed: Optional[bool] = None,
        include_combos: Optional[bool] = None,
        freeze_quotes: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_all_by_instrument"""
    return mg.generate_message("private/cancel_all_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "order_type": None if not order_type else order_type.value,
        "detailed": detailed,
        "include_combos": include_combos,
        "freeze_quotes": freeze_quotes
    }))


def private_cancel_all_by_kind_or_type(
        currency: Currency,
        kind: Optional[Instrument] = None,
        order_type: Optional[OrderType] = None,
        detailed: Optional[bool] = None,
        freeze_quotes: Optional[bool] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_all_by_kind_or_type"""
    return mg.generate_message("private/cancel_all_by_kind_or_type", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "order_type": None if not order_type else order_type.value,
        "detailed": detailed,
        "freeze_quotes": freeze_quotes
    }))


def private_cancel_by_label(label: str, currency: Optional[Currency] = None,) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_by_label"""
    return mg.generate_message("private/cancel_by_label", mg.clean_params({
        "label": label,
        "currency": None if not currency else currency.value
    }))


def private_cancel_quotes(
        cancel_type: CancelType,
        detailed: Optional[bool] = None,
        freeze_quotes: Optional[bool] = None,
        min_delta: Optional[float] = None,
        max_delta: Optional[float] = None,
        quote_set_id: Optional[str] = None,
        kind: Optional[Instrument] = None,
        currency: Optional[Currency] = None,
        currency_pair: Optional[IndexName] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-cancel_quotes"""
    return mg.generate_message("private/cancel_quotes", mg.clean_params({
        "cancel_type": cancel_type.value,
        "detailed": detailed,
        "freeze_quotes": freeze_quotes,
        "min_delta": min_delta,
        "max_delta": max_delta,
        "quote_set_id": quote_set_id,
        "kind": None if not kind else kind.value,
        "currency": None if not currency else currency.value,
        "currency_pair": None if not currency_pair else currency_pair.value
    }))


def private_close_position(instrument_name: str, order_type: OrderType, price: Optional[float] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-close_position"""
    return mg.generate_message("private/close_position", mg.clean_params({
        "instrument_name": instrument_name,
        "order_type": order_type.value,
        "price": price
    }))


def private_get_margins(instrument_name: str, amount: float, price: float) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_margins"""
    return mg.generate_message("private/get_margins", {"instrument_name": instrument_name, "amount": amount, "price": price})


def private_get_mmp_config(index_name: Optional[IndexName] = None, mmp_group: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_mmp_config"""
    return mg.generate_message("private/get_mmp_config", mg.clean_params({
        "index_name": None if not index_name else index_name.value,
        "mmp_group": mmp_group
    }))


def private_get_open_orders(kind: Optional[Instrument] = None, order_type: Optional[OrderType] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_open_orders"""
    return mg.generate_message("private/get_open_orders", mg.clean_params({
        "kind": None if not kind else kind.value,
        "order_type": None if not order_type else order_type.value
    }))


def private_get_open_orders_by_currency(
        currency: Currency,
        kind: Optional[Instrument] = None,
        order_type: Optional[OrderType] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_open_orders_by_currency"""
    return mg.generate_message("private/get_open_orders_by_currency", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "order_type": None if not order_type else order_type.value
    }))


def private_get_open_orders_by_instrument(instrument_name: str, order_type: Optional[OrderType] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_open_orders_by_instrument"""
    return mg.generate_message("private/get_open_orders_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "order_type": None if not order_type else order_type.value
    }))


def private_get_open_orders_by_label(currency: Currency, label: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_open_orders_by_label"""
    return mg.generate_message("private/get_open_orders_by_label", mg.clean_params({
        "currency": currency.value,
        "label": label
    }))


def private_get_order_history_by_currency(
        currency: Currency,
        kind: Optional[Instrument] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        include_old: Optional[bool] = None,
        include_unfilled: Optional[bool] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_order_history_by_currency"""
    return mg.generate_message("private/get_order_history_by_currency", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "count": count,
        "offset": offset,
        "include_old": include_old,
        "include_unfilled": include_unfilled
    }))


def private_get_order_history_by_instrument(
        instrument_name: str,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        include_old: Optional[bool] = None,
        include_unfilled: Optional[bool] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_order_history_by_instrument"""
    return mg.generate_message("private/get_order_history_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "count": count,
        "offset": offset,
        "include_old": include_old,
        "include_unfilled": include_unfilled
    }))


def private_get_order_margin_by_ids(ids: List[str]) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_order_margin_by_ids"""
    return mg.generate_message("private/get_order_margin_by_ids", {"ids": ids})


def private_get_order_state(order_id: str) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_order_state"""
    return mg.generate_message("private/get_order_state", {"order_id": order_id})


def private_get_order_state_by_label(currency: Currency, label: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_order_state_by_label"""
    return mg.generate_message("private/get_order_state_by_label", mg.clean_params({
        "currency": currency.value,
        "label": label
    }))


def private_get_trigger_order_history(
        currency: Currency,
        instrument_name: Optional[str] = None,
        count: Optional[int] = None,
        continuation_token: Optional[str] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_trigger_order_history"""
    return mg.generate_message("private/get_trigger_order_history", mg.clean_params({
        "currency": currency.value,
        "instrument_name": instrument_name,
        "count": count,
        "continuation_token": continuation_token
    }))


def private_get_user_trades_by_currency(
        currency: Currency,
        kind: Optional[Instrument] = None,
        start_id: Optional[str] = None,
        end_id: Optional[str] = None,
        count: Optional[int] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        sorting: Optional[Sorting] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_trades_by_currency"""
    return mg.generate_message("private/get_user_trades_by_currency", mg.clean_params({
        "currency": currency.value,
        "kind": None if not kind else kind.value,
        "start_id": start_id,
        "end_id": end_id,
        "count": count,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "sorting": None if not sorting else sorting.value
    }))


def private_get_user_trades_by_currency_and_time(
        currency: Currency,
        start_timestamp: int,
        end_timestamp: int,
        kind: Optional[Instrument] = None,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_trades_by_currency_and_time"""
    return mg.generate_message("private/get_user_trades_by_currency_and_time", mg.clean_params({
        "currency": currency.value,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "kind": None if not kind else kind.value,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def private_get_user_trades_by_instrument(
        instrument_name: str,
        start_seq: Optional[int] = None,
        end_seq: Optional[int] = None,
        count: Optional[int] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
        sorting: Optional[Sorting] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_trades_by_instrument"""
    return mg.generate_message("private/get_user_trades_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "start_seq": start_seq,
        "end_seq": end_seq,
        "count": count,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "sorting": None if not sorting else sorting.value
    }))


def private_get_user_trades_by_instrument_and_time(
        instrument_name: str,
        start_timestamp: int,
        end_timestamp: int,
        count: Optional[int] = None,
        sorting: Optional[Sorting] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_trades_by_instrument_and_time"""
    return mg.generate_message("private/get_user_trades_by_instrument_and_time", mg.clean_params({
        "instrument_name": instrument_name,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count": count,
        "sorting": None if not sorting else sorting.value
    }))


def private_get_user_trades_by_order(order_id: str, sorting: Optional[Sorting] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_user_trades_by_order"""
    return mg.generate_message("private/get_user_trades_by_order", mg.clean_params({
        "order_id": order_id,
        "sorting": None if not sorting else sorting.value
    }))


def private_mass_quote(
        quotes: QuotesRequest,
        quote_id: str,
        mmp_group: str,
        wait_for_response: Optional[bool] = None,
        detailed: Optional[bool] = None,
        valid_until: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-mass_quote"""
    return mg.generate_message("private/mass_quote", mg.clean_params({
        "quotes": quotes,
        "quote_id": quote_id,
        "mmp_group": mmp_group,
        "wait_for_response": wait_for_response,
        "detailed": detailed,
        "valid_until": valid_until
    }))


def private_reset_mmp(index_name: IndexName, mmp_group: Optional[str] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-reset_mmp"""
    return mg.generate_message("private/reset_mmp", mg.clean_params({
        "index_name": index_name.value,
        "mmp_group": mmp_group
    }))


def private_send_rfq(instrument_name: str, amount: Optional[float] = None, side: Optional[OrderSide] = None) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-send_rfq"""
    return mg.generate_message("private/send_rfq", mg.clean_params({
        "instrument_name": instrument_name,
        "amount": amount,
        "side": None if not side else side.value
    }))


def private_set_mmp_config(
        index_name: IndexName,
        interval: int,
        frozen_time: int,
        mmp_group: Optional[str] = None,
        quantity_limit: Optional[int] = None,
        delta_limit: Optional[int] = None
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-set_mmp_config"""
    return mg.generate_message("private/set_mmp_config", mg.clean_params({
        "index_name": index_name.value,
        "interval": interval,
        "frozen_time": frozen_time,
        "mmp_group": mmp_group,
        "quantity_limit": quantity_limit,
        "delta_limit": delta_limit
    }))


def private_get_settlement_history_by_instrument(
        instrument_name: str,
        type_: Optional[SettlementType] = None,
        count: Optional[int] = None,
        continuation: Optional[str] = None,
        search_start_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_settlement_history_by_instrument"""
    return mg.generate_message("private/get_settlement_history_by_instrument", mg.clean_params({
        "instrument_name": instrument_name,
        "type": None if not type_ else type_.value,
        "count": count,
        "continuation": continuation,
        "search_start_timestamp": search_start_timestamp
    }))


def private_get_settlement_history_by_currency(
        currency: Currency,
        type_: Optional[SettlementType] = None,
        count: Optional[int] = None,
        continuation: Optional[str] = None,
        search_start_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    """https://docs.deribit.com/#private-get_settlement_history_by_currency"""
    return mg.generate_message("private/get_settlement_history_by_currency", mg.clean_params({
        "currency": currency.value,
        "type": None if not type_ else type_.value,
        "count": count,
        "continuation": continuation,
        "search_start_timestamp": search_start_timestamp
    }))
