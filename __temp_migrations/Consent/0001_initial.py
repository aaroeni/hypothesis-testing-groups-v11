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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consent_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Consent_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('codes', otree.db.models.LongStringField(null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consent_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Consent_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('GermanMothertongueNiveau', otree.db.models.IntegerField(null=True)),
                ('mobileVersion', otree.db.models.IntegerField(null=True)),
                ('consent', otree.db.models.BooleanField(choices=[[True, 'Ja'], [False, 'Nein, ich beende die Studie jetzt (Dies ist können Sie nicht rückgängig machen)']], null=True)),
                ('consentRefused', otree.db.models.LongStringField(blank=True, null=True)),
                ('priorPB1', otree.db.models.IntegerField(null=True)),
                ('priorPB2', otree.db.models.IntegerField(null=True)),
                ('priorPB3', otree.db.models.IntegerField(null=True)),
                ('certaintyPriorsPB1', otree.db.models.IntegerField(null=True)),
                ('certaintyPriorsPB2', otree.db.models.IntegerField(null=True)),
                ('certaintyPriorsPB3', otree.db.models.IntegerField(null=True)),
                ('berechtigungPriorsHypoPB', otree.db.models.IntegerField(null=True)),
                ('certaintyPriorsHypoPB', otree.db.models.IntegerField(null=True)),
                ('prolificID', otree.db.models.StringField(max_length=10000, null=True)),
                ('groupDecision', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Consent.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consent_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consent_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consent.Subsession')),
            ],
            options={
                'db_table': 'Consent_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consent.Subsession'),
        ),
    ]