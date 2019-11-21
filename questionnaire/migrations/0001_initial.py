# Generated by Django 2.2.7 on 2019-11-21 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5, verbose_name='Has your trip exceeded your expectations')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]