from rest_framework import generics
from .models import AnalyticsReport
from .serializers import AnalyticsReportSerializer

class AnalyticsReportListCreateView(generics.ListCreateAPIView):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
