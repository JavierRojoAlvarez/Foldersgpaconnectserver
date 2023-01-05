# Generated by Django 3.1.5 on 2021-04-08 15:10

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import invoice.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_delete_invoice'),
        ('invoice', '0004_auto_20210407_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivedinvoice',
            name='number',
            field=models.CharField(default='', max_length=50, verbose_name='Invoice Number'),
        ),
        migrations.CreateModel(
            name='IssuedInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('number', models.CharField(default='', max_length=50, verbose_name='Invoice Number')),
                ('date_issued', models.DateField(verbose_name='Date Issued')),
                ('pdf', models.FileField(upload_to='issued-invoices/', validators=[invoice.validators.validate_is_pdf], verbose_name='PDF File')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Paid by customer')),
                ('associated_payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='my_app.contractpayment', verbose_name='Associated Payment')),
            ],
            options={
                'verbose_name_plural': 'Issued Invoices',
            },
        ),
    ]
