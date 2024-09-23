from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, user_id_tg, **extra_fields):
        """
        Creates and saves a User with the given user_id_tg.
        """
        if not user_id_tg:
            raise ValueError('The user_id_tg must be set')
        
        user = self.model(user_id_tg=user_id_tg, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id_tg, **extra_fields):
        """
        Creates and saves a superuser with the given user_id_tg.
        """
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_id_tg, **extra_fields)


class Users(AbstractBaseUser):
    email = models.CharField(max_length=32, unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = "users"
        