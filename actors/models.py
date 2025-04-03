from django.db import models

NATIONALITY_CHOICES = (
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
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name + " (" + self.nationality + ")"
