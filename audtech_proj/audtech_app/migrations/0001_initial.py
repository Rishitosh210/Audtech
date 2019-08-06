# Generated by Django 2.2.3 on 2019-08-04 03:52

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('post_code', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('web_address', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('phone_no', models.CharField(max_length=50, null=True, verbose_name='Contact Number')),
                ('logo', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Rishitosh Guha\\PycharmProjects\\AY\\audtech_proj\\media'), upload_to='')),
            ],
            options={
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('company_type', models.CharField(blank=True, max_length=60, null=True)),
                ('engagement_name', models.CharField(blank=True, max_length=90, null=True)),
                ('Currency', models.CharField(blank=True, max_length=50, null=True, verbose_name='Entity Currency')),
                ('financial_management_system', models.CharField(blank=True, max_length=90, null=True, verbose_name='System Name')),
                ('fiscal_start_month', models.DateField(blank=True, null=True, verbose_name='Fiscal Start Date')),
                ('fiscal_end_month', models.DateField(blank=True, null=True, verbose_name='Fiscal End Date')),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'permissions': (('create_eng ', 'Create Engagement'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FinalTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=1000000, null=True)),
                ('engangement', models.CharField(blank=True, max_length=1000000, null=True)),
                ('user_id', models.CharField(blank=True, max_length=1000000, null=True)),
                ('Upload_Date', models.DateField(blank=True, null=True)),
                ('SrNo', models.CharField(blank=True, max_length=50, null=True)),
                ('JournalDate', models.DateTimeField(blank=True, null=True)),
                ('JournalNumber', models.CharField(blank=True, max_length=1000000, null=True)),
                ('JournalType', models.CharField(blank=True, max_length=1000000, null=True)),
                ('DivisionCode', models.CharField(blank=True, max_length=1000000, null=True)),
                ('StatusPostedUnposted', models.CharField(blank=True, max_length=1000000, null=True)),
                ('PostingDate', models.DateTimeField(blank=True, null=True, verbose_name='Posting Date')),
                ('TransactionType', models.CharField(blank=True, max_length=1000000, null=True)),
                ('ReferenceNo', models.CharField(blank=True, max_length=1000000, null=True)),
                ('AccountCategory', models.CharField(blank=True, max_length=1000000, null=True)),
                ('MainAccountCode', models.CharField(blank=True, max_length=1000000, null=True)),
                ('MainAccountName', models.CharField(blank=True, max_length=1000000, null=True)),
                ('SubAccountCode', models.CharField(blank=True, max_length=1000000, null=True)),
                ('SubAccountName', models.CharField(blank=True, max_length=1000000, null=True)),
                ('Year', models.CharField(blank=True, max_length=1000000, null=True)),
                ('GroupName', models.CharField(blank=True, max_length=1000000, null=True)),
                ('ShortText', models.TextField(blank=True, null=True)),
                ('TaxReference', models.CharField(blank=True, max_length=1000000, null=True)),
                ('Splitbetweenheads', models.CharField(blank=True, max_length=1000000, null=True)),
                ('CreatedBy', models.CharField(blank=True, max_length=1000000, null=True)),
                ('AuthorisedBy', models.CharField(blank=True, max_length=1000000, null=True)),
                ('CurrencyCode', models.CharField(blank=True, max_length=1000000, null=True)),
                ('DebitAmount', models.FloatField(blank=True, null=True)),
                ('CreditAmount', models.FloatField(blank=True, null=True)),
                ('DebitAmountFC', models.FloatField(blank=True, null=True)),
                ('CreditAmountFC', models.FloatField(blank=True, null=True)),
                ('DocumentHeaderText', models.CharField(blank=True, max_length=1000000, null=True)),
                ('EntityCode', models.CharField(blank=True, max_length=1000000, null=True)),
            ],
            options={
                'permissions': (('is_analytics', 'Analytics'), ('is_read', 'Only read'), ('is_import', 'Import Data')),
            },
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng', models.CharField(blank=True, max_length=50, null=True)),
                ('client', models.CharField(blank=True, max_length=200, null=True, verbose_name='Financial System')),
                ('transaction_type', models.CharField(blank=True, max_length=200, null=True)),
                ('final_field', models.CharField(blank=True, max_length=200, null=True, verbose_name='Audtech Field')),
                ('source_filed', models.CharField(blank=True, max_length=200, null=True, verbose_name='System Field')),
                ('column_no', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': True,
                'default_permissions': (),
            },
        ),
    ]
