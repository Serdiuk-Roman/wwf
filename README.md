# wwf (Wake Wood Flask)

## Base

 - Linux Mint 18.3 Sylvia XFCE
 - Python 3 (3.5.2)
 - Flask, SQLAlchemy, sqlite3, Bootstrap
 - Pycairo

 ## Description

Хочу автоматизувати частину своєї роботи - видача шаблонів на стандартні моделі дверей певних розмірів, в популярних декоративних покриттях.

Приклади заявок, які до мене приходять і які файли я видаю, в печатному вигляді, на виробництво, можна буде побачити на індексній сторінці після запуску проекта.

Для розширення списку можливих декорів - сторінка "Добавить декор".

Поповнення можливих моделей дверей - сторінка "Добавить модель".

На сторінці "Добавить позицию" хочу реалізувати таблицю подібну до тієї, що можна побачити на прикладах заявок із індексної сторінки. Пізніше добавлю кнопку генерувати, щоб таблицю зі списком позицій перводити в pdf сторінки шаблонів, за добопомогою бібліотеки Pycairo. Код для малювання поки що лежить в архіві scetch.zip, те що я реалізував на данний момент в генерації pdf сторінки можна побачити на індексній сторінці в самому низу.

## Install

Створіть робочу папку

    mkdir fla

Перейдіть в неї

    cd fla

Створимо оточення

    python3 -m venv wf

Запустимо його

    source wf/bin/activate

Старт Гіта

    git init

Тягнемо проект
`git pull https://github.com/Serdiuk-Roman/wwf.git`
логін, пароль від Гіта

Встановимо пакети

    pip install -r requirements.txt

Змінні в оточення

    export FLASK_APP=runner.py
    export FLASK_ENV=development

База даних
~~~python3
flask db init
flask db migrate -m "First migrate"
flask db upgrade
~~~

Перший запуск

    flask run

Занесення початкових даних в базу, для цього перейти по силці

    http://127.0.0.1:5000/first_data

Реєструємося, логінимося

Пробуємо добавляти декор, моделі, позиції
