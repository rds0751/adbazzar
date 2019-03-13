from django.contrib import admin
from . models import ReadingTest, ListeningTest, WritingTest, WritingAnswer, ReadingAnswer, ListeningAnswer


# Register your models here.
admin.site.register(ReadingTest)
admin.site.register(ListeningTest)
admin.site.register(WritingTest)
admin.site.register(WritingAnswer)
admin.site.register(ReadingAnswer)
admin.site.register(ListeningAnswer)
