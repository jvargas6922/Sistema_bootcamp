from django.db import models

class Bootcamp(models.Model):
    id_bootcamp = models.AutoField(primary_key=True)
    bootcamp = models.CharField(max_length=120)
    
    class Meta:
        managed = False
        db_table = 'bootcamps'
    
    def __str__(self):
        return self.bootcamp








