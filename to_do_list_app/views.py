from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, "./index.html", {
        "items": items
    })

def create(request):
    user_input = request.POST["content"]
    if not (user_input == ""):
        new_item = Item(content = user_input)
        new_item.save()
    return HttpResponseRedirect(reverse("to_do_list:index"))

def check(request, item_index):
    checked_item = Item.objects.get(id = item_index)
    checked_item.is_done = True
    checked_item.save()
    return HttpResponseRedirect(reverse("to_do_list:index"))