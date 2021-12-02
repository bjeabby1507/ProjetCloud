import script
import asyncio
import os
import time
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

CONNECTION_STR = os.environ.get("CONNECTION_STR")
EVENTHUB_NAME = 'eventhubprojetcloud'

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR,eventhub_name=EVENTHUB_NAME)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        #event_data_batch.add(EventData('First event '))
        event_data_batch.add(EventData(str(script.getdata(script.url, script.headers)))) # For MessageBodyType.Data, the body must be str or bytes or list of str or bytes.
        #event_data_batch.add(EventData('Third event'))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(run())

#start_time = time.time()
#asyncio.run(run())
print("Send messages in {} seconds.".format(time.time() - start_time))