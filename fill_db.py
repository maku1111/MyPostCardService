import os
import django

# Setze die Django-Umgebung
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPostCardService.settings')
django.setup()

from Home.models import Paragraph
from django.conf import settings

def fill_database():
    paragraphs = [
        "Welcome to my website. My name is Maximilian Kuehn and I am currently in Malaysia to complete my semester abroad. Malaysia impresses me with its diverse nature, breathtaking landscapes and rich wildlife. The Malaysian rainforest is one of the oldest and richest in species in the world, with endemic plants and animals. Orangutans, tigers, elephants and the world's largest flower, Rafflesia, are just a few of the fascinating species. Underwater, Malaysia also beckons with colorful coral reefs and rich marine diversity. National parks such as Taman Negara, Bako, Kinabalu and Tunku Abdul Rahman Marine Park protect natural habitats and allow visitors to experience the beauty of Malaysian nature firsthand. The country's indigenous peoples have a deep connection to nature and maintain sustainable lifestyles. Malaysia is a paradise for nature lovers who want to explore the diverse wonders of nature and abundant wildlife.",
        "I, as a hobby wildlife photographer, think it's great here and want to give something back. On this website you can therefore send a selection of my own photos free of charge as an electronic postcard by e-mail to your friends. Have fun with it!"
    ]

    for paragraph in paragraphs:
        Paragraph.objects.create(content=paragraph)

if __name__ == '__main__':
    # Holen des Projektnamens aus der settings.py-Datei
    project_name = settings.ROOT_URLCONF.split('.')[0]
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}.settings')
    django.setup()

    fill_database()
