from logs.logger_helper import LoggerHelper
from orderbook.update_strategy_interface import UpdateStrategyInterface
from orderbook.tracker_interface import TrackerInterface
from orderbook.orderbook_wrapper import OrderBookWrapper
from orderbook.constants import (
    BOOK_SIDE_UPDATE,
    BookSide,
    SORTED_BOOK,
    InvalidOrderBookUpdate
)
from typing import Tuple, Optional


logger = LoggerHelper(__file__)


class DeribitUpdateStrategy(UpdateStrategyInterface):
    """
    DeribitUpdateStrategy is an implementation of UpdateStrategyInterface that handles order book data parsing specifically for Deribit.
    """
    def __init__(self):
        super().__init__()
        self.logger = logger.get_logger(f"{__name__}.{self.__class__.__name__}")

    def parse_update(self, obj) -> Tuple[BOOK_SIDE_UPDATE, BOOK_SIDE_UPDATE]:
        try:
            return obj['params']['data'][BookSide.BIDS.value], obj['params']['data'][BookSide.ASKS.value]
        except Exception as e:
            self.logger.error(f"Error parsing order book update: {e}\nObject: {obj}")

    def normalize_size(self, price, size, size_flag) -> float:
        try:
            return size / price if size_flag else size  # futures sizes come in quote currency rather than base
        except Exception as e:
            self.logger.error(f"Error normalizing order book size: {e}\nprice, size, size_flag: {price, size, size_flag}")


class DeribitTracker(TrackerInterface):
    """
    DeribitTracker is an implementation of TrackerInterface that handles tracking order book updates specifically for Deribit.
    """
    def __init__(self):
        super().__init__()
        self.logger = logger.get_logger(f"{__name__}.{self.__class__.__name__}")

    def initialize(self, obj) -> None:
        self.update_tracker(obj)
        self.logger.info(f"Tracker Initialized: {self.tracker}")

    def validate_update(self, obj) -> bool:
        if obj['params']['data']['prev_change_id'] == self.tracker['change_id']:
            # valid update, no messages skipped
            self.update_tracker(obj)  # ensure to update the tracker each time
            return True
        else:
            # there was a message skipped, clear data, and refresh book
            self.logger.error(f"There was an invalid order book object. Possibility of a skipped message."
                              f"Object: {obj}\nTracker: {self.tracker}")
            return False

    def update_tracker(self, obj) -> None:
        data = obj['params']['data']
        change_id = data['change_id']
        self.tracker.update({'prev_change_id': change_id if 'prev_change_id' not in data else data['prev_change_id'], 'change_id': change_id})


class DeribitOrderBook(OrderBookWrapper):
    """
    DeribitOrderBook is an implementation of OrderBookWrapper that handles order book updates specifically for Deribit.
    """
    def __init__(self, limit: int, size_flag: bool = False):
        super().__init__(limit, size_flag, DeribitUpdateStrategy(), DeribitTracker())
        self.logger = logger.get_logger(f"{__name__}.{self.__class__.__name__}")

    def initialize(self, obj) -> SORTED_BOOK:
        data = obj['params']['data']
        self.orderbook[BookSide.BIDS.value].update({bid[1]: self.update_strategy.normalize_size(bid[1], bid[2], self.size_flag) for bid in data[BookSide.BIDS.value] if bid[0] == 'new'})
        self.orderbook[BookSide.ASKS.value].update({ask[1]: self.update_strategy.normalize_size(ask[1], ask[2], self.size_flag) for ask in data[BookSide.ASKS.value] if ask[0] == 'new'})
        self.tracker.initialize(obj)
        self.logger.info(f"Order Book Initialized: {self.orderbook}")
        return self.orderbook

    def update_orderbook_side(self, updates: BOOK_SIDE_UPDATE, book_side: BookSide) -> None:
        # update action: 'new' or 'change' (not 'delete')
        self.orderbook[book_side].update({update[1]: self.update_strategy.normalize_size(update[1], update[2], self.size_flag) for update in updates if update[0] != 'delete'})

        # remove action: 'delete' orders
        for price in [update[1] for update in updates if update[0] == 'delete']:
            self.orderbook[book_side].pop(price, None)

    def handler(self, obj) -> Optional[SORTED_BOOK]:
        if self.tracker.validate_update(obj) is True:  # valid update, update book as normal
            self.update_book(obj)
            return self.orderbook
        else:  # invalid update, reset order book
            self.logger.error("Invalid order book update. Throwing InvalidOrderBookUpdate, resetting order book data, and restarting order book stream.")
            raise InvalidOrderBookUpdate  # raise an error to reset the book
