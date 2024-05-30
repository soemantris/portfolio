from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, no_hp, password=None):
        if not email:
            raise ValueError('Pengguna harus memiliki alamat email')
        
        user = self.model(
            email=self.normalize_email(email),
            no_hp = no_hp,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, no_hp, password=None):
        user = self.create_user(
            email,
            no_hp=no_hp,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Account(AbstractBaseUser):
    email           = models.EmailField(unique=True)
    nm_lengkap      = models.CharField(max_length=70)
    tmp_lahir       = models.CharField(max_length=70, blank=True)
    tgl_lahir       = models.DateField(null=True, blank=True)
    no_hp           = models.IntegerField(null=True, blank=True)
    alamat          = models.TextField(max_length=300)
    avatar          = models.ImageField(upload_to='akun/', default='akun/akun_default.png', blank=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects         = AccountManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['no_hp',]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True


