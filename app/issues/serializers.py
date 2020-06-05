from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Issue, Task


class TaskSerializer(serializers.ModelSerializer):
    child_set = RecursiveField(many=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'status',
            'modified',
            'created',
            'child_set',
        )


class IssueSerializer(serializers.ModelSerializer):
    # root_task_set = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = (
            'is_urgent',

            'task_set',
        )

    # def get_root_task_set(self, obj):
    #     # tasks = [task for task in obj.task_set.all() if task.is_root_node()]
    #     tasks = [task for task in obj.task_set.all() if task.parent is None]
    #     return TaskSerializer(tasks, many=True).data
