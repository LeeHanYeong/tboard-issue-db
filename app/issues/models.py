from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

__all__ = (
    'Issue',
    'Task',
)


class Issue(models.Model):
    merchant = models.ForeignKey('merchants.Merchant', on_delete=models.CASCADE)
    is_urgent = models.BooleanField(default=False)
    recall_nums = models.PositiveSmallIntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['modified'], name='issue_modified'),
            models.Index(fields=['created'], name='issue_created'),
        ]


class Task(MPTTModel):
    STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_TRANSFERRED, STATUS_COMPLETED, STATUS_CANCELED = (
        '0001_pending', '0010_in_progress', '0100_transferred', '1000_completed', '1100_canceled',
    )
    # 담당자가 없다면 무조건 대기
    CHOICES_STATUS = (
        (STATUS_PENDING, '대기'),
        (STATUS_IN_PROGRESS, '진행중'),
        (STATUS_TRANSFERRED, '이관완료'),
        (STATUS_COMPLETED, '완료'),
        (STATUS_CANCELED, '취소됨'),
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_set')
    status = models.CharField(choices=CHOICES_STATUS, max_length=30)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['status'], name='task_status'),
            models.Index(fields=['modified'], name='task_modified'),
            models.Index(fields=['created'], name='task_created'),
        ]
