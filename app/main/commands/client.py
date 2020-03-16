from flask_script import Command, Option

from ..services.client_service import create_client


class CreateNewClient(Command):

    option_list = (
        Option('--name', '-n', dest='name', help="The client name", required=True),
    )

    def run(self, name):
        client = create_client(name)
        print(f"Details for client {name} - client_id: {client.id}, client_secret: {client.secret} ")
