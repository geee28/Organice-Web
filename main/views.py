from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Note
from .forms import CreateNewList, CreateNewNote


# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def viewlist(response, id):
    ls = ToDoList.objects.get(id=id)
    # {"save" : ["save"], "c1":["clicked"], ...}
    if response.method == "POST":
        print(response.POST)

        if response.POST.get("deletelist" + str(ls.id)) == "deletelist":
            ls.delete()
            ls = ToDoList.objects.all()
            return HttpResponseRedirect("/viewalllists/", {"ls": ls})

        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.text = response.POST.get("item-text" + str(item.id))
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")

        for item in ls.item_set.all():
            if response.POST.get("d" + str(item.id)) == "deleted":
                print("Deleted item:", item.text, item.id)
                item.delete()
                ls.save()

    return render(response, "main/viewlist.html", {"ls": ls})


def createlist(response):
    if response.method == "POST":  # Python's syntax use "POST" only
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/list%i/" % t.id)

    else:
        form = CreateNewList()

    return render(response, "main/createlist.html", {"form": form})


def createnote(response):
    if response.method == "POST":  # Python's syntax use "POST" only
        # print("\n\n\nBefore CreateNewNote form")
        form = CreateNewNote(response.POST)
        # print("\n\n\nAfter CreateNewNote form")
        # print("Printing form",response.POST, form)

        if form.is_valid():
            nt = form.cleaned_data["notetitle"]
            t = Note(notetitle=nt, notetext="Enter note text here")
            t.save()
            # print("T SAVED")

        return HttpResponseRedirect("/note%i/" % t.id)

    else:
        # print("GET METHOD")
        form = CreateNewNote()

    return render(response, "main/createnote.html", {"form": form})


def viewnote(response, nid):
    nobj = Note.objects.get(id=nid)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            nobj.notetext = response.POST.get("note-text" + str(nobj.id))
            nobj.save()

        if response.POST.get("d" + str(nobj.id)) == "deleted":
            print("Deleted item:", nobj.notetext)
            nobj.delete()
            return HttpResponseRedirect("/viewallnotes/")

    return render(response, "main/viewnote.html", {"nobj": nobj})


def viewalllists(response):
    tobj = ToDoList.objects.all()
    return render(response, "main/viewalllists.html", {"tobj": tobj})


def viewallnotes(response):
    nobj = Note.objects.all()
    return render(response, "main/viewallnotes.html", {"nobj": nobj})
