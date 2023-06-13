import os
import django

# Setze die Django-Umgebung
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPostCardService.settings')
django.setup()

from Home.models import Paragraph

def delete_entries():
    # Hole die ersten beiden Einträge
    entries_to_delete = Paragraph.objects.all()
    
    # Lösche die Einträge
    entries_to_delete.delete()

if __name__ == '__main__':
    delete_entries()
