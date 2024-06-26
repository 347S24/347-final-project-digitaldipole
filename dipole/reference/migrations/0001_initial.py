# Generated by Django 4.2.11 on 2024-03-26 16:22

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atom',
            fields=[
                ('name', models.CharField(help_text='Enter element name', max_length=15, unique=True)),
                ('symbol', models.CharField(help_text='Enter chemical symbol', max_length=3, unique=True)),
                ('std_state', models.CharField(help_text="Enter this element's standard state")),
                ('cpk_hexcolor', models.CharField(help_text='Enter element CPK Hex Color Code', max_length=7)),
                ('atomic_number', models.PositiveIntegerField(help_text='Enter element atomic number', primary_key=True, serialize=False, unique=True)),
                ('e_config', models.CharField(help_text='Enter neutral atom electron configuration', max_length=256)),
                ('atomic_radius', models.FloatField(help_text="Enter this element's atomic radius in picometers")),
                ('ionization_energy', models.FloatField(help_text="Enter this element's first ionization energy")),
                ('atomic_mass', models.FloatField(help_text="Enter this element's atomic mass, in amu")),
                ('electronegativity', models.FloatField(help_text="Enter this element's electronegativity")),
                ('electron_affinity', models.FloatField(help_text="Enter this element's electron affinity")),
                ('melting_point', models.FloatField(help_text="Enter this element's melting point")),
                ('boiling_point', models.FloatField(help_text="Enter this element's boiling point")),
                ('density', models.FloatField(help_text="Enter this element's density")),
                ('oxidation_states', models.CharField(help_text="Enter a comma separated list of this element's common oxidation states")),
                ('year_discovered', models.PositiveIntegerField(help_text='Enter the discovery year')),
                ('group_block', models.CharField(help_text='Enter element classification (ie, group name)')),
            ],
            options={
                'ordering': ['atomic_number'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter unit name', max_length=128)),
                ('symbol', models.CharField(help_text='Enter unit symbol', max_length=32)),
                ('is_SI', models.BooleanField(default=False, help_text='Is this an SI unit?')),
                ('is_Metric', models.BooleanField(default=True, help_text='Does this unit use metric prefixes?')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(help_text='Enter numerical value of measurement')),
                ('precision', models.FloatField(help_text='Enter Number of significant figures')),
                ('unit', models.ForeignKey(help_text='Choose a unit for this measurement', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='reference.unit')),
            ],
        ),
        migrations.AddConstraint(
            model_name='atom',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='genre_name_case_insensitive_unique', violation_error_message='Element already in table'),
        ),
    ]
