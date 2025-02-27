from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("trade", "Trade"),
        ("sale", "Sale"),
        ("system", "System"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_notification_type_display()} - {self.message[:20]}"
