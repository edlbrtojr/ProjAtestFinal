# Generated by Django 5.0.6 on 2024-05-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atestado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=100)),
                ('ano_aluno', models.CharField(choices=[('6', '6º ano'), ('7', '7º ano'), ('8', '8º ano'), ('9', '9º ano')], max_length=50)),
                ('turma_aluno', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('APC', 'Aprender é o caminho')], max_length=50)),
                ('data_atestado', models.DateField()),
                ('dias_afastamento', models.PositiveIntegerField()),
                ('observacoes', models.TextField()),
                ('arquivo', models.FileField(upload_to='atestados/%Y/%m/%d/')),
            ],
        ),
    ]
