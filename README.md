# wwf (Wake Wood Flask)

## Base



## Install

Створіть робочу папку,

    mkdir fla

Перейдіть в неї,

    cd fla

Створимо оточення

    python3 -m venv wf

Запустимо його

    source wf/bin/activate

Старт Гіта

    git init

Тягнемо пакет

    git pull https://github.com/Serdiuk-Roman/wwf.git
логін, пароль від Гіта

Встановимо пакети

    pip install -r requirements.txt

Змінні в оточення

    export FLASK_APP=runner.py
    export FLASK_ENV=development

База даних

    flask db init
    flask db migrate -m "First migrate"
    flask db upgrade

Перший запуск

    flask run

Занесення початкових даних в базу, для цього перейти по силці

    http://127.0.0.1:5000/first_data

Реєструємося, логінимося

Пробуємо добавляти декор, моделі, позиції
