from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# . : 같은 폴더 내 models를 불러오는거

# Register your models here.

# 반드시 아래 데코레이터 밑에다가  써야함
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",  # 대분류
            {
                "fields": (
                    "사업자형태",
                    "사업자등록번호",
                )
            },
        ),
        (
            "Other Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "상담내용",
                    "생년월일",
                    "언어",
                    "통화",
                    "superhost",
                )
            },
        ),
    )

    # list_display = ("username", "gender", "사업자형태", "사업자등록번호", "언어", "통화", "superhost")
    # list_filter = ("사업자형태", "superhost")


# admin패널에서 이 user을 보고 싶어!

# user을 컨트롤한 클래스가 바로 이게 될거야
# decorator은 이렇게 클래스 위에 있어야 작동

# admin.site.register(models.User, CustomUserAdmin)

# Fieldset을 꾸리기 (파랑 창)
