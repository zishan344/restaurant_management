
from django.utils import timezone


def validateDate(a,b):
    now = timezone.now().date()
    return a <= now <= b