import csv
from actors.models import Actor
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", type=str, help="Nome do arquivo CSV de atores."
        )

    def handle(self, *args, **options):
        file_name = options["file_name"]
        self.stdout.write(
            self.style.NOTICE(
                f"Iniciando a importação do arquivo de atores '{file_name}'..."
            )
        )
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                nationality = row["nationality"]
                Actor.objects.create(name=name, nationality=nationality)
        self.stdout.write(
            self.style.SUCCESS(
                f"Importação do arquivo de '{file_name}' realizada com sucesso!"
            )
        )
