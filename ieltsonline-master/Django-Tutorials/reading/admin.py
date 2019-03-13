from django.contrib import admin
from .models import passageMain
from .models import yesNoNotGiven, Summary, MCQ, Matching, Fillup
from .models import yesNoNotGivenQues, MCQQues, FillupQue

# Register your models here.
admin.site.register(passageMain)
admin.site.register(yesNoNotGiven)
admin.site.register(yesNoNotGivenQues)
admin.site.register(Summary)
admin.site.register(MCQ)
admin.site.register(MCQQues)
admin.site.register(Matching)
admin.site.register(Fillup)
admin.site.register(FillupQue)
