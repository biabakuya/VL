# Generated by Django 4.2.6 on 2023-12-13 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndk_app', '0002_article_devise'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.CharField(blank=True, choices=[('top-featured', 'Alimentaire'), ('best-seller', 'Médicamenteux')], max_length=255, null=True),
        ),
    ]