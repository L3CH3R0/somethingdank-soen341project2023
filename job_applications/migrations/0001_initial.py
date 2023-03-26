# Generated by Django 4.1.2 on 2023-03-26 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_portal', '0001_initial'),
        ('job_postings', '0002_alter_jobposting_job_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Selected', 'Selected'), ('Not Selected', 'Not Selected')], default='Pending', max_length=20)),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_postings.jobposting')),
                ('student_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_portal.profile')),
            ],
        ),
    ]
