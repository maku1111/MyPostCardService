from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def createpostcardaction(request):
    return render(request,'Create_your_postcard.html')
