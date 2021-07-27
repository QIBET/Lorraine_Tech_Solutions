from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Lorraine Tech Solutions"
    return render(request, 'index.html',{"title":title})