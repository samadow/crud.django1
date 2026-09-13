import django.db.models.deletion
from django.db import migrations, models


def save_authors(apps, schema_editor):
    Author = apps.get_model('myapp', 'Author')
    Book = apps.get_model('myapp', 'Book')

    for book in Book.objects.all():
        value = str(book.author).strip()
        author = None

        if value.isdigit():
            author = Author.objects.filter(id=int(value)).first()

        if author is None:
            author = Author.objects.filter(name__iexact=value).first()

        if author is None:
            parts = value.split(maxsplit=1)
            name = parts[0] if parts else 'Unknown'
            last_name = parts[1] if len(parts) > 1 else ''

            if last_name:
                author = Author.objects.filter(
                    name__iexact=name,
                    last_name__iexact=last_name
                ).first()

        if author is None:
            author = Author.objects.create(
                name=name,
                last_name=last_name,
                b_date=0
            )

        book.author_new = author
        book.save(update_fields=['author_new'])


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_new',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='myapp.author',
            ),
        ),
        migrations.RunPython(save_authors, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author_new',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='myapp.author',
            ),
        ),
    ]
