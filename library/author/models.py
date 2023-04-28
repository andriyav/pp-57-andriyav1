from django.db import models

import book.models


class Author(models.Model):

    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20, null=True)
    books = models.ManyToManyField(book.models.Book, related_name='authors',)
    id = models.AutoField(primary_key=True)

    def __str__(self):

        # return f"\'id\': {self.pk}, \'name\': \'{self.name}\'," \
        #        f" \'surname\': \'{self.surname}\', \'patronymic\': \'{self.patronymic}\'"

        return f"{self.name} {self.surname}"

    def __repr__(self):

        return f"Author(id={self.pk})"

    @staticmethod
    def get_by_id(author_id):

        # return Author.objects.filter(id=author_id)
        # return Author.get_by_id(author_id)
        # return  Author.get_object_or_404()
        try:
            return Author.objects.get(pk=author_id)
        except:
            return None

    @staticmethod
    def delete_by_id(author_id):

        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        if name and len(name) <= 20 and surname and len(surname) <= 20 and patronymic and len(patronymic) <= 20:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        # return self.__dict__

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """

        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()
