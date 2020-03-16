from mongoengine import Document, StringField


class Client(Document):
    name = StringField(required=True, max_length=200)
    secret = StringField(required=True, max_length=64)
