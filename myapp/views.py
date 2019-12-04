from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, "base.html")

def child1(request):
    return render(request, "child1.html")

def child2(request):
    return render(request, "child2.html")

def form(request):
    print(request.POST)
    return render(request, "form.html")