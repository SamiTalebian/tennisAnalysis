from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from analysis.models import Player, TechnicalRecord

def player_detail(request, uuid):
    try:
        player = Player.objects.get(uuid=uuid)
        technicalReords = TechnicalRecord.objects.filter(player__uuid=uuid).order_by('-date_created')
    except:
        raise Http404("Player not found!")
    
    if technicalReords is None or len(technicalReords) == 0: 
        return HttpResponseNotFound("No records have been found!")

    return render(request, 'analysis/detail.html', {'records': list(technicalReords), 'player':player})
