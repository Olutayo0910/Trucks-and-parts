# migrations/000X_auto_convert_charfield_to_json.py
from django.db import migrations, models
import json

def convert_charfield_to_json(apps, schema_editor):
    SparePart = apps.get_model('core', 'SparePart')
    Equipment = apps.get_model('core', 'Equipment')

    # Convert SparePart details from CharField to JSONField
    for part in SparePart.objects.all():
        if part.details:
            try:
                # Convert string to JSON, handle invalid JSON gracefully
                part.details = json.loads(part.details)
            except json.JSONDecodeError:
                # In case details are not valid JSON, wrap in a dict
                part.details = {"raw": part.details}
            part.save()

    # Convert Equipment details from CharField to JSONField
    for equipment in Equipment.objects.all():
        if equipment.details:
            try:
                # Convert string to JSON, handle invalid JSON gracefully
                equipment.details = json.loads(equipment.details)
            except json.JSONDecodeError:
                # In case details are not valid JSON, wrap in a dict
                equipment.details = {"raw": equipment.details}
            equipment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20240804_0518'),
    ]

    operations = [
        migrations.RunPython(convert_charfield_to_json),
    ]
