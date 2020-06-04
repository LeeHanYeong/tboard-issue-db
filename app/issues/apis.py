from rest_framework import generics
from .models import Issue, Task
from .serializers import IssueSerializer


class IssueListAPIView(generics.ListAPIView):
    queryset = Issue.objects.select_related(

    ).prefetch_related(
        'task_set',
        'task_set__child_set',
        'task_set__parent',
    )
    serializer_class = IssueSerializer

    def get_queryset(self):
        filter_dict = {}
        status = self.request.query_params.get('status')
        if status:
            filter_dict['a']
        return self.queryset.filter(

        )