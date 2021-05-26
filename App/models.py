from django.db import models

# Create your models here.

class InputData(models.Model):
    
    pin = models.CharField(db_column="key", max_length=50, null=True)

    FileName = models.FileField(db_column="FileField", null=True)

    
