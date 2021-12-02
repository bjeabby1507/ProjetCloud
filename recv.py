import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

CONNECTION_STR = os.environ.get("CONNECTION_STR_RCV")
EVENTHUB_NAME = 'eventhubprojetcloud'
STORAGE_CONNECTION_STR = os.environ.get("STORAGE_CONNECTION_STR")
BLOB_CONTAINER_NAME = "containerprojetcloud"  # Please make sure the blob container resource exists.

async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(STORAGE_CONNECTION_STR, BLOB_CONTAINER_NAME)

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(CONNECTION_STR, consumer_group="$Default", eventhub_name=EVENTHUB_NAME, checkpoint_store=checkpoint_store)
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1") # "-1" is from the beginning of the partition.

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())
    
    #asyncio.run(main())