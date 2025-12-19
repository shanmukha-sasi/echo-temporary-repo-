from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        # We don't ask for username, but we must provide one to the model
        # We temporary set it to the email prefix, or let the model .save() handle it
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('employee', 'Employee'),
    )
    
    # 1. We removed "username = None". 
    # 2. Instead, we overwrite it to be "blank=True". 
    #    This means "Forms/Admin, don't demand this from the user."
    username = models.CharField(max_length=150, unique=True, blank=True)
    
    email = models.EmailField(unique=True) 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # We don't ask for username in the command line either

    objects = CustomUserManager()

    # THIS IS THE MAGIC PART
    def save(self, *args, **kwargs):
        # If the username is missing...
        if not self.username:
            # Take the email (e.g., sasi@gmail.com)
            # Split it at '@' -> ['sasi', 'gmail.com']
            # Take the first part -> 'sasi'
            base_username = self.email.split('@')[0]
            
            # (Optional) Simple uniqueness logic: 
            # In a real app, you might need to check if 'sasi' already exists and add numbers.
            # For now, we trust the email prefix is enough.
            self.username = base_username
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email