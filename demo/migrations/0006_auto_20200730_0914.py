# Generated by Django 3.0.8 on 2020-07-30 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_dataoee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='endRead',
            field=models.IntegerField(null=True, verbose_name='end Read address +1 plc'),
        ),
        migrations.AddField(
            model_name='point',
            name='endWrite',
            field=models.IntegerField(null=True, verbose_name='end Write address +1 plc'),
        ),
        migrations.AddField(
            model_name='point',
            name='startRead',
            field=models.IntegerField(null=True, verbose_name='start  Read address plc'),
        ),
        migrations.AddField(
            model_name='point',
            name='startWrite',
            field=models.IntegerField(null=True, verbose_name='start  Write address plc'),
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name connection')),
                ('ip', models.CharField(max_length=255, verbose_name='ip connection plc')),
                ('rack', models.IntegerField(verbose_name='rack connection plc')),
                ('slot', models.IntegerField(verbose_name='slot connection plc')),
                ('dbRead', models.IntegerField(null=True, verbose_name='db Read number plc')),
                ('startRead', models.IntegerField(null=True, verbose_name='start Read address plc')),
                ('endRead', models.IntegerField(null=True, verbose_name='end Read address +1 plc')),
                ('dbWrite', models.IntegerField(null=True, verbose_name='db Write number plc')),
                ('startWrite', models.IntegerField(null=True, verbose_name='start Write address plc')),
                ('endWrite', models.IntegerField(null=True, verbose_name='end Write address +1 plc')),
                ('whenAdd', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Line')),
            ],
        ),
        migrations.AlterField(
            model_name='point',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Connections'),
        ),
    ]
