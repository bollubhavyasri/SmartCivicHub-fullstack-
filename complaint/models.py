from django.db import models
from django.contrib.auth.models import User

# Organization Model
class Organization(models.Model):
    name = models.CharField(max_length=200)
    org_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# User Profile Model
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username


# Complaint Model
class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('road', 'Road'),
        ('sanitation', 'Sanitation'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title