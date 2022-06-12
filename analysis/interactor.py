

from django.http import Http404, HttpResponseNotFound
from analysis.models import Player, TechnicalRecord
from django.db.models import Avg

class AnalysisInteractor():
    def __init__(self):
        pass

    def set_params(self, uuid):
        self.uuid = uuid
    
    def _get_player_records(self):
        try:
            self.player = Player.objects.get(uuid=self.uuid)
            self.technical_records = TechnicalRecord.objects.filter(player__uuid=self.uuid).order_by('-class_date')
        except:
            raise Http404("Player not found!")

    def _check_records(self):
        if self.technical_records is None or len(self.technical_records) == 0: 
            raise HttpResponseNotFound("No records have been found!")

    def _get_avgs(self):
        self.avg = {'movement' : 0 , 'listening' : 0}
        self.avg['movement'] = TechnicalRecord.objects.all().aggregate(Avg('movement'))
        self.avg['listening'] = TechnicalRecord.objects.all().aggregate(Avg('listening'))

    def _get_player_avgs(self):
        self.p_avg = {'movement' : 0 , 'listening' : 0}
        self.p_avg['movement'] = TechnicalRecord.objects.filter(player__uuid=self.uuid).all().aggregate(Avg('movement'))
        self.p_avg['listening'] = TechnicalRecord.objects.filter(player__uuid=self.uuid).aggregate(Avg('listening'))

    def execute(self):
        self._get_player_records()
        self._check_records()
        self._get_avgs()
        self._get_player_avgs()

        return {'Avg':self.avg,'p_Avg':self.p_avg ,'player':self.player,'records': self.technical_records}
        
    
       