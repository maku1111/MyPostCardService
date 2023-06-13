from django.shortcuts import render
from .models import Paragraph

# Create your views here.
def homeaction(request):
    paragraphs = Paragraph.objects.all()
    context = {'paragraphs': paragraphs}
    return render(request,'Home.html', context)