
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
            "note" : db_model.note if db_model.note is not None else "-" 
        }
    
    def player_status_list(self, db_models):
        return [self.player_status(item) for item in db_models]
    
    def player(self, db_model : Player):
        return{
            "name" : db_model.name,
            "dob" : db_model.dob
        }