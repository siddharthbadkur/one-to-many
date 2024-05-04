from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    dep_name=models.CharField(max_length=100,verbose_name='Name')
    description=models.TextField(max_length=200)
    def __str__(self):
        return  self.dep_name

# Create your models here.
class StudentModel(models.Model):
    stu_Name=models.CharField(max_length=50)
    stu_Email=models.EmailField()
    stu_Contact=models.IntegerField()
    stu_department=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.stu_Name
