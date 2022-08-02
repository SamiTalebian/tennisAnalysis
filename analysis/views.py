from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render 
from analysis.interactor import AnalysisInteractor
from analysis.models import Player, TechnicalRecord

from .DTO import AnalysisDTO

def player_detail(request, uuid):
    analysis_interactor = AnalysisInteractor()
    analysis_interactor.set_params(uuid=uuid)

    body = analysis_interactor.execute()
    
    dto_class = AnalysisDTO()
    return render(request, 'analysis/detail.html', {'records': dto_class.player_status_list(db_models=body['records']),
     'player': dto_class.player(db_model=body['player']),
     'avgs' : dto_class.avgs(db_model=body['Avg']),
     'p_avgs': dto_class.avgs(db_model=body['p_Avg']),
     'medias' : dto_class.media(db_models=body['media']),
     'bar_datas' : dto_class.bar_datas(db_models=body['bar_datas']),
     'records_count' : body['records_count'],
     'total_time' : body['total_time'],
     })
