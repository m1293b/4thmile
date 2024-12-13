from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    """
    Represents a notification in the database.

    Attributes:
        notification_id (int): The unique id of the notification.
        user (User): The user the notification is for.
        message (str): The message of the notification.
        status (str): The status of the notification, e.g. 'read' or 'unread'.
        created_at (datetime): The date and time the notification was created.

    Returns:
        str: A string representation of the notification.
    """
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10)  # e.g., 'read' or 'unread'
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Notification for {self.user.username}'
