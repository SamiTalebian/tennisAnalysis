

from django.http import Http404, HttpResponseNotFound
from analysis.models import Player, PlayerMedia, TechnicalRecord
from django.db.models import Avg, Q, F, Sum
import random
import operator

class AnalysisInteractor():
    def __init__(self):
        pass

    def set_params(self, uuid):
        self.uuid = uuid
    
    def _get_player_records(self):
        try:
            self.player = Player.objects.get(uuid=self.uuid)
            self.technical_records = TechnicalRecord.objects.filter(player__uuid=self.uuid).order_by('-id')
            self.time_in_court = TechnicalRecord.objects.filter(player__uuid=self.uuid).aggregate(total_time=Sum('class_duration'))
        except:
            raise Http404("Player not found!")

    def _check_records(self):
        if self.technical_records is None or len(self.technical_records) == 0: 
            raise HttpResponseNotFound("No records have been found!")

    def _get_avgs(self):
        self.avg = {'movement' : 0 , 'listening' : 0, 'forehand' : 0, 'backhand': 0, 'serve' : 0, 'volley' : 0}
        self.avg['movement'] = TechnicalRecord.objects.all().aggregate(Avg('movement'))
        self.avg['listening'] = TechnicalRecord.objects.all().aggregate(Avg('listening'))
        self.avg['forehand'] = TechnicalRecord.objects.filter(~Q(forehand=0)).aggregate(Avg('forehand'))
        self.avg['backhand'] = TechnicalRecord.objects.filter(~Q(backhand=0)).aggregate(Avg('backhand'))
        self.avg['serve'] = TechnicalRecord.objects.filter(~Q(serve=0)).aggregate(Avg('serve'))
        self.avg['volley'] = TechnicalRecord.objects.filter(~Q(volley=0)).aggregate(Avg('volley'))
        

    def _get_player_avgs(self):
        self.p_avg = {'movement' : 0 , 'listening' : 0, 'forehand' : 0, 'backhand': 0, 'serve' : 0, 'volley' : 0}
        self.p_avg['movement'] = TechnicalRecord.objects.filter(player__uuid=self.uuid).aggregate(Avg('movement'))
        self.p_avg['listening'] = TechnicalRecord.objects.filter(player__uuid=self.uuid).aggregate(Avg('listening'))
        self.p_avg['forehand'] = TechnicalRecord.objects.filter(~Q(forehand=0),player__uuid=self.uuid).aggregate(Avg('forehand'))
        self.p_avg['backhand'] = TechnicalRecord.objects.filter(~Q(backhand=0),player__uuid=self.uuid).aggregate(Avg('backhand'))
        self.p_avg['serve'] = TechnicalRecord.objects.filter(~Q(serve=0),player__uuid=self.uuid).aggregate(Avg('serve'))
        self.p_avg['volley'] = TechnicalRecord.objects.filter(~Q(volley=0),player__uuid=self.uuid).aggregate(Avg('volley'))

    def _get_player_media(self):
        self.media = []
        for item in PlayerMedia.objects.values_list('players','id'):
            if item[0] == self.player.id:
                self.media.append(PlayerMedia.objects.get(id=item[1]))
    
    def _get_bar_data(self):
        self.bar_datas = []

        signeture_data = self.technical_records.order_by('-id').annotate(sum=(F('forehand') + F('listening') + F('movement') + F('backhand') + F('serve') + F('volley'))/6)
    
        data_count = signeture_data.count()

        self.bar_datas.append(signeture_data[data_count-1])
        self.bar_datas.append(signeture_data[data_count-2])
        self.bar_datas.append(signeture_data[int(data_count/2)])
        self.bar_datas.append(signeture_data[1])
        self.bar_datas.append(signeture_data[0])
        
        return self.bar_datas



    def execute(self):
        self._get_player_records()
        self._check_records()
        self._get_avgs()
        self._get_player_avgs()
        self._get_player_media()
        self._get_bar_data()

        return {'Avg':self.avg,'p_Avg':self.p_avg ,
        'player':self.player, 'records': self.technical_records ,
        'media' : self.media, 'records_count' : TechnicalRecord.objects.count(),
        'bar_datas' : self.bar_datas, 'total_time' : self.time_in_court['total_time']}
        
    
       