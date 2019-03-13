from django.contrib import admin
from .models import AudioMain
from .models import Fillup, Matching, MapMatch, MCQ, Summary
from .models import FillupQue, MapMatchQues, MCQQues
# Register your models here.

admin.site.register(AudioMain)
admin.site.register(Fillup)
admin.site.register(FillupQue)
admin.site.register(Matching)
admin.site.register(MapMatch)
admin.site.register(MapMatchQues)
admin.site.register(MCQ)
admin.site.register(MCQQues)
admin.site.register(Summary)
