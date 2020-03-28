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

Встановимо пакети

    pip install -r requirements.txt

База даних

    flask db init
    flask db migrate -m "First migrate"
    flask db upgrade

Перший запуск

    export FLASK_APP=runner.py
    export FLASK_ENV=development
    flask run
