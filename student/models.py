from django.db import models

# Create your models here.

class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    email = models.EmailField

    class Meta:
        managed = False
        db_table = 'students'

    def __str__(self):
        return self.name
