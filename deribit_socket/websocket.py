from websocket.exchange_strategy_interface import ExchangeStrategyInterface
from websocket.socket_wrapper import SocketWrapper


# deribit has a specific heartbeat message and response
HB_MSG = {"jsonrpc": "2.0", "id": 0000, "method": "public/set_heartbeat", "params": {"interval": 30}}
HB_RESPONSE = {"jsonrpc": "2.0", "id": 0000, "method": "public/test"}

# ws url
WS_URL = "wss://www.deribit.com/ws/api/v2"


class DeribitExchangeStrategy(ExchangeStrategyInterface):
    # this will add a method to the start method in SocketWrapper
    async def start(self, manager) -> None:
        await manager.send_message(HB_MSG)  # send the heartbeat message as per deribit docs

    # this will add a method to the handle_message method in SocketWrapper
    async def handle_message(self, manager, message) -> None:
        if "method" in message and message['method'] == "heartbeat":
            if message['params']['type'] == "test_request":
                await manager.send_message(HB_RESPONSE)  # respond to the heartbeat as per deribit docs


class DeribitSocketManager(SocketWrapper):
    def __init__(self):
        super().__init__(ws_url=WS_URL, strategy=DeribitExchangeStrategy())
