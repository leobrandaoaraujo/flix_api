# Generated by Django 5.1.3 on 2025-04-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="nationality",
            field=models.CharField(
                choices=[
                    ("BRA", "Brasil"),
                    ("EUA", "Estados Unidos"),
                    ("ENG", "Inglaterra"),
                    ("GER", "Alemanha"),
                    ("AUS", "Austrália"),
                    ("AUT", "Áustria"),
                    ("MEX", "México"),
                    ("CHN", "China"),
                    ("COL", "Colômbia"),
                    ("NZL", "Nova Zelândia"),
                    ("ESP", "Espanha"),
                    ("CAN", "Canadá"),
                    ("ZAF", "África do SUl"),
                    ("GBR", "Escócia"),
                    ("IRL", "Irlanda"),
                    ("ITA", "Itália"),
                    ("PRT", "Portugal"),
                ],
                max_length=100,
            ),
        ),
    ]
