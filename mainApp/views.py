from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from sendMailApp.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Welcome!")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Email Sent Boss!")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='sendMailApp.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")