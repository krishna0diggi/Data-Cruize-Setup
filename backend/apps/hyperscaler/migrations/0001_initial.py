# Generated by Django 5.2.3 on 2025-07-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('aws', 'Amazon Web Services'), ('azure', 'Microsoft Azure'), ('gcp', 'Google Cloud Platform')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.CharField(blank=True, max_length=100, null=True)),
                ('subscription_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tenant_id', models.CharField(blank=True, max_length=100, null=True)),
                ('client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('client_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('arm_access_key', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cloud_credentials',
            },
        ),
    ]
