from django.db import migrations
from django.contrib.auth.models import Group

def create_groups(apps, schema_editor):
    Group.objects.get_or_create(name='Arrendador')
    Group.objects.get_or_create(name='Arrendatario')

class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0003_alter_usuario_rut'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
    
