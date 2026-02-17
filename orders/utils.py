
from django.utils import timezone
import string, random

def validateDate(a,b):
    now = timezone.now().date()
    return a <= now <= b

def generate_coupon_code(length=10):
    pool = string.ascii_letters+string.digits
    return ''.join(random.choice(pool) for _ in range(length))
