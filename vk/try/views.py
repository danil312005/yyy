from django.shortcuts import render
# Создаём глобальный список для хранения данных
user_inputs = []
def button_page(request):
    if request.method == 'POST':
        # Получаем текст, введённый пользователем
        user_input = request.POST.get('user_input', '')

        # Сохраняем данные в список
        user_inputs.append(user_input)

        # Выводим данные в терминал
        print(f"Новое сообщение от пользователя: {user_input}")

    # Возвращаем ту же страницу
    return render(request, 'try/button_page.html')
