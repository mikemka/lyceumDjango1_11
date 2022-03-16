from django.http import HttpResponse


def user_list(request):
    return HttpResponse("Список пользователей")


def user_detail(request, user_id):
    return HttpResponse(f"Информация о пользователе {user_id}")


def signup(request):
    return HttpResponse("Регистрация")


def profile(request):
    return HttpResponse("Мой профиль")
