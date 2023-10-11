from django.db import models

class Record(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    Phone = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, unique=True)
    Email = models.CharField(max_length=100, unique=True)
    University = models.CharField(max_length=50)
    School = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Block_Dorm = models.CharField(max_length=50)
    Acadamics = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    



    

