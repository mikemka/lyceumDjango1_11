from django.http import HttpResponse


def item_list(request):
    return HttpResponse("Список элементов")


def item_detail(request, prod_id):
    return HttpResponse(f"Подробно элемент {prod_id}")
