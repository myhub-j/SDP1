from django.shortcuts import render

def index(request):
    # Logic to fetch data about festivals
    festivals_data = [...]  # Example data
    return render(request, 'festivals/index.html', {'festivals_data': festivals_data})
