from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(max_length=16, primary_key=True)
    name = models.CharField(max_length=48)
    sex = models.IntegerField(max_length=1)
    age = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_myapp_user"
