# Generated by Django 2.2.2 on 2019-06-29 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_set', to='gym.Gym', verbose_name='헬스장'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_trainer',
            field=models.BooleanField(default=False, verbose_name='트레이너 여부'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='닉네임'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('m', '남성'), ('f', '여성'), ('o', '기타'), ('n', '알리지 않음')], default='', max_length=1, verbose_name='성별'),
            preserve_default=False,
        ),
    ]
