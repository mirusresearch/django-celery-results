# Generated by Django 3.1.2 on 2020-10-05 17:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0008_chordcounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupResult',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    ),
                ),
                (
                    'group_id',
                    models.CharField(
                        db_index=True,
                        help_text='Celery ID for the Group that was run',
                        max_length=getattr(
                            settings,
                            'DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH',
                            255
                        ),
                        unique=True,
                        verbose_name='Group ID',
                    ),
                ),
                (
                    'date_created',
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        help_text='Datetime field when the group result'
                                  ' was created in UTC',
                        verbose_name='Created DateTime',
                    ),
                ),
                (
                    'date_done',
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        help_text=(
                            'Datetime field when the group'
                            'was completed in UTC'
                        ),
                        verbose_name='Completed DateTime',
                    ),
                ),
                (
                    'content_type',
                    models.CharField(
                        help_text='Content type of the result data',
                        max_length=128,
                        verbose_name='Result Content Type',
                    ),
                ),
                (
                    'content_encoding',
                    models.CharField(
                        help_text='The encoding used to save the '
                                  'task result data',
                        max_length=64,
                        verbose_name='Result Encoding',
                    ),
                ),
                (
                    'result',
                    models.TextField(
                        default=None,
                        editable=False,
                        help_text='The data returned by the task. Use '
                        'content_encoding and content_type fields to read.',
                        null=True,
                        verbose_name='Result Data',
                    ),
                ),
            ],
            options={
                'verbose_name': 'group result',
                'verbose_name_plural': 'group results',
                'ordering': ['-date_done'],
            },
        ),
    ]
