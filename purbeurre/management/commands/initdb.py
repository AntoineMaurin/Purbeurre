from django.core.management.base import BaseCommand, CommandError
from purbeurre.database_init import DatabaseInit
from purbeurre.models import Product, Category

class Command(BaseCommand):
    help = 'Says HELLO'

    def handle(self, *args, **options):

        d = DatabaseInit()
        d.delete_products()
        d.request()
