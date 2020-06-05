from rest_framework import generics
from .models import Issue, Task
from .serializers import IssueSerializer


class IssueListAPIView(generics.ListAPIView):
    queryset = Issue.objects.select_related(

    ).prefetch_related(
        'task_set',
    )
    serializer_class = IssueSerializer
