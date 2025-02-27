from celery import shared_task
from .models import AnalyticsReport
import json

@shared_task
def generate_analytics_report(name, data):
    report = AnalyticsReport.objects.create(report_name=name, data=json.loads(data))
    return report.id
