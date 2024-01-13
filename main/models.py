from django.db import models


# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)    #if todolist is deleted, all items are to be deleted too
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Note(models.Model):
    notetitle = models.CharField(max_length=100)
    notetext = models.CharField(max_length=100)

    def __str__(self):
        return self.notetitle
