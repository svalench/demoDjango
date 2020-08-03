# Generated by Django 3.0.8 on 2020-07-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20200730_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='childModel',
            field=models.CharField(choices=[('real', 'Real type variable'), ('int', 'Int type variable'), ('dint', 'Double type variable'), ('bool', 'Boolean variable'), ('q', 'quit boolean variable'), ('i', 'input boolean variable'), ('m', 'Memory boolean variable'), ('oee', 'Data OEE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='endRead',
            field=models.IntegerField(null=True, verbose_name='end Read address +1 plc (for bit set 0)'),
        ),
        migrations.AlterField(
            model_name='point',
            name='startRead',
            field=models.IntegerField(null=True, verbose_name='start  Read address plc (for bit set bit number)'),
        ),
    ]
