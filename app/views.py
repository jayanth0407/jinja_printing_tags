from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'jayanth',}
    return render(request,'jinja.html',context=d)
