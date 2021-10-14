from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager,
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('invalid email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', User.USER)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', User.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER = 'user'
    ADMIN = 'admin'
    ROLE = [
        (USER, 'user'),
        (ADMIN, 'admin'),
    ]

    email = models.EmailField(max_length=254, db_index=True, validators=[validators.validate_email], unique=True, blank=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, choices=ROLE, default=USER, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    post_agreement = models.BooleanField(default=False)
    tin = models.CharField(max_length=12, null=True, blank=True)
    bank_account = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']