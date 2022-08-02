from django.shortcuts import render


def hello_user(request):
    """
    hello_user(): обрабатывает GET передаёт в шаблон hello/main.html 
    имя и сообщенние для пользователя, в случае пустого GET 
    запроса в шаблон отправляются None.
    """
    if request.method == "GET":
        name = request.GET.get('name' or None)
        message = request.GET.get('message' or None)
        content = {
            'name': name,
            'message': message
        }
        return render(request, 'hello/main.html', content)


def server_error(request):
    """Кастомная страница ошибки Internal Server Error."""
    return render(request, 'errors_pages/500.html', status=500)


def page_not_found(request, exception):
    """Кастомная страница ошибки Not Found."""
    return render(request, 'errors_pages/404.html', status=404)
