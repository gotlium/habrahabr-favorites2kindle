Habrahabr Favorites to Kindle
=============================

Скрипт для отправки избранных пользователем статей на Kindle.
Удобно для офлайн чтения в поездках. Либо в свободное время,
без необходимости ручной отправки с использованием различных
расширений в браузере. Достаточно лишь добавить в избранное,
и статья автоматически синхронизируется с любым устройством,
где установлено приложение Kindle (iOS, Android, Kindle). Так
же остается возможность читать непосредственно на десктопе.


Установка и настройка
---------------------
1. Создайте аккаунт на сайте readability.com
2. Добавьте Kindle Email в настройки аккаунта Readability -> Kindle Settings (для каждого девайса возможно создать email адрес в настройках девайса на Амазоне)
3. Разрешите адрес kindle@readability.com в `настройках <https://www.amazon.com/gp/digital/fiona/manage?ie=UTF8&*Version*=1&*entries*=0&#pdocSettings>`_ Амазона
4. Установите расширение `Readability <https://chrome.google.com/webstore/detail/readability/oknpjjbmpnndlpmnhmekjpocelpnlfdi>`_ для Google Chrome
5. Авторизируйтесь в раширении Readability в браузере
6. Проверьте верность настроек, и попробуйте выслать какую-нибудь статью на Kindle используя установленное расширение
7. Откройте chrome://extensions/ -> Readability -> Фоновая страница -> Network
8. Отправьте тестовую статью на Ваш Kindle, чтобы удостовериться что все настроено верно
9. Скопируйте куки, которые были высланы на /api/session/v1/kindle/send/ и заполните значения словаря COOKIES в settings.py
10. Установите пакеты -> pip install -r requirements.txt (используйте virtualenv)
11. Запустите скрипт отправки избранного -> python main.py
12. Добавьте вызов в cron, для автоматизации процесса -> */10 * * * * flock -n /tmp/hf2k.lock -c "python /path-to-app/main.py"
13. Можно включить DEBUG, если необходимо выводить лог в консоль. В противном случае логи будут в файле habrahabr-favorites2kindle.log


Дополнительно
-------------
Если есть необходимость удалить все данные, это можно сделать на страничке `CloudDrive <https://www.amazon.com/clouddrive/>`_ -> My Send-to-Kindle Docs