from django.shortcuts import render, HttpResponse
from .models import ReadingTest, ListeningTest, WritingTest, WritingAnswer, ReadingAnswer, ListeningAnswer
from reading.models import MCQ, yesNoNotGiven, Summary, Fillup, Matching
from reading.models import yesNoNotGivenQues, MCQQues, FillupQue
from listening.models import MCQ as MCQl, Summary as Summaryl, MapMatch as MapMatchl, Fillup as Fillupl, Matching as Matchingl
from listening.models import MCQQues as MCQQuesl, MapMatchQues as MapMatchQuesl, FillupQue as FillupQuel
from writing.models import Writing
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return HttpResponse("WELCOME TO IELTS QUESTION PAPER SECTION")


def ReadingPaper(request):
    if request.method == 'POST':
        student = User.objects.get(username=request.user)
        if request.POST.get('test_name'):
            test_name = request.POST.get('test_name')
            if request.POST.get('ysnid[0]'):
                ysn_id0 = request.POST.get('ysnid[0]')
                ans0 = request.POST.get('ysn[0]')
            if request.POST.get('ysnid[1]'):
                ysn_id1 = request.POST.get('ysnid[1]')
                ans1 = request.POST.get('ysn[1]')
            if request.POST.get('ysnid[2]'):
                ysn_id2 = request.POST.get('ysnid[2]')
                ans2 = request.POST.get('ysn[2]')
            if request.POST.get('ysnid[3]'):
                ysn_id3 = request.POST.get('ysnid[3]')
                ans3 = request.POST.get('ysn[3]')
            if request.POST.get('ysnid[4]'):
                ysn_id4 = request.POST.get('ysnid[4]')
                ans4 = request.POST.get('ysn[4]')
            if request.POST.get('ysnid[5]'):
                ysn_id5 = request.POST.get('ysnid[5]')
                ans5 = request.POST.get('ysn[5]')

            if request.POST.get('sum'):
                sum_id = request.POST.get('sum')
            if request.POST.get('sum0'):
                sum0 = request.POST.get('sum0')
            if request.POST.get('sum1'):
                sum1 = request.POST.get('sum1')
            if request.POST.get('sum2'):
                sum2 = request.POST.get('sum2')
            if request.POST.get('sum3'):
                sum3 = request.POST.get('sum3')
            if request.POST.get('sum4'):
                sum4 = request.POST.get('sum4')
            if request.POST.get('sum5'):
                sum5 = request.POST.get('sum5')

            if request.POST.get('mcq[0]'):
                mcq_id = request.POST.get('mcq[0]')
            if request.POST.get('mcqq[0]'):
                mcq0 = request.POST.get('mcqq[0]')

            if request.POST.get('fillup_id[0]'):
                fillup_id0 = request.POST.get('fillup_id[0]')
            if request.POST.get('fillup[0]'):
                fillup0 = request.POST.get('fillup[0]')
            if request.POST.get('fillup_id[1]'):
                fillup_id1 = request.POST.get('fillup_id[1]')
            if request.POST.get('fillup[1]'):
                fillup1 = request.POST.get('fillup[1]')
            if request.POST.get('fillup_id[2]'):
                fillup_id2 = request.POST.get('fillup_id[2]')
            if request.POST.get('fillup[2]'):
                fillup2 = request.POST.get('fillup[2]')

            if request.POST.get('mat_id'):
                mat_id = request.POST.get('mat_id')
                print(mat_id)
            if request.POST.get('mat0'):
                mat0 = request.POST.get('mat0')
            if request.POST.get('mat1'):
                mat1 = request.POST.get('mat1')
            if request.POST.get('mat2'):
                mat2 = request.POST.get('mat2')
            if request.POST.get('mat3'):
                mat3 = request.POST.get('mat3')

            ReadingAnswer.objects.create(student=student, test_name=test_name, ysn_id0=ysn_id0, ysn0=ans0, ysn_id1=ysn_id1, ysn1=ans1, ysn_id2=ysn_id2, ysn2=ans2, ysn_id3=ysn_id3, ysn3=ans3, ysn_id4=ysn_id4, ysn4=ans4, ysn_id5=ysn_id5, ysn5=ans5,
                                         sum_id=sum_id, sum0=sum0, sum1=sum1, sum2=sum2, sum3=sum3, sum4=sum4, sum5=sum5,
                                         mcq_id=mcq_id, mcq0=mcq0,
                                         fillup_id0 = fillup_id0, fillup_id1 = fillup_id1, fillup_id2 = fillup_id2, fillup0=fillup0, fillup1=fillup1, fillup2=fillup2,
                                         mat_id=mat_id, mat0=mat0, mat1=mat1, mat2=mat2, mat3=mat3,
                                         )
            return HttpResponse("<h4>aubmitted your test</h4>")
    else:
        passage = ReadingTest.objects.all()
        mcq = MCQ.objects.all()
        mcqques = MCQQues.objects.all()
        yesno = yesNoNotGiven.objects.all()
        yesnoques = yesNoNotGivenQues.objects.all()
        summary = Summary.objects.all()
        fillup = Fillup.objects.all()
        fillupques = FillupQue.objects.all()
        matching = Matching.objects.all()
        args = {'passage': passage, 'mcq':mcq, 'mcqques': mcqques, 'yesno':yesno, 'yesnoques':yesnoques,
                'summary': summary, 'fillup': fillup, 'fillupques':fillupques, 'matching': matching}
        return render(request, 'ReadingTest.html', args)



def ListeningPaper(request):
    if request.method == "POST":
        student = User.objects.get(username=request.user)
        if request.POST.get('test_name'):
            test_name = request.POST.get('test_name')


            if request.POST.get('fillup_id[0]'):
                fillup_id0 = request.POST.get('fillup_id[0]')
            if request.POST.get('fillup[0]'):
                fillup0 = request.POST.get('fillup[0]')
            if request.POST.get('fillup_id[1]'):
                fillup_id1 = request.POST.get('fillup_id[1]')
            if request.POST.get('fillup[1]'):
                fillup1 = request.POST.get('fillup[1]')
            if request.POST.get('fillup_id[2]'):
                fillup_id2 = request.POST.get('fillup_id[2]')
            if request.POST.get('fillup[2]'):
                fillup2 = request.POST.get('fillup[2]')
            if request.POST.get('fillup_id[3]'):
                fillup_id3 = request.POST.get('fillup_id[2]')
            if request.POST.get('fillup[3]'):
                fillup3 = request.POST.get('fillup[3]')

            if request.POST.get('mcq[0]'):
                mcq_id = request.POST.get('mcq[0]')
            if request.POST.get('mcqq[0]'):
                mcq0 = request.POST.get('mcqq[0]')


            if request.POST.get('map[0]'):
                map_id0 = request.POST.get('map[0]')
            if request.POST.get('mapp[0]'):
                map0 = request.POST.get('mapp[0]')
            if request.POST.get('map[1]'):
                map_id1 = request.POST.get('map[1]')
            if request.POST.get('mapp[1]'):
                map1 = request.POST.get('mapp[1]')
            if request.POST.get('map[2]'):
                map_id2 = request.POST.get('map[2]')
            if request.POST.get('mapp[2]'):
                map2 = request.POST.get('mapp[2]')


            if request.POST.get('sum'):
                sum_id = request.POST.get('sum')
            if request.POST.get('sum0'):
                sum0 = request.POST.get('sum0')
            if request.POST.get('sum1'):
                sum1 = request.POST.get('sum1')
            if request.POST.get('sum2'):
                sum2 = request.POST.get('sum2')
            if request.POST.get('sum3'):
                sum3 = request.POST.get('sum3')
            if request.POST.get('sum4'):
                sum4 = request.POST.get('sum4')
            if request.POST.get('sum5'):
                print("into")
                sum5 = request.POST.get('sum5')
            else:
                sum5 = ""

            if request.POST.get('mat_id'):
                mat_id = request.POST.get('mat_id')
                print(mat_id)
            if request.POST.get('mat0'):
                mat0 = request.POST.get('mat0')
            if request.POST.get('mat1'):
                mat1 = request.POST.get('mat1')
            if request.POST.get('mat2'):
                mat2 = request.POST.get('mat2')

        ListeningAnswer.objects.create(student=student, test_name=test_name, map_id0=map_id0, map0=map0, map_id1=map_id1, map1=map1,
                                     map_id2=map_id2, map2=map2,
                                     sum_id=sum_id, sum0=sum0, sum1=sum1, sum2=sum2, sum3=sum3, sum4=sum4, sum5=sum5,
                                     mcq_id=mcq_id, mcq0=mcq0,
                                     fillup_id0=fillup_id0, fillup_id1=fillup_id1, fillup_id2=fillup_id2,
                                     fillup0=fillup0, fillup1=fillup1, fillup2=fillup2, fillup_id3=fillup_id3, fillup3=fillup3,
                                     mat_id=mat_id, mat0=mat0, mat1=mat1, mat2=mat2,
                                     )
        return HttpResponse("<h4>aubmitted your test</h4>")
    else:
        audio = ListeningTest.objects.all()
        mcq = MCQl.objects.all()
        mcqques = MCQQuesl.objects.all()
        summary = Summaryl.objects.all()
        fillup = Fillupl.objects.all()
        fillupques = FillupQuel.objects.all()
        matching = Matchingl.objects.all()
        map = MapMatchl.objects.all()
        mapques = MapMatchQuesl.objects.all()
        args = {'audio': audio, 'mcq': mcq, 'mcqques': mcqques, 'map': map, 'mapques': mapques,
                'summary': summary, 'fillup': fillup, 'fillupques': fillupques, 'matching': matching}
        return render(request, 'ListeningTest.html', args)





def WritingPaper(request):
    if request.method == 'POST':
        student = User.objects.get(username=request.user)
        if request.POST.get('xyz'):
            test_name = request.POST.get('test_name')
            ques = request.POST.get('ques')
            ans = request.POST.get('xyz')
            WritingAnswer.objects.create(test_name=test_name, student=student, ques=ques, ans=ans)
            return HttpResponse("<h4>Submitted your test</h4>")
    else:
        writing = WritingTest.objects.all()
        write = Writing.objects.all()
        args = {'write':write, 'writing':writing}
        return render(request, 'WritingTest.html', args)
