from django.core.management import call_command
from django.core.management.base import BaseCommand

from ...endpoints.DatabaseCaller import DatabaseCaller

class Command(BaseCommand):
    help = 'Runs server with database parameters'

    def add_arguments(self, parser):
        parser.add_argument("dbUser", type=str, help='Indicates the username to pass to the db')
        parser.add_argument("dbPassword", type=str, help="Indicates the password to pass to the db")
        parser.add_argument("dbIPAddress", type=str, help="Indicates the IP address that the db is hosted on")
        parser.add_argument("dbDatabase", type=str, help="Indicates the Database being accessed for content")

    def handle(self, *args, **kwargs):
        dbUser = kwargs['dbUser']
        dbPassword = kwargs['dbPassword']
        dbIPAddress = kwargs['dbIPAddress']
        dbDatabase = kwargs['dbDatabase']
        kwargs = {}
        kwargs['addrport'] = "8000"

        DatabaseCaller.server = dbIPAddress
        DatabaseCaller.username = dbUser
        DatabaseCaller.password = dbPassword
        DatabaseCaller.database = dbDatabase

        call_command('runserver', *args, **kwargs)