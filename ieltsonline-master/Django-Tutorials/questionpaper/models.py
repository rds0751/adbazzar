from django.db import models
from reading.models import passageMain
from listening.models import AudioMain
from writing.models import Writing
# Create your models here.

class ReadingTest(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    ques1 = models.ForeignKey(passageMain, related_name="Reading1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(passageMain, related_name="Reading2", on_delete=models.PROTECT)
    ques3 = models.ForeignKey(passageMain, related_name="Reading3", on_delete=models.PROTECT)

    def __str__(self):
        return self.test_name

class ListeningTest(models.Model):
    test_name = models.CharField(max_length=100, default="Listening Test")
    ques1 = models.ForeignKey(AudioMain, related_name="Listening1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(AudioMain, related_name="Listening2", on_delete=models.PROTECT)
    ques3 = models.ForeignKey(AudioMain, related_name="Listening3", on_delete=models.PROTECT)
    ques4 = models.ForeignKey(AudioMain, related_name="Listening4", on_delete=models.PROTECT)

    def __str__(self):
        return  self.test_name


class WritingTest(models.Model):
    test_name = models.CharField(max_length=100, default="Writing Test")
    ques1 = models.ForeignKey(Writing, related_name="Listening1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(Writing, related_name="Listening2", on_delete=models.PROTECT)

    def __str__(self):
        return self.test_name



class WritingAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Writing Test")
    student = models.CharField(max_length=100, null=True)
    ques = models.TextField(max_length=100, null=True)
    ans = models.TextField(max_length=1000000, default="Nothing Wriiten by the Student")
    # ques2 = models.TextField(max_length=1000000, default="Nothing Written")

    def __str__(self):
        return self.student



class ReadingAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    student = models.CharField(max_length=100, null=True)
    ysn_id0 = models.IntegerField(null=True)
    ysn0 = models.CharField(max_length=10, null=True)
    ysn_id1 = models.IntegerField(null=True)
    ysn1 = models.CharField(max_length=10, null=True)
    ysn_id2 = models.IntegerField(null=True)
    ysn2 = models.CharField(max_length=10, null=True)
    ysn_id3 = models.IntegerField(null=True)
    ysn3 = models.CharField(max_length=10, null=True)
    ysn_id4 = models.IntegerField(null=True)
    ysn4 = models.CharField(max_length=10, null=True)
    ysn_id5 = models.IntegerField(null=True)
    ysn5 = models.CharField(max_length=10, null=True)

    sum_id = models.IntegerField(null=True)
    sum0 = models.CharField(max_length=100, null=True)
    sum1 = models.CharField(max_length=100, null=True)
    sum2 = models.CharField(max_length=100, null=True)
    sum3 = models.CharField(max_length=100, null=True)
    sum4 = models.CharField(max_length=100, null=True)
    sum5 = models.CharField(max_length=100, null=True)

    mcq_id = models.IntegerField(null=True)
    mcq0 = models.CharField(max_length=100, null=True)

    fillup_id0 = models.IntegerField(null=True)
    fillup0 = models.CharField(max_length=100, null=True)
    fillup_id1 = models.IntegerField(null=True)
    fillup1 = models.CharField(max_length=100, null=True)
    fillup_id2 = models.IntegerField(null=True)
    fillup2 = models.CharField(max_length=100, null=True)

    mat_id = models.IntegerField(null=True)
    mat0 = models.CharField(max_length=10, null=True)
    mat1 = models.CharField(max_length=10, null=True)
    mat2 = models.CharField(max_length=10, null=True)
    mat3 = models.CharField(max_length=10, null=True)
    mat4 = models.CharField(max_length=10, null=True)
    mat5 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.test_name



class ListeningAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    student = models.CharField(max_length=100, null=True)
    map_id0 = models.IntegerField(null=True)
    map0 = models.CharField(max_length=10, null=True)
    map_id1 = models.IntegerField(null=True)
    map1 = models.CharField(max_length=10, null=True)
    map_id2 = models.IntegerField(null=True)
    map2 = models.CharField(max_length=10, null=True)
    map_id3 = models.IntegerField(null=True)
    map3 = models.CharField(max_length=10, null=True)
    map_id4 = models.IntegerField(null=True)
    map4 = models.CharField(max_length=10, null=True)
    map_id5 = models.IntegerField(null=True)
    map5 = models.CharField(max_length=10, null=True)

    sum_id = models.IntegerField(null=True)
    sum0 = models.CharField(max_length=100, null=True)
    sum1 = models.CharField(max_length=100, null=True)
    sum2 = models.CharField(max_length=100, null=True)
    sum3 = models.CharField(max_length=100, null=True)
    sum4 = models.CharField(max_length=100, null=True)
    sum5 = models.CharField(max_length=100, null=True)

    mcq_id = models.IntegerField(null=True)
    mcq0 = models.CharField(max_length=100, null=True)

    fillup_id0 = models.IntegerField(null=True)
    fillup0 = models.CharField(max_length=100, null=True)
    fillup_id1 = models.IntegerField(null=True)
    fillup1 = models.CharField(max_length=100, null=True)
    fillup_id2 = models.IntegerField(null=True)
    fillup2 = models.CharField(max_length=100, null=True)
    fillup_id3 = models.IntegerField(null=True)
    fillup3 = models.CharField(max_length=100, null=True)

    mat_id = models.IntegerField(null=True)
    mat0 = models.CharField(max_length=10, null=True)
    mat1 = models.CharField(max_length=10, null=True)
    mat2 = models.CharField(max_length=10, null=True)
    mat3 = models.CharField(max_length=10, null=True)
    mat4 = models.CharField(max_length=10, null=True)
    mat5 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.test_name

