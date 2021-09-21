# Generated by Django 2.2 on 2021-09-06 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interviewinfo',
            options={'verbose_name': '面试官评价', 'verbose_name_plural': '面试官评价'},
        ),
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'ordering': ('write_score',), 'verbose_name': '报名表', 'verbose_name_plural': '报名总表'},
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='interview_info',
        ),
        migrations.AddField(
            model_name='interviewinfo',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.StudentInfo'),
        ),
    ]