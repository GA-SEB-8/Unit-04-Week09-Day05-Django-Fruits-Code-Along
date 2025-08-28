from django.db import models

# Create your models here.

# all your models should inheret from the models.Model class
class Fruit(models.Model):
    name = models.CharField(max_length=80, unique=True)
    is_ready_to_eat = models.BooleanField(default=False)

    class Meta:
        db_table = 'fruits' # save table in db as 'fruits'