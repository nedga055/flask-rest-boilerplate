import secrets
from bson.objectid import ObjectId
from bson.errors import InvalidId
from ..models.client import Client


def get_all_clients():
    return Client.objects().all()


def get_client(client_id):
    try:
        client = Client.objects(id=ObjectId(client_id)).first()
    except InvalidId:
        # Provided client_id is not a valid ObjectId. Set client to None
        client = None
    return client


def create_client(client_name):
    client = Client(name=client_name, secret=secrets.token_hex(24))
    client.save()
    return client
