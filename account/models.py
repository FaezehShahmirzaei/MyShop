from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator


# Create user.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("user must have email address")
        if not username:
            raise ValueError("user must have username")
        user = self.model(email=self.normalize_email(email), username=username, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Create superuser.
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_path(self, filename):
    return f'./media/profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "./media/profile_images/prof1.png"


class Account(AbstractBaseUser):
    # password = models.CharField(max_length=128)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True,
                                      default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((MALE, 'مرد'), (FEMALE, 'زن'))
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username}"

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'./media/profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True


class State(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, unique=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name},{self.state.name}'


class AccountAddress(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, default=1)
    address = models.CharField(max_length=50, null=False, blank=False)
    postalcode = models.CharField(max_length=12, validators=[
        MinLengthValidator(10, 'the field must contain at least 10 characters')])
    receiver_mobile = models.CharField(max_length=11, validators=[
        MinLengthValidator(10, 'the field must contain at least 10 characters')])
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.postalcode}, {self.city.name},{self.address}'
    #
    # def set_default_address(self):
    #
