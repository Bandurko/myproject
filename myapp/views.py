from django.shortcuts import render

# Create your views here.

import logging
from django.http import HttpResponse, HttpRequest


logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная</title>
</head>
<body>
    <p><h1>Это мой первый сайт на Django.</h1></p>
    <p><a href="https://bandurko2gb.pythonanywhere.com/about/">Обо мне.</a></p>
    <p></p>
</body>
</html>
"""
    logger.info('Index page requested.')

    return HttpResponse(html)


def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Обо мне</title>
</head>
<body>
    <p><h1>Эта страница обо мне.</h1></p>
    <h3>Меня зовут Бандурко Сергей.<br>
    Я живу во Владивостоке.</h3>
    <p>
</body>
</html>
"""
    logger.info('About page requested.')

    return HttpResponse(html)