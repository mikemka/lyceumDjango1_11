from django.http import HttpResponse


def item_list(request):
    return HttpResponse("Список элементов")


def item_detail(request):
    return HttpResponse("Подробно элемент")
