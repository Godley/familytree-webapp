from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    mother = models.ForeignKey('self', on_delete=models.CASCADE, related_name="mothered", null=True, blank=True)
    father = models.ForeignKey('self', on_delete=models.CASCADE, related_name="fathered", null=True, blank=True)

    def __str__(self):
        return self.name