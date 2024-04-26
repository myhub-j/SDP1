from django.shortcuts import render

def index(request):
    # Logic to fetch data about dance forms
    dance_forms_data = [...]  # Example data
    return render(request, 'dance_froms/index.html', {'dance_froms_data': dance_forms_data})
