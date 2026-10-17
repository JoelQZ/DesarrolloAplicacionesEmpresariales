from django.shortcuts import render

from .models import Item


def item_list(request):
	items = Item.objects.all().order_by("-created_at") 
	return render(request, "core/item_list.html", {"items": items})
