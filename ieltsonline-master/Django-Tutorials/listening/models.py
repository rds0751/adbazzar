from django.db import models

# Create your models here.

########################## MAIN QUESTION ########################################
class AudioMain(models.Model):
    Question_Name = models.CharField(max_length=50, default="Listening Part")
    Instruction = models.TextField(max_length=2000, default="instructions")
    audio_file = models.FileField(upload_to='audiofolder/',
                                  help_text=("Allowed type - .mp3, .wav, .ogg"), null=True)

    def __str__(self):
        return self.Question_Name


########################## SUB QUESTIONS ######################################

########################### Summary Fillup types #####################################
class Summary(models.Model):
    audio = models.ForeignKey(AudioMain, related_name="audiosumm", null=True, on_delete=models.PROTECT)
    Question_Name = models.CharField(max_length=50, default="audio Question")
    Instruction = models.TextField(max_length=2000, default="your instructions")
    part1 = models.CharField(max_length=100, null=True)
    part2 = models.CharField(max_length=100, null=True)
    part3 = models.CharField(max_length=100, blank=True, null=True)
    part4 = models.CharField(max_length=100, blank=True, null=True)
    part5 = models.CharField(max_length=100, blank=True, null=True)
    part6 = models.CharField(max_length=100, blank=True, null=True)
    part7 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Question_Name


############################ MCQs ##########################################
class MCQ(models.Model):
    audio = models.ForeignKey(AudioMain, related_name="audiomcq", null=True, on_delete=models.PROTECT)
    Question_Name = models.CharField(max_length=50, default="MCQ Question")
    Instruction = models.TextField(max_length=2000, default="your instructions")

    def __str__(self):
        return self.Question_Name


class MCQQues(models.Model):
    linked = models.ForeignKey(MCQ, related_name="linkedmcq", null=True, on_delete=models.PROTECT)
    Question = models.TextField(max_length=100, default="Your questions")
    option1 = models.CharField(max_length=100, null=True)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    option5 = models.CharField(max_length=100, blank=True, null=True)
    option6 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.linked.Question_Name


########################## MATACH DRAG AND DROP ##########################################
class Matching(models.Model):
    audio = models.ForeignKey(AudioMain, related_name="audioMatch", null=True, on_delete=models.PROTECT)
    Question_Name = models.CharField(max_length=50, default="Matching Question")
    Instruction = models.TextField(max_length=2000, default="your instructions")
    l1 = models.CharField(max_length=100, null=True)
    l2 = models.CharField(max_length=100, null=True)
    l3 = models.CharField(max_length=100, blank=True, null=True)
    l4 = models.CharField(max_length=100, blank=True, null=True)
    l5 = models.CharField(max_length=100, blank=True, null=True)
    l6 = models.CharField(max_length=100, blank=True, null=True)
    l7 = models.CharField(max_length=100, blank=True, null=True)
    l8 = models.CharField(max_length=100, blank=True, null=True)
    l9 = models.CharField(max_length=100, blank=True, null=True)
    l10 = models.CharField(max_length=100, blank=True, null=True)
    r1 = models.CharField(max_length=100, null=True)
    r2 = models.CharField(max_length=100, null=True)
    r3 = models.CharField(max_length=100, blank=True, null=True)
    r4 = models.CharField(max_length=100, blank=True, null=True)
    r5 = models.CharField(max_length=100, blank=True, null=True)
    r6 = models.CharField(max_length=100, blank=True, null=True)
    r7 = models.CharField(max_length=100, blank=True, null=True)
    r8 = models.CharField(max_length=100, blank=True, null=True)
    r9 = models.CharField(max_length=100, blank=True, null=True)
    r10 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Question_Name


############################## Fillups ###############################################
class Fillup(models.Model):
    audio = models.ForeignKey(AudioMain, related_name="audioFill", null=True, on_delete=models.PROTECT)
    Question_Name = models.CharField(max_length=50, default="Fillup Question")
    Instruction = models.TextField(max_length=2000, default="your instructions")
    Question = models.TextField(max_length=100, default="Your questions")

    def __str__(self):
        return self.Question_Name

class FillupQue(models.Model):
    linked = models.ForeignKey(Fillup, related_name="linkedfillup", null=True, on_delete=models.PROTECT)
    part1 = models.CharField(max_length=100, null=True)
    part2 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.linked.Question_Name


###########################Map Matching##################################
class MapMatch(models.Model):
    audio = models.ForeignKey(AudioMain, related_name="audioMap", null=True, on_delete=models.PROTECT)
    map = models.ImageField(upload_to='audiomap/', null=True)
    Question_Name = models.CharField(max_length=50, default="Map Question")
    Instruction = models.TextField(max_length=2000, default="your instructions")
    Question = models.TextField(max_length=100, default="Your questions")

    def __str__(self):
        return self.Question_Name

class MapMatchQues(models.Model):
    linked = models.ForeignKey(MapMatch, related_name="linkedmap", null=True, on_delete=models.PROTECT)
    part = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.linked.Question_Name
