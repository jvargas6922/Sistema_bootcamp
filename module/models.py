from django.db import models
from bootcamp.models import Bootcamp

# Create your models here.
class Module(models.Model):
    id_module = models.AutoField(primary_key=True)
    module = models.CharField(max_length=100)
    id_bootcamp = models.ForeignKey(Bootcamp, db_column='id_bootcamp', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'modules'

    def __str__(self):
        return self.module