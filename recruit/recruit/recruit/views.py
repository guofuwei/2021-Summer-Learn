import json
from django.db.models.query import RawQuerySet
from student.models import StudentInfo,InterviewInfo
from django.http import JsonResponse
import re
import hashlib,time


def register_view(request):
    # 拿取参数
    if request.method!='POST':
        return JsonResponse({'code':-1,'reason':'非法请求'})
    name=request.POST.get('name')
    sex=request.POST.get('sex')
    classroom=request.POST.get('classroom')
    studentID=request.POST.get('studentID')
    if studentID:
        studentID=studentID.upper()
    phone=request.POST.get('phone')
    QQnumber=request.POST.get('QQnumber')
    email=request.POST.get('email')
    photo=request.FILES.get('photo')
    if photo:
        p=hashlib.md5()
        p.update(str(time.time()).encode('utf-8'))
        photo.name.split('/')[-1]=p.hexdigest()+photo.name.split('.')[-1]
        # print(photo.name)
    learnt_skill=request.POST.get('learnt_skill')
    familiar_skill=request.POST.get('familiar_skill')
    nontech_skill=request.POST.get('nontech_skill')
    orgnization=request.POST.get('orgnization')
    reason=request.POST.get('reason')
    valued=request.POST.get('valued')
    city=request.POST.get('city')

    #检查参数
    if not name or not sex or not classroom or not email or not photo or not learnt_skill or not city\
    or not familiar_skill or not nontech_skill or not orgnization or not reason or not valued:
        return JsonResponse({'code':-1,'reason':'某些字段为空,请重新输入'})
    if not re.match(r'U\d{9}',studentID):
        return JsonResponse({'code':-1,'reason':'学号输入错误,请重新输入'})
    if not re.match(r'\d{11}',phone):
        return JsonResponse({'code':-1,'reason':'手机号输入错误，请重新输入'})
    if not re.match(r'\d{6,15}',QQnumber):
        return JsonResponse({'code':-1,'reason':'QQ输入错误，请重新输入'})
    try:
        StudentInfo.objects.get(studentID=studentID)
        return JsonResponse({'code':-1,'reason':'您已提交，请勿重复提交'})
    except:
        pass
    #存入数据库
    try:
        StudentInfo.objects.create(name=name,
        sex=sex,classroom=classroom,studentID=studentID,
        phone=phone,QQnumber=QQnumber,email=email,photo=photo,
        learnt_skill=learnt_skill,familiar_skill=familiar_skill,
        nontech_skill=nontech_skill,orgnization=orgnization,
        reason=reason,valued=valued,city=city)
    except:
        return JsonResponse({'code':-1,'reason':'提交失败，请再次尝试'})

    return JsonResponse({'code':0,'reason':''})



def query_view(request):
    studentID=request.GET.get('studentID')
    phone=request.GET.get('phone')
    try:
        student=StudentInfo.objects.get(studentID=studentID,phone=phone)
    except Exception as ret:
        print('query error:%s' %ret)
        return JsonResponse({'code':-1,'reason':'查询无结果,请检查学号和手机号'})

    data={
        'code':0,
        'reason':{
            'resume_result':student.is_resume,
            'writeexam_result':student.is_writetest,
            'interview_result':student.is_interview,
        }
    }
    return JsonResponse(data)


def query_detail_view(request):
    if request.method!='GET':
        return JsonResponse({'code':-1,'reason':'非法请求'})

    studentID=request.GET.get('studentID')
    phone=request.GET.get('phone')
    try:
        student=StudentInfo.objects.get(studentID=studentID,phone=phone)
    except:
        return JsonResponse({'code':-1,'reason':'查询无结果,请检查学号和手机号'})

    
    
    data={
        'name':student.name,
        'sex':student.sex,
        'classroom':student.classroom,
        'studentID':student.studentID,
        'phone':phone,
        'QQnumber':student.QQnumber,
        'email':student.email,
        'photo':student.photo.url,
        'learnt_skill':student.learnt_skill,
        'familiar_skill':student.familiar_skill,
        'nontech_skill':student.nontech_skill,
        'orgnization':student.orgnization,
        'reason':student.reason,
        'valued':student.valued,
        'city':student.city,
        # 'is_resume':student.is_resume,
        # 'is_writetest':student.is_writetest,
        # 'write_score':student.write_score,
        # 'write_detail':student.write_detail,
        # 'is_interview':student.is_interview,
    }

    return JsonResponse({'code':0,'reason':data})