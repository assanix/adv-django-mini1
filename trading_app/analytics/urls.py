from django.urls import path
from .views import AnalyticsReportListCreateView

urlpatterns = [
    path("", AnalyticsReportListCreateView.as_view(), name="analytics-list"),
]
