from django.shortcuts import render

def index(request):
    # Logic to fetch data about monuments from the database or other sources
    monuments_data = [...]  # Example data
    return render(request, 'monuments/index.html', {'monuments_data': monuments_data})
