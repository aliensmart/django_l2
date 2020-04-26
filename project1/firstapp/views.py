from django.shortcuts import render
from firstapp.models import Topic, AccessRecord, Webpage
# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': webpage_list
    }
    return render(request, 'firstapp/index.html', context=date_dict)