
from .models import TechnicalRecord ,Player


class AnalysisDTO():
    def __init__(self):
        pass

    def player_status(self, db_model : TechnicalRecord):
        return {
            "forehand" : db_model.forehand,
            "backhand" : db_model.backhand,
            "serve" : db_model.serve,
            "volley" : db_model.volley,
            "movement" : db_model.movement,
            "listening" : db_model.listening,
            "class_date" : db_model.class_date if db_model.class_date is not None else "-",
            "note" : db_model.note if db_model.note is not None else "-",
            "class_duration" : db_model.class_duration
        }
    
    def player_status_list(self, db_models):
        return [self.player_status(item) for item in db_models]
    
    def player(self, db_model : Player):
        return{
            "name" : db_model.name,
            "dob" : db_model.dob
        }
    
    def avgs(self, db_model):
        return {
            'movement_avg' : round(db_model['movement']['movement__avg'],2),
            'listening_avg' : round(db_model['listening']['listening__avg'],2),
            'forehand_avg' : round(db_model['forehand']['forehand__avg'],2) if db_model['forehand']['forehand__avg'] is not None else 0,
            'backhand_avg' : round(db_model['backhand']['backhand__avg'],2) if db_model['backhand']['backhand__avg'] is not None else 0,
            'serve_avg' : round(db_model['serve']['serve__avg'],2) if db_model['serve']['serve__avg'] is not None else 0,
            'volley_avg' : round(db_model['volley']['volley__avg'],2) if db_model['volley']['volley__avg'] is not None else 0,
        }
    
    def media(self , db_models):
        return [{'note':item.note, 'url':item.media_url , 'date':item.date_created} for item in db_models]
    
    def bar_datas(self, db_models):
        return [{'date':str(item.class_date), 'data':item.sum} for item in db_models]
