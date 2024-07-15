from django.db import models
from module.models import Module
# Create your models here.

class Section(models.Model):
    id_section = models.AutoField(primary_key=True)
    section = models.CharField(max_length=120)
    id_module = models.ForeignKey(Module, db_column='id_module', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'sections'

    def __str__(self):
        return self.section
