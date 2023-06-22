# Views.py for Home.html by Maximilian Kuehn, 22/06/2023

# import from
from django.shortcuts import render
from .models import Paragraph

# loading context from paragraph objects
def homeaction(request):
    paragraphs = Paragraph.objects.all()
    context = {'paragraphs': paragraphs}
    return render(request,'Home.html', context)