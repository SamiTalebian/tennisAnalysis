from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from analysis.models import Player, TechnicalRecord

from .DTO import AnalysisDTO

def player_detail(request, uuid):
    try:
        player = Player.objects.get(uuid=uuid)
        technical_records = TechnicalRecord.objects.filter(player__uuid=uuid).order_by('-date_created')
    except:
        raise Http404("Player not found!")
    
    if technical_records is None or len(technical_records) == 0: 
        return HttpResponseNotFound("No records have been found!")

    dto_class = AnalysisDTO()
    return render(request, 'analysis/detail.html', {'records': dto_class.player_status_list(db_models=technical_records), 'player': dto_class.player(db_model=player)})
