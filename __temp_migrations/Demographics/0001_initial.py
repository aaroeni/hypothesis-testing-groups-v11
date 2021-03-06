# Generated by Django 2.2.12 on 2020-11-16 14:20

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demographics_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Demographics_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demographics_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Demographics_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('age', otree.db.models.IntegerField(null=True)),
                ('gender', otree.db.models.IntegerField(blank=True, null=True)),
                ('education', otree.db.models.IntegerField(null=True)),
                ('subject', otree.db.models.StringField(max_length=10000, null=True)),
                ('politicalOrientation', otree.db.models.IntegerField(default=0, null=True)),
                ('executiveSelf', otree.db.models.IntegerField(null=True)),
                ('executiveOther', otree.db.models.IntegerField(null=True)),
                ('violentProtester', otree.db.models.IntegerField(null=True)),
                ('contactPoliceBrutality', otree.db.models.IntegerField(null=True)),
                ('GermanMuttersprache', otree.db.models.IntegerField(null=True)),
                ('GermanFluency', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Demographics.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demographics_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demographics_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demographics.Subsession')),
            ],
            options={
                'db_table': 'Demographics_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demographics.Subsession'),
        ),
    ]
