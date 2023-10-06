
from django.db import models





# # register/models.py
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, name, nid, email, password=None):
#         if not email:
#             raise ValueError('The Email field must be set')
#         if not nid:
#             raise ValueError('The NID field must be set')

#         email = self.normalize_email(email)
#         user = self.model(email=email, nid=nid, name=name)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, name, nid, email, password=None):
#         user = self.create_user(name, nid, email, password=password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser):
#     name = models.CharField(max_length=100)
#     nid = models.CharField(max_length=20, unique=True)
#     email = models.EmailField(unique=True)
#     # Add other fields as needed
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'nid'
#     REQUIRED_FIELDS = ['name', 'email']

#     def __str__(self):
#         return self.email
    


    
