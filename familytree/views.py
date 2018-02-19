from django.shortcuts import render
from django.http import HttpResponse
from familytree.models import FamilyMember
import json

# Create your views here.
def identify(request, user_id):
    person = FamilyMember.objects.get(pk=user_id)
    children = []
    children.extend(person.mothered.all())
    children.extend(person.fathered.all())
    context = {
        "name": person.name,
        "mother": person.mother,
        "father": person.father,
        "children": children
    }
    return render(request, "familytree/person.html", context)

def index(request):
    people = FamilyMember.objects.all()
    context = {"people": people}
    return render(request, "familytree/index.html", context)