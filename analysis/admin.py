from operator import truediv
from xmlrpc.client import Boolean
from django.contrib import admin
from analysis.models import Payment, PhysicalRecord, Player, Staff, TechnicalRecord
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Player) 
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'right_hand', 'dob' , 'height' , 'weight' , 'date_created']
    search_fields = ['name']



@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'date_created', 'time_in_court', 'staff_last_payment','time_in_court_since_last_payment']
    search_fields = ['name']


    def time_in_court(self, obj):
        sum = 0
        for i in obj.staffs.all():
            sum += i.class_duration

        for i in obj.staffs_pr.all():
            sum += i.class_duration
        return sum
    
    def staff_last_payment(self, obj):
        return obj.payments.order_by('payment_date').last()


    def time_in_court_since_last_payment(self, obj):
        sum = 0
        last_payment = obj.payments.order_by('payment_date').last()
        for i in obj.staffs.all():
            if str(i.date_created) > str(last_payment):
                sum += i.class_duration
        
        for i in obj.staffs_pr.all():
            if str(i.date_created) > str(last_payment):
                sum += i.class_duration

        return sum

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_date', 'staff']
    list_filter = ['staff']


@admin.register(TechnicalRecord)
class TechnicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id' , 'player', 'staff' , 'date_created', 'forehand' , 'backhand' , 'serve' , 'volley' , 'movement' , 'listening' , 'has_note']
    search_fields = ['player__name', 'staff__name']

    list_filter = ['staff']

    def has_note(self, obj) -> Boolean:
        return len(obj.note) > 0

    has_note.boolean = True

@admin.register(PhysicalRecord)
class PhysicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id' , 'player', 'staff' , 'stamina' , 'stretching' , 'movement' , 'attention', 'has_note' ,'date_created']
    search_fields = ['player__name', 'staff__name']

    list_filter = ['staff']

    def has_note(self, obj) -> Boolean:
        return len(obj.note) > 0

    has_note.boolean = True