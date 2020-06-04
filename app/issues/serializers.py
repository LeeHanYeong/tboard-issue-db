from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Issue, Task
from rest_framework import serializers

from .models import Issue, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'status',
            'modified',
            'created',
        )


class RootTaskSerializer(serializers.ModelSerializer):
    child_set = TaskSerializer(many=True)

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
    root_task_set = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = (
            'root_task_set',
        )

    def get_root_task_set(self, obj):
        tasks = [task for task in obj.task_set.all() if task.parent is None]
        return TaskSerializer(tasks, many=True).data
