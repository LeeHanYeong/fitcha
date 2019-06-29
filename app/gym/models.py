from django.db import models
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Gym(TimeStampedModel):
    name = models.CharField('이름', max_length=100)
    location = models.CharField('위치', max_length=200, blank=True)
    phone_number = PhoneNumberField('전화번호', blank=True)
    facility_set = models.ManyToManyField('Facility', verbose_name='시설 목록')
    description = models.TextField('설명', blank=True)

    class Meta:
        verbose_name = 'GYM'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class GymImage(TimeStampedModel):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='image_set')
    img = models.ImageField(upload_to='gym')

    class Meta:
        verbose_name = 'GYM 이미지'
        verbose_name_plural = f'{verbose_name} 목록'


class Facility(models.Model):
    name = models.CharField('시설명', max_length=100)

    class Meta:
        verbose_name = '시설'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class Service(models.Model):
    CHOICES_SERVICE = (
        ('pt', 'PT'),
        ('yoga', '요가'),
        ('swimming', '수영'),
        ('golf', '골프'),
        ('pilates', '필라테스'),
        ('tabata', '타바타'),
        ('spinning', '스피닝'),
        ('fitness', '헬스'),
    )
    gym = models.ForeignKey(
        Gym, verbose_name='체육관', on_delete=models.CASCADE,
        related_name='service_set',
    )
    type = models.CharField('유형', choices=CHOICES_SERVICE, max_length=20)
    cost = models.IntegerField('가격')

    class Meta:
        verbose_name = 'GYM 서비스'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.gym.name} | {self.get_type_display()}'
