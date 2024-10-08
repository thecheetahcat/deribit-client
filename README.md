# Deribit Client Package

---

## Description:
`deribit-client` has implementation for all requests and streams from the Deribit documentation. Also includes a custom orderbook from the `orderbook-handler` package,
custom websocket from the `socket-client` package, as well as custom logging, and encrypted notifications from the `logging-notifications` package. This is meant to be
the base for any algorithmic trading on Deribit, providing functionality for all requests and streams, websocket management, and orderbook data handling. 

---

## Installation

### Requirements
- Python 3.8+
- `socket_client` 
- `orderbook_handler` 
- `logging_notifications`

You can install the required dependencies via `pip`:
```bash
pip install -r requirements.txt
```

***Please read through each of the above packages to get a full understanding for `deribit-client`:***
- [socket-client](https://github.com/thecheetahcat/socket-client)
- [orderbook-handler](https://github.com/thecheetahcat/orderbook-handler)
- [logging-notifications](https://github.com/thecheetahcat/logging-notifications)

---

## Required Environment Variables
For private requests / streams, you must authenticate your connection with your Deribit client ID and secret ID.
Add the following to your `.env` file:
```bash
# DERIBIT CREDENTIALS
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<you-client-secret>
```
***Learn more about Deribit API keys and how to generate them [here](https://www.deribit.com/kb/asymmetric-api-keys).***

The encrypted notifications functionality relies on the following environment variables stored in a `.env` file:
```bash
# MATRIX NIO Credentials
USERNAME=<your-matrix-username>
PASSWORD=<your-matrix-password>
ROOM_ID=<your-matrix-room-id>
```

The final `.env` file should look like this:
```bash
# DERIBIT CREDENTIALS
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<you-client-secret>

# MATRIX NIO Credentials
USERNAME=<your-matrix-username>
PASSWORD=<your-matrix-password>
ROOM_ID=<your-matrix-room-id>
```

---

## Usage

### Example testing callback functionality, streams, and requests:
```python
from deribit_socket.websocket import DeribitSocketManager
import deribit_requests.methods.authentication as auth
import deribit_requests.methods.market_data as md
import deribit_requests.subscriptions.public as pub
import deribit_requests.methods.subscription_management as sub
import deribit_requests.helpers.constants as constants
from deribit_orderbook.orderbook import DeribitOrderBook
import asyncio

auth_message = auth.public_auth_credentials()  # authorize the connection with your CLIENT_ID and CLIENT_SECRET
request = md.public_get_instrument("BTC-PERPETUAL")  # example request
subscribe = sub.private_subscribe([pub.book_instrument_name_interval("BTC-PERPETUAL", constants.BookInterval.MS100)])  # orderbook subscription

manager = DeribitSocketManager()  # set up the socket client
book = DeribitOrderBook(limit=1, size_flag=True)  # set up the orderbook data handler


def callback(obj):  # callback function to handle orderbook data
    if 'method' in obj and obj['method'] == 'subscription' and 'book' in obj['params']['channel']:  # identify the book subscription
        symbol = obj['params']['data']['instrument_name']  # find the symbol

        if obj['params']['data']['type'] == 'snapshot':  # initialize the book on the snapshot
            book.initialize(obj)

        elif obj['params']['data']['type'] == 'change':  # update on each change
            book.handler(obj)

        print(f"{symbol}: {book.orderbook}")

    else:
        print(obj)


async def main():
    # start and authorize the connection
    await manager.start()
    task = asyncio.create_task(manager.run())
    await manager.send_message(auth_message)

    # send a request and add the callback method
    await asyncio.sleep(1)
    await manager.send_message(request)
    manager.add_callback_method(callback)

    # send a subscription message
    await asyncio.sleep(1)
    await manager.send_message(subscribe)

    # allow the connection to stay alive for the next 120 seconds
    await asyncio.sleep(120)
    # you could put more functionality here ...
    await manager.stop_stream(task)  # safely close the connection


asyncio.run(main())
```

---

#### License
This package is licensed under the MIT License. See the LICENSE file for details.