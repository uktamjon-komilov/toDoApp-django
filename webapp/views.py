from django.shortcuts import render, redirect
from . import models

# Create your views here.


def listView(request):
    content = {}

    if "list-create" in request.POST:
        newListName = request.POST["list-name"]
        if models.List.objects.filter(title=newListName).exists():
            content["message"] = "List already exists! Try another name."
            content["messageType"] = "danger"
        else:
            newList = models.List(title=newListName)
            newList.save()
            content["message"] = "List has been created successfully!"
            content["messageType"] = "success"

    if "listName" in request.POST:
        listId = request.POST["listid"]
        editedListName = request.POST["listName"]
        models.List.objects.filter(id=listId).update(title=editedListName)
        content["message"] = "List name has been changed!"
        content["messageType"] = "success"

    if "action" in request.GET:
        actionType = request.GET["action"]
        if actionType == "clear":
            if request.GET["type"] == "list":
                listId = request.GET["id"]
                models.Item.objects.filter(
                    type=models.List.objects.get(id=listId)).delete()
        if actionType == "delete":
            if request.GET["type"] == "list":
                listId = request.GET["id"]
                models.List.objects.get(id=listId).delete()

        lists = models.List.objects.all()
        content["lists"] = lists
        return redirect("/")

    lists = models.List.objects.all()
    content["lists"] = lists

    return render(request, 'index.html', content)


def itemsView(request):
    pass


def edit(request):
    if "type" in request.GET:
        listId = request.GET["id"]
        content = {}

        if models.List.objects.filter(id=listId).exists():
            content["listname"] = models.List.objects.filter(
                id=listId).values('title')[0]["title"]
            content["id"] = listId
            return render(request, 'edit.html', content)
        else:
            lists = models.List.objects.all()
            content["lists"] = lists
            content["message"] = "List does not exist!"
            content["messageType"] = "danger"
            return render(request, 'index.html', content)
