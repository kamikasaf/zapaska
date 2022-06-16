from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from apps.user_account.services.signals import post_screate_cart_signal
from django.db.models.signals import post_save
from decouple import config


class CustomUserManager(BaseUserManager):
    def _create(self, email, password, name, last_name, **extra_fields):
        if not email:
            raise ValueError('Email cannot be empty')
        user = self.model(email=email, name=name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, name, last_name, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, name, last_name, **extra_fields)

    def create_superuser(self, email, password, name, last_name, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, name, last_name, **extra_fields)




class CustomUser(AbstractBaseUser):
    use_in_migrations = True

    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj):
        return self.is_staff

    @staticmethod
    def generate_activation_code():
        from django.utils.crypto import get_random_string
        code = get_random_string(8)
        return code 

    def set_activation_code(self):
        code = self.generate_activation_code()
        if CustomUser.objects.filter(activation_code=code).exists():
            self.set_activation_code()
        else:
            self.activation_code = code
            self.save()
    
    def send_activation_email(self):
        activation_url = f"{config('LINK')}/account/activate/{self.activation_code}"
        message = f'''
            You are signed up successfully!
            Activate your account {activation_url}
        '''
        send_mail('Activate your account', message, 'test@mail.com', [self.email, ])
    
    def send_confirm_email(self):
        activation_url = f"{config('LINK')}/account/confirm_email/{self.activation_code}"
        message = f"""
            confirm password change: {activation_url}
        """
        send_mail('Confirm your account', message, 'test@mail.com', [self.email, ])

    



post_save.connect(post_screate_cart_signal, CustomUser)
