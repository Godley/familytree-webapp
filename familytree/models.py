from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    mother = models.ForeignKey('self', on_delete=models.CASCADE, related_name="mothered", null=True, blank=True)
    father = models.ForeignKey('self', on_delete=models.CASCADE, related_name="fathered", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def children(self):
        children = []
        children.extend(self.mothered.all())
        children.extend(self.fathered.all())
        return children

    @property
    def siblings(self):
        father_children = self.father.children
        mother_children = self.mother.children
        siblings = set(father_children)
        siblings = siblings.intersection(set(mother_children))
        siblings.remove(self)
        return siblings