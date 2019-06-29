# Generated by Django 2.2.2 on 2019-06-29 18:11

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='시설명')),
            ],
            options={
                'verbose_name': '시설',
                'verbose_name_plural': '시설 목록',
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='위치')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='전화번호')),
                ('description', models.TextField(blank=True, verbose_name='설명')),
                ('facility_set', models.ManyToManyField(to='gym.Facility', verbose_name='시설 목록')),
            ],
            options={
                'verbose_name': 'GYM',
                'verbose_name_plural': 'GYM 목록',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pt', 'PT'), ('yoga', '요가'), ('swimming', '수영'), ('golf', '골프'), ('pilates', '필라테스'), ('tabata', '타바타'), ('spinning', '스피닝'), ('fitness', '헬스')], max_length=20, verbose_name='유형')),
                ('cost', models.IntegerField(verbose_name='가격')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gym_service_set', to='gym.Gym', verbose_name='체육관')),
            ],
            options={
                'verbose_name': 'GYM 서비스',
                'verbose_name_plural': 'GYM 서비스 목록',
            },
        ),
        migrations.CreateModel(
            name='GymImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('img', models.ImageField(upload_to='gym')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='gym.Gym')),
            ],
            options={
                'verbose_name': 'GYM 이미지',
                'verbose_name_plural': 'GYM 이미지 목록',
            },
        ),
    ]