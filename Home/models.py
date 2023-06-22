from django.db import models

# Class for loading text paragraphs from database
# features: content
class Paragraph(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]