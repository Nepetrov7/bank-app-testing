Тест-кейс 1: Ввод некорректных значений в баланс счета

Предусловия:
Нет

Шаги для воспроизведения:
1. Открыть страницу сервиса по урлу http://localhost:8000/?balance=-38000

Ожидаемый результат:
Знак минус отсутствует в значении баланса


Тест-кейс 2: Тестирование механизма расчета комиссии

Предусловия:
1. Открыта страница сервиса

Шаги для воспроизведения:
1. Выбрать любой счет
2. Ввести валидный номер карты
3. Ввести сумму перевода 100

Ожидаемый результат:
Комиссия составляет 10


Тест-кейс 3: Проверка валидации номера карты

Предусловия:
1. Открыта страница сервиса

Шаги для воспроизведения:
1. Выбрать любой счет
2. Ввести номер карты 1111 1111 1111 1111
3. Попытаться сделать перевод

Ожидаемый результат:
Выводится сообщение об ошибке, указывающее на недействительный номер карты


Тест-кейс 4: Ввод некорректных данных в виде кириллицы в сумму резерва

Предусловия:
Нет

Шаги для воспроизведения:
1. Открыть страницу сервиса по урлу http://localhost:8000/?reserved=восемьдесят

Ожидаемый результат:
Система отображает числовое значение резерва счета


Тест-кейс 5: Проверка функционала выбора валюты

Предусловия:
1. Открыта страница сервиса

Шаги для воспроизведения:
1. Нажать на кнопку "Доллары" для выбора валюты
2. Ввести номер карты (например, 1234 5678 9012 3456)
3. Ввести сумму для перевода (например, 50)
4. Нажать кнопку "Перевести"

Ожидаемый результат:
В сообщении об успешном переводе указана валюта "$