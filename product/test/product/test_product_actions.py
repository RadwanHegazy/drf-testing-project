from channels.testing import WebsocketCommunicator, ChannelsLiveServerTestCase
from core.asgi import application
from globals.test_objects import create_access_token, create_user, create_product
from channels.db import database_sync_to_async

class TestProductActions(ChannelsLiveServerTestCase):

    def endpoint (self, access_token) : 
        return f'/ws/notifications?token={access_token}'
    
    async def test_not_connected(self) : 
        communicator = WebsocketCommunicator(
            application,
            self.endpoint('')
        )

        connected, _ = await communicator.connect()

        self.assertFalse(connected)
        await communicator.disconnect()


    async def test_connect_not_superuser(self) : 
        access_token = await database_sync_to_async(create_access_token)()

        communicator = WebsocketCommunicator(
            application,
            self.endpoint(access_token)
        )

        connected, _ = await communicator.connect()

        self.assertFalse(connected)
        await communicator.disconnect()

    async def test_product_creation_and_delation_notification(self) : 
        superuser = await database_sync_to_async(create_user)(is_superuser=True)
        access_token = await database_sync_to_async(create_access_token)(superuser)

        communicator = WebsocketCommunicator(
            application,
            self.endpoint(access_token)
        )

        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        product = await database_sync_to_async(create_product)()

        res = await communicator.receive_from()
        self.assertIn(product.title, res)


        await database_sync_to_async(product.delete)()

        res = await communicator.receive_from()
        self.assertIn(product.title, res)

        await communicator.disconnect()

    async def test_not_superuser(self) : 
        user = await database_sync_to_async(create_user)(is_superuser=False)
        access_token = await database_sync_to_async(create_access_token)(user)

        communicator = WebsocketCommunicator(
            application,
            self.endpoint(access_token)
        )

        connected, _ = await communicator.connect()
        self.assertFalse(connected)
