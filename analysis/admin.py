from operator import truediv
from xmlrpc.client import Boolean
from django.contrib import admin
from analysis.models import Payment, PhysicalRecord, Player, Staff, StaffRecord, TechnicalRecord
#from django_jalali.admin.filters import JDateFieldListFilter


class MyAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        # reorder the app list as you like
        return app_list
    admin.AdminSite.get_app_list = get_app_list



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'right_hand', 'dob' , 'height' , 'weight' , 'time_in_court' , 'date_created' ,'url']
    list_display_links = ('id','name')
    search_fields = ['name']
    list_per_page = 30


    def url(self, obj):
        return 'https://atp-analysis.herokuapp.com/player-status/' + str(obj.uuid)
    
    def time_in_court(self, obj):
        sum = 0
        for i in obj.players.all():
            sum += i.class_duration
        
        return sum



@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'date_created', 'time_in_court', 'staff_last_payment','time_in_court_since_last_payment']
    list_display_links = ('id','name')
    search_fields = ['name']


    def time_in_court(self, obj):
        sum = 0
        for i in obj.staffs_sr.all():
            sum += i.class_duration

        return sum
    
    def staff_last_payment(self, obj):
        return obj.payments.order_by('payment_date').last()


    def time_in_court_since_last_payment(self, obj):
        sum = 0

        last_payment = obj.payments.order_by('payment_date').last()
        if last_payment is None:
            return self.time_in_court(obj)

        for i in obj.staffs_sr.all():
            if str(i.date_created) > str(last_payment):
                sum += i.class_duration

        return sum

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_date', 'staff']
    list_display_links = ('id','staff')
    list_filter = ['staff']


@admin.register(TechnicalRecord)
class TechnicalRecordAdmin(admin.ModelAdmin):
    fields = (('player','staff'),('class_date','class_duration'),('forehand' , 'backhand') , ('serve' , 'volley'), ('movement' , 'listening'), 'note')
    list_display = ['id' , 'player', 'staff' , 'class_date' ,'date_created','class_duration' ,'forehand' , 'backhand' , 'serve' , 'volley' , 'movement' , 'listening' , 'has_note']
    list_display_links = ('id','player')
    search_fields = ['player__name', 'staff__name']
    list_per_page = 30

    list_filter = ['staff']

    def has_note(self, obj) -> Boolean:
        return len(obj.note) > 0


    has_note.boolean = True

@admin.register(PhysicalRecord)
class PhysicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id' , 'player', 'staff' , 'date_created' , 'class_date','stamina' , 'stretching' , 'movement' , 'attention', 'has_note' ]
    list_display_links = ('id','player')
    search_fields = ['player__name', 'staff__name']

    list_filter = ['staff']

    def has_note(self, obj) -> Boolean:
        return len(obj.note) > 0

    has_note.boolean = True

@admin.register(StaffRecord)
class StaffRecordAdmin(admin.ModelAdmin):
    list_display = ['id' , 'staff', 'date_created' , 'class_duration' , 'mark']
    list_display_links = ('id','staff')
    search_fields = ['staff', 'date_created']
