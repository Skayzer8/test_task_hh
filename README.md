# Test task
-------------

## ТЗ:

Вам необходимо создать веб-сервис, который будет выводить "Rekruto! Давай дружить!". 
URL с GET запросом, который будет выводиться уже на странице: урл должен быть таким:
  'xx.xx.xx.xx./?name=Rekruto&message=Давай дружить! и выводиться на странице Hello {name}! {message}!'

-------------

## Исполнитель:

[Skayzer8](https://github.com/Skayzer8)

-------------

##  Технологии
    Python 3.8
    Django 2.2
    dotenv
    Django TestCase 

-------------

## Установка

1. Clone the repository to your PC:
    - git clone git@github.com:Skayzer8/test_task_hh.git
2. Go to the project directory, create and activate VENV:
    - cd test_task_hh
    - python3 -m venv env
    - source venv/bin/activate
3. Install requirements:
    - cd rekruto
    - pip install -r requirements.txt
4. Perform migrations:
    - python3 manage.py migrate
5. run server and enjoy!:
    - python3 manage.py runserver
