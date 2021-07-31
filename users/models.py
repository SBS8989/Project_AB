from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    CORPORATE_BUSINESS = "법인사업자"
    INDIVIDUAL_BUSINESS = "개인사업자"
    # constant 적어줌

    BUSINESS_CHOICES = (
        (CORPORATE_BUSINESS, "법인사업자"),
        (INDIVIDUAL_BUSINESS, "개인사업자"),
    )

    LANGUAGE_ENGLISH = "English"
    LANGUAGE_KOREAN = "Korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    사업자형태 = models.CharField(choices=BUSINESS_CHOICES, max_length=5, default="")
    사업자등록번호 = models.CharField(max_length=12, default="")
    상담내용 = models.TextField(default="", blank=True)
    생년월일 = models.DateField(blank=True, null=True)
    언어 = models.CharField(choices=LANGUAGE_CHOICES, max_length=8, blank=True)
    통화 = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)


# Model에 form을 적어주면 장고는 form 생성 -> 장고는 migration과 함께 이 form에 필요한 정보를 요청함. 예를 들어 bio 항목을 넣고싶으면 bio = models.TextField(default="") 라고 넣음 하지만 데이터베이스에는 해당 값을 넣을 칸을 만들지 않음. 따라서 makemigration을 통해 필드값을 만들어주고 migrate를 통해 데이터베이스에 넣어줌
# default 대신 null=True를 넣어도 괜찮음. 비어있어도 괜찮아~

# 이미지 필드를 설정하려면 Pillow를 설치해야함 >> pipenv install Pillow

# textfield는 많은 문장, charfield는 한줄
