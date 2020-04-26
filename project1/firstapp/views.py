from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {
        'the_text': 'this is a text from view'
    }
    return render(request, 'firstapp/index.html', context=my_dict)