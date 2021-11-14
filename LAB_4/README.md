# **Лабораторна робота №4**

---

## Послідовність виконання лабораторної роботи:

#### 1. Для ознайомляння з `Docker` звернувся до документації.

#### 2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустітив перевірку версії командою `sudo docker -v > my_work.log`, виведення допомоги командою `sudo docker --help >> my_work.log` та тестовий імедж командою `sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log`. Вивід цих команд перенаправляв у файл `my_work.log` та закомітив його до репозиторію.

#### 3. `Docker` працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи `Docker` дещо схожа на віртуальні машини. Спочатку створив імедж з якого буде запускатись контейнер.
#### 4. Для знайомства з `Docker` створив імедж із `Django` сайтом зробленим у попередній роботі.
1. ##### Оскільки мій проект на `Python` то і базовий імедж також потрібно вибрати відповідний. Використовую команду `docker pull python:3.8-slim` щоб завантажити базовий імедж з репозиторію. Переглядаю створеного вміст імеджа командою `docker inspect python:3.8-slim`
    ##### Перевіряю чи добре встановився даний імедж командою:
    
    ```text
    falcon@Makohons-MBP LAB_4 % docker images
    REPOSITORY               TAG        IMAGE ID       CREATED        SIZE
    python                   3.8-slim   214d62795dbb   2 weeks ago    122MB
    docker/getting-started   latest     3ba8f2ff0727   8 months ago   27.9MB
    docker/whalesay          latest     6b362a9f73eb   6 years ago    247MB     
    ```
2. ##### Створив файл з іменем `Dockerfile` та скопіював туди вміс такого ж файлу з репозиторію викладача.
    ###### Вміст файлу `Dockerfile`:
    ```text
    FROM python:3.7-slim
    
    LABEL author="Bohdan"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/BobasB/devops_course.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/devops_course/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
3. ##### Ознайомився із коментарями та зрозумів структуру написання `Dockerfile`.
4. ##### Змінений`Dockerfile` файл:
    ```text
    FROM python:3.8-slim
    
    LABEL author="Makohon"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/IFalcoNI/Pavlo_Makohon_IK_31.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/Pavlo_Makohon_IK_31/LAB_3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
#### 5. Створив власний репозиторій на [Docker Hub](https://hub.docker.com/repository/docker/makohon/lab4). Для цього залогінився у власний аккаунт на `Docker Hub` після чого перейшов у вкладку Repositories і далі натиснув кнопку `Create new repository`.
#### 6. Виконав білд (build) Docker імеджа та завантажтажив його до репозиторію. Для цього я повинен вказати правильну назву репозиторію та TAG. Оскільки мій репозиторій `makohon/lab4` то команда буде виглядати `sudo docker build -t makohon/lab4:django .`, де `django` - це тег.
Команда `docker images`:
```text
falcon@Makohons-MBP LAB_4 % docker images
REPOSITORY               TAG        IMAGE ID       CREATED          SIZE
makohon/lab4             django     33a4589e7964   21 minutes ago   273MB
python                   3.8-slim   214d62795dbb   2 weeks ago      122MB
docker/getting-started   latest     3ba8f2ff0727   8 months ago     27.9MB
docker/whalesay          latest     6b362a9f73eb   6 years ago      247MB
```
Команда для завантаження на власний репозеторій `docker push makohon/lab4:django`.
Посилання на мій [`Docker Hub`](https://hub.docker.com/repository/docker/makohon/lab4) репозиторій та посилання на [`images`](https://hub.docker.com/layers/177287597/makohon/lab4/django/images/sha256-a8401f471dc7a131227686f1288d44066d7a41ebea2975bbda9409aa960e04cc?context=repo).
#### 7. Для запуску веб-сайту виконав команду `sudo docker run -it --name=django --rm -p 8080:8080 makohon/lab4:django`:
```text
falcon@Makohons-MBP LAB_4 % sudo docker run -it --name=django --rm -p 8080:8080 makohon/lab4:django
Warning: Your Pipfile requires python_version 3.10, but you are using 3.8.12 (/root/.local/share/v/a/bin/python).
  $ pipenv --rm and rebuilding the virtual environment may resolve the issue.
  $ pipenv check will surely fail.
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
Run 'python manage.py migrate' to apply them.
November 14, 2021 - 20:44:36
Django version 3.2.9, using settings 'my_site.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
[14/Nov/2021 20:44:59] "GET /favicon.ico HTTP/1.1" 400 60479
[14/Nov/2021 20:45:12] "GET / HTTP/1.1" 200 315

```
Перейшов на адресу http://localhost:8080 та переконався що мій веб-сайт працює:
#### 8. Оскільки веб-сайт готовий і працює, потрібно створит ще один контейнер із програмою моніторингу нашого веб-сайту (Моє Завдання на роботу):
1. ##### Створив ще один Dockerfile з назвою `Dockerfile.site` в якому помістив програму моніторингу.
    Вміст файлу `Dockerfile.site`:
    ```text
    FROM python:3.8-slim
    
    LABEL author="Makohon"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/IFalcoNI/Pavlo_Makohon_IK_31.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/Pavlo_Makohon_IK_31/LAB_3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8080 на зовні
    EXPOSE 8080

    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "monitoring.py", "0.0.0.0:8080"]
    ```
2. ##### Виконав білд даного імеджа та дав йому тег `monitoring` командами:
    ```text
    sudo docker build -f Dockerfile.site -t makohon/lab4:monitoring .
    docker push makohon/lab4:monitoring
    ```
3. ##### Запустив два контейнери одночасно (у різних вкладках) та переконався що програма моніторингу успішно доступається до сторінок мого веб-сайту.
    ##### Використовуючи команди:
    Запуск серевера:
    ```text
    falcon@Makohons-MBP LAB_4 % docker run -it --name=django --rm -p 8000:8000 makohon/lab4:django
    Warning: Your Pipfile requires python_version 3.10, but you are using 3.8.12 (/root/.local/share/v/a/bin/python).
     $ pipenv --rm and rebuilding the virtual environment may resolve the issue.
     $ pipenv check will surely fail.
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    November 14, 2021 - 21:00:43
    Django version 3.2.9, using settings 'my_site.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    [14/Nov/2021 21:01:09] "GET /health HTTP/1.1" 301 0
    [14/Nov/2021 21:01:09] "GET /health/ HTTP/1.1" 200 286
    ```
    Запуск моніторингу:
    ```text
    falcon@Makohons-MBP LAB_4 % docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log makohon/lab4:monitoring
    Warning: Your Pipfile requires python_version 3.10, but you are using 3.8.12 (/root/.local/share/v/a/bin/python).
    $ pipenv --rm and rebuilding the virtual environment may resolve the issue.
    $ pipenv check will surely fail.
    ^CTraceback (most recent call last):
    File "monitoring.py", line 32, in <module>
    time.sleep(60)
    KeyboardInterrupt   
    ```
4. ##### Закомітив `Dockerfile.site` та результати роботи програми моніторингу запущеної з `Docker` контейнера.