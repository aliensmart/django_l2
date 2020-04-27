from django.shortcuts import render
from firstapp.models import Topic, AccessRecord, Webpage
from firstapp import theform

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': webpage_list
    }
    return render(request, 'firstapp/index.html', context=date_dict)

def form_name_view(request):
    form = theform.FormName

    if request.method == 'POST':
        
        form = theform.FormName(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

    return render(request, 'firstapp/form.html', {'form':form})