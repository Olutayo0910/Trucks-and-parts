from django.db import migrations, models
import json

def convert_charfield_to_json(apps, schema_editor):
    # Get models
    SparePart = apps.get_model('core', 'SparePart')
    Equipment = apps.get_model('core', 'Equipment')

    # Backup the current tables
    schema_editor.execute("ALTER TABLE core_sparepart RENAME TO core_sparepart_backup;")
    schema_editor.execute("ALTER TABLE core_equipment RENAME TO core_equipment_backup;")

    # Create new tables with JSONField
    schema_editor.execute("""
    CREATE TABLE core_sparepart (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        image VARCHAR(100) NOT NULL,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        details TEXT DEFAULT '{}',
        category VARCHAR(50) NOT NULL,
        type VARCHAR(50) NOT NULL,
        price REAL,
        old_price REAL,
        new BOOLEAN NOT NULL
    );
    """)

    schema_editor.execute("""
    CREATE TABLE core_equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        image VARCHAR(100) NOT NULL,
        category VARCHAR(50) NOT NULL,
        type VARCHAR(50) NOT NULL,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        new BOOLEAN NOT NULL,
        details TEXT DEFAULT '{}'
    );
    """)

    # Migrate data from backup tables to new tables with data validation and conversion
    schema_editor.execute("""
    INSERT INTO core_sparepart (id, image, name, description, details, category, type, price, old_price, new)
    SELECT id, image, name, description, 
        CASE 
            WHEN json_valid(details) = 1 THEN details 
            ELSE '{}' 
        END AS details,
        category, type, price, old_price, new 
    FROM core_sparepart_backup;
    """)

    schema_editor.execute("""
    INSERT INTO core_equipment (id, image, category, type, name, description, new, details)
    SELECT id, image, category, type, name, description, new, 
        CASE 
            WHEN json_valid(details) = 1 THEN details 
            ELSE '{}' 
        END AS details
    FROM core_equipment_backup;
    """)

    # Drop the backup tables
    schema_editor.execute("DROP TABLE core_sparepart_backup;")
    schema_editor.execute("DROP TABLE core_equipment_backup;")

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240804_0519'),  # Replace with the name of the last migration before this one
    ]

    operations = [
        migrations.RunPython(convert_charfield_to_json),
    ]
