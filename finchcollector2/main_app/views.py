from django.shortcuts import render

finches = [
  {'name': 'Flicker', 'breed': 'Shaft-tail', 'description': 'never idle, always moving', 'age': 2},
  {'name': 'Runnymede', 'breed': 'European Goldfinch', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches})