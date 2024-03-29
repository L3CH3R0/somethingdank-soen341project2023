# Generated by Django 4.1.2 on 2023-03-23 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Volunteer', 'Volunteer'), ('Internship', 'Internship'), ('Other', 'Other')], max_length=255)),
                ('job_category', models.CharField(choices=[('Arts and entertainment', 'Arts and entertainment'), ('Education', 'Education'), ('Technology', 'Technology'), ('Business', 'Business'), ('Healthcare', 'Healthcare'), ('Other', 'Other')], max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('application_deadline', models.DateField()),
                ('contact_info', models.CharField(max_length=255)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
