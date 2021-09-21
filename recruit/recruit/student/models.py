from django.db import models
from django.contrib import admin
from django.core import mail


class StudentInfo(models.Model):
    name=models.CharField(max_length=11,verbose_name='姓名')
    sex=models.CharField(max_length=5,verbose_name='性别')
    classroom=models.CharField(max_length=11,verbose_name='班级')
    studentID=models.CharField(max_length=20,verbose_name='学号')
    phone=models.CharField(max_length=20,verbose_name='手机')
    QQnumber=models.CharField(max_length=20,verbose_name='QQ号码')
    email=models.EmailField(verbose_name='邮箱')
    photo=models.ImageField(upload_to='photo',null=True)
    learnt_skill=models.CharField(max_length=500,verbose_name='掌握的技术能力')
    familiar_skill=models.CharField(max_length=200,verbose_name='熟练掌握的技术能力')
    nontech_skill=models.CharField(max_length=300,verbose_name='非技术能力')
    orgnization=models.CharField(max_length=100,verbose_name='有意向/已加入的其他学生组织')
    reason=models.CharField(max_length=200,verbose_name='加入科协的理由')
    valued=models.CharField(max_length=200,verbose_name='在科协你最期望收获到的三样东西')
    is_resume=models.NullBooleanField(verbose_name='简历是否审核通过',default=None,blank=True,null=True)
    is_writetest=models.NullBooleanField(verbose_name='笔试是否通过',default=None,blank=True,null=True)
    write_score=models.IntegerField(verbose_name='笔试分数',blank=True,null=True)
    write_detail=models.CharField(max_length=100,verbose_name='笔试详情',blank=True,null=True)
    is_interview=models.NullBooleanField(verbose_name='面试是否通过',default=None,blank=True,null=True)
    city=models.CharField(max_length=30,verbose_name='城市',default=None)

    class Meta:
        ordering = ('write_score',)
        verbose_name = "报名表"
        verbose_name_plural = "报名总表"

    def __str__(self):
        return self.name


class InterviewInfo(models.Model):
    interviewer=models.CharField(max_length=11,verbose_name='面试官姓名')
    evaluate=models.CharField(max_length=100,verbose_name='评价')
    student = models.ForeignKey(StudentInfo,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return str("评价人："+self.interviewer+" 考生："+self.student.name)

    class Meta:
        verbose_name = "面试官评价"
        verbose_name_plural = "面试官评价"


class interview_inline(admin.TabularInline):
    model = InterviewInfo

class student_admin(admin.ModelAdmin):
    inlines = [interview_inline]
    list_display=['name','sex','is_resume','write_score','is_writetest','is_interview']
    list_editable=['is_resume','write_score','is_writetest','is_interview']
    list_filter = ['is_resume','is_writetest','is_interview']
    actions = ['resume_pass','resume_fail','write_pass','write_fail','interview_pass','interview_fail',
    'email_resume_pass','email_resume_fail','email_write_pass','email_write_fail',
    'email_interview_pass','email_interview_fail']

    def resume_pass(self,request,queryset):
        queryset.update(is_resume=True)
    resume_pass.short_description = '简历批量通过'

    def resume_fail(self,request,queryset):
        queryset.update(is_resume=False)
    resume_fail.short_description = '简历批量淘汰'

    def write_pass(self,request,queryset):
        queryset.update(is_writetest=True)
    write_pass.short_description = '笔试批量通过'

    def write_fail(self,request,queryset):
        queryset.update(is_writetest=False)
    write_fail.short_description = '笔试批量淘汰'

    def interview_pass(self,request,queryset):
        queryset.update(is_interview=True)
    interview_pass.short_description = '面试批量通过'

    def interview_fail(self,request,queryset):
        queryset.update(is_interview=False)
    interview_fail.short_description = '面试批量淘汰'




    def email_resume_pass(self,request,queryset):
        emails=queryset.filter(is_resume=True).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        # recipient_list.append('3555970235@qq.com')
        # print(recipient_list)
        mail.send_mail(subject='2021电信科协秋招简历审核结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_resume_pass.short_description = '简历通过--邮件发送'

    def email_resume_fail(self,request,queryset):
        emails=queryset.filter(is_resume=False).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        mail.send_mail(subject='2021电信科协秋招简历审核结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_resume_fail.short_description = '简历淘汰--邮件发送'

    def email_write_pass(self,request,queryset):
        emails=queryset.filter(is_writetest=True).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        mail.send_mail(subject='2021电信科协秋招笔试结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_write_pass.short_description = '笔试通过--邮件发送'

    def email_write_fail(self,request,queryset):
        emails=queryset.filter(is_writetest=False).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        mail.send_mail(subject='2021电信科协秋招笔试结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_write_fail.short_description = '笔试淘汰--邮件发送'

    def email_interview_pass(self,request,queryset):
        emails=queryset.filter(is_interview=True).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        mail.send_mail(subject='2021电信科协秋招面试结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_interview_pass.short_description = '面试通过--邮件发送'

    def email_interview_fail(self,request,queryset):
        emails=queryset.filter(is_interview=False).values('email')
        recipient_list=list()
        for email in emails:
            recipient_list.append(email['email'])
        mail.send_mail(subject='2021电信科协秋招面试结果',message='----test----',from_email='2625406970@qq.com',
        recipient_list=recipient_list)
    email_interview_fail.short_description = '面试淘汰--邮件发送'
