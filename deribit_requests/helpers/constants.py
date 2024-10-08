from dotenv import load_dotenv
import os
from enum import Enum
from typing import List, Optional, TypedDict

load_dotenv()

# ---------- apis ---------- #
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


# ---------- types ---------- #
class Currency(Enum):
    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    USDT = "USDT"
    EUR = "EURR"
    ANY = "any"
    MATIC = "MATIC"
    SOL = "SOL"
    XRP = "XRP"
    CROSS = "CROSS"


class Instrument(Enum):
    FUTURE = "future"
    OPTION = "option"
    SPOT = "spot"
    FUTURE_COMBO = "future_combo"
    OPTION_COMBO = "option_combo"
    COMBO = "combo"
    ANY = "any"


class IndexName(Enum):
    ADA_USD = "ada_usd"
    ALGO_USD = "algo_usd"
    AVAX_USD = "avax_usd"
    BCH_USD = "bch_usd"
    BTC_USD = "btc_usd"
    DOGE_USD = "doge_usd"
    DOT_USD = "dot_usd"
    ETH_USD = "eth_usd"
    LINK_USD = "link_usd"
    LTC_USD = "ltc_usd"
    MATIC_USD = "matic_usd"
    NEAR_USD = "near_usd"
    SHIB_USD = "shib_usd"
    SOL_USD = "sol_usd"
    TRX_USD = "trx_usd"
    UNI_USD = "uni_usd"
    USDC_USD = "usdc_usd"
    XRP_USD = "xrp_usd"
    ADA_USDC = "ada_usdc"
    ALGO_USDC = "algo_usdc"
    AVAX_USDC = "avax_usdc"
    BCH_USDC = "bch_usdc"
    BTC_USDC = "btc_usdc"
    DOGE_USDC = "doge_usdc"
    DOT_USDC = "dot_usdc"
    ETH_USDC = "eth_usdc"
    LINK_USDC = "link_usdc"
    LTC_USDC = "ltc_usdc"
    MATIC_USDC = "matic_usdc"
    NEAR_USDC = "near_usdc"
    SHIB_USDC = "shib_usdc"
    SOL_USDC = "sol_usdc"
    TRX_USDC = "trx_usdc"
    UNI_USDC = "uni_usdc"
    XRP_USDC = "xrp_usdc"
    ADA_USDT = "ada_usdt"
    ALGO_USDT = "algo_usdt"
    AVAX_USDT = "avax_usdt"
    BCH_USDT = "bch_usdt"
    BNB_USDT = "bnb_usdt"
    BTC_USDT = "btc_usdt"
    DOGE_USDT = "doge_usdt"
    DOT_USDT = "dot_usdt"
    ETH_USDT = "eth_usdt"
    LINK_USDT = "link_usdt"
    LTC_USDT = "ltc_usdt"
    LUNA_USDT = "luna_usdt"
    MATIC_USDT = "matic_usdt"
    NEAR_USDT = "near_usdt"
    SHIB_USDT = "shib_usdt"
    SOL_USDT = "sol_usdt"
    TRX_USDT = "trx_usdt"
    UNI_USDT = "uni_usdt"
    XRP_USDT = "xrp_usdt"
    BTCDVOL_USDC = "btcdvol_usdc"
    ETHDVOL_USDC = "ethdvol_usdc"


class SettlementType(Enum):
    SETTLEMENT = "settlement"
    DELIVERY = "delivery"
    BANKRUPTCY = "bankruptcy"


class Sorting(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"
    DEFAULT = "default"


class DepthLevel(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    ONE_HUNDRED = 100
    ONE_THOUSAND = 1000
    TEN_THOUSAND = 10000


class IndexType(Enum):
    ALL = "all"
    SPOT = "spot"
    DERIVATIVE = "derivative"


class Resolution(Enum):
    ONE = "1"
    THREE = "3"
    FIVE = "5"
    TEN = "10"
    FIFTEEN = "15"
    THIRTY = "30"
    SIXTY = "60"
    ONE_HUNDRED_TWENTY = "120"
    ONE_HUNDRED_EIGHTY = "180"
    THREE_HUNDRED_SIXTY = "360"
    SEVEN_HUNDRED_TWENTY = "720"
    ONE_DAY = "1D"
    THREE_THOUSAND_SIX_HUNDRED = "3600"
    FORTY_THREE_THOUSAND_TWO_HUNDRED = "43200"


class OrderType(Enum):
    LIMIT = "limit"
    STOP_LIMIT = "stop_limit"
    TAKE_LIMIT = "take_limit"
    MARKET = "market"
    STOP_MARKET = "stop_market"
    TAKE_MARKET = "take_market"
    MARKET_LIMIT = "market_limit"
    TRAILING_STOP = "trailing_stop"
    ALL = "all"


class TimeInForce(Enum):
    GOOD_TIL_CANCELLED = "good_til_cancelled"
    GOOD_TIL_DAY = "good_til_day"
    FILL_OR_KILL = "fill_or_kill"
    IMMEDIATE_OR_CANCEL = "immediate_or_cancel"


class TriggerType(Enum):
    INDEX_PRICE = "index_price"
    MARK_PRICE = "mark_price"
    LAST_PRICE = "last_price"


class Advanced(Enum):
    USD = "usd"
    IMPLV = "implv"


class LinkedOrderType(Enum):
    ONE_TRIGGERS_OTHER = "one_triggers_other"
    ONE_CANCELS_OTHER = "one_cancels_other"
    ONE_TRIGGERS_ONE_CANCELS_OTHER = "one_triggers_one_cancels_other"


class TriggerFillCondition(Enum):
    FIRST_HIT = "first_hit"
    COMPLETE_FILL = "complete_fill"
    INCREMENTAL = "incremental"


class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"


class CancelType(Enum):
    DELTA = "delta"
    QUOTE_SET_ID = "quote_set_id"
    INSTRUMENT = "instrument"
    INSTRUMENT_KIND = "instrument_kind"
    CURRENCY = "currency"
    CURRENCY_PAIR = "currency_pair"
    ALL = "all"


class OrderDetails(TypedDict):
    price: Optional[float]
    amount: Optional[float]
    post_only: Optional[bool]
    reject_post_only: Optional[bool]


class Quote(TypedDict):
    instrument_name: str
    quote_set_id: str
    ask: Optional[OrderDetails]
    bid: Optional[OrderDetails]


class QuotesRequest(TypedDict):
    quotes: List[Quote]


class MarginModel(Enum):
    CROSS_PM = "cross_pm"
    CROSS_SM = "cross_sm"
    SEGREGATED_PM = "segregated_pm"
    SEGREGATED_SM = "segregated_sm"


class Mode(Enum):
    REJECT_TAKER = "reject_taker"
    CANCEL_MAKER = "cancel_maker"


class Group(Enum):
    NONE = "none"
    ONE = "1"
    TWO = "2"
    FIVE = "5"
    TEN = "10"
    TWENTY_FIVE = "25"
    ONE_HUNDRED = "100"
    TWO_HUNDRED_FIFTY = "250"


class BookInterval(Enum):
    MS100 = "100ms"
    AGG2 = "agg2"
    RAW = "raw"
