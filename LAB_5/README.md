# **Лабораторна робота №5**

---

## Послідовність виконання лабораторної роботи:

#### 1. Для ознайомляння з `docker-compose` звернувся до документації.

Щоб встановити `docker-compose` використав команди:

```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 2. Ознайомився з бібліотекою `Flask`, яку найчастіше використовують для створення простих веб-сайтів на Python.

#### 3. Завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами. Зроблю я це двома методами:

- за допомогою `Makefile`;
- за допомогою `docker-compose.yaml`.

#### 4. Першим розгляну метод з `Makefile`, але спочатку створю робочий проект.

#### 5. Створив папку `my_app` в якій буде знаходитись мій проект. Створив папку `tests` де будуть тести на перевірку працездатності мого проекту. Скопіював файли `my_app/templates/index.html`, `my_app/app.py `, `my_app/requirements.txt`, `tests/conftest.py`, `tests/requirements.txt`, `tests/test_app.py` з репозиторію викладача у відповідні папки мого репозеторію. Ознайомився із вмістом кожного з файлів. Звернув увагу на файл requirements.txt у папці проекту та тестах. Даний файл буде мітити залежності для мого проекту він містить назви бібліотек які імпортуються.

#### 6. Я спробував чи проект є працездатним перейшовши у папку `my_app` та після ініціалізації середовища виконав команди записані нижче:

```text
sudo pipenv --python 3.8
sudo pipenv install -r requirements.txt
sudo pipenv run python app.py
```

1. Так само я ініціалузував середовище для тестів у іншій вкладці шелу та запустив їх командою `sudo pipenv run pytest test_app.py --url http://localhost:5000` але спочатку треба перейти в папку `tests`:

````text
falcon@Makohons-MBP tests % sudo pipenv run pytest test_app.py --url http://localhost:5000
Warning: Your Pipfile requires python_version 3.10, but you are using 3.8.2 (/Users/falcon/.local/share/v/t/bin/python).
 $ pipenv --rm and rebuilding the virtual environment may resolve the issue.
 $ pipenv check will surely fail.
======================================================================== test session starts ========================================================================
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/falcon/Desktop/Projects/Pavlo_Makohon_IK_31/LAB_5/tests
collected 4 items

test_app.py F.FF                                                                                                                                              [100%]

============================================================================= FAILURES ==============================================================================
______________________________________________________________________ test_default_urls_check ______________________________________________________________________

url = 'http://localhost:5000'

   def test_default_urls_check(url):
       hits = requests.get(url + '/hits')
>       assert len(hits.text) > 0, 'Main page is empty'
E       AssertionError: Main page is empty
E       assert 0 > 0
E        +  where 0 = len('')
E        +    where '' = <Response [403]>.text

test_app.py:15: AssertionError
_____________________________________________________________________________ test_logs _____________________________________________________________________________

url = 'http://localhost:5000'

   def test_logs(url):
       response = requests.get(url + '/logs')
>       assert 'My Hostname is:' in response.text, 'Logs do not have Hostname'
E       AssertionError: Logs do not have Hostname
E       assert 'My Hostname is:' in ''
E        +  where '' = <Response [403]>.text

test_app.py:27: AssertionError
__________________________________________________________________________ test_main_page ___________________________________________________________________________

url = 'http://localhost:5000'

   def test_main_page(url):
       response = requests.get(url)
>       assert 'You are at main page.' in response.text, 'Main page without text'
E       AssertionError: Main page without text
E       assert 'You are at main page.' in ''
E        +  where '' = <Response [403]>.text

test_app.py:32: AssertionError
====================================================================== short test summary info ======================================================================
FAILED test_app.py::test_default_urls_check - AssertionError: Main page is empty
FAILED test_app.py::test_logs - AssertionError: Logs do not have Hostname
FAILED test_app.py::test_main_page - AssertionError: Main page without text
==================================================================== 3 failed, 1 passed in 0.20s ====================================================================
falcon@Makohons-MBP tests %
   ```
2. Звернув увагу, що в мене автоматично створюються файли `Pipfile` та `Pipfile.lock`, а також на хост машині буде створена папка `.venv`. Після зупинки проекту видалив їх.
3. Перевірив роботу сайту перейшовши головну сторінку. Сайт не працює бо на відсутній `redis`.
![Screen](https://github.com/IFalcoNI/Pavlo_Makohon_IK_31/tree/master/LAB_5/redis_exeption.png)

#### 7. Видалив файли які постворювались після тестового запуску. Щоб моє середовище було чистим, все буде створюватись і виконуватись всередині Docker. Створив два файла `Dockerfile.app`, `Dockerfile.tests` та `Makefile` який допоможе автоматизувати процес розгортання.
#### 8. Скопіював вміст файлів `Dockerfile.app`, `Dockerfile.tests` та `Makefile` з репозиторію викладача та ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами.
Вміст файла `Dockerfile.app`:
```text
FROM python:3.8-slim
LABEL author="Pavlo Makohon"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
   && apt-get upgrade -y\
   && apt-get install git -y\
   && pip install pipenv

WORKDIR /app

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо наш додаток
COPY my_app/ ./

# Створюємо папку для логів
RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
````

Вміст файла `Dockerfile.tests`:

```text
FROM python:3.8-slim
LABEL author="Pavlo Makohon"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
    && apt-get upgrade -y\
    && apt-get install git -y\
    && pip install pipenv

WORKDIR /tests

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY tests/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо нашого проекту
COPY tests/ ./

ENTRYPOINT pipenv run pytest test_app.py --url http://app:5000
```

Вміст файла `Makefile`:

```text
STATES := app tests
REPO := makohon/lab4

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force
```

Дерективи `app` та `tests`:
Створення імеджів для сайту та тесту відповідно.
Деректива `run`:
Запускає сторінку сайту.
Деректива `test-app`:
Запуск тесту сторінки.
Деректива `docker-prune`:
Очищення іміджів, контейнера і інших файлів без тегів.

#### 9. Для початку, використовуючи команду `sudo make app` створіть Docker імеджі для додатку та для тестів `sudo make tests`. Теги для цих імеджів є з моїм Docker Hub репозиторієм. Запустив додаток командою `sudo make run` та перейшовши в іншу вкладку шелу запустіть тести командою `sudo make test-app`.

Запуск сайту

```text
falcon@Makohons-MBP LAB_5 % sudo make run
577ace7bc85a0dd0a7d9cecdfca5909aeb836c7aea22831c9f466038054912a7
f00ad437281cfe316ec32734eec06ac523ad53e1d811504159334e0caa36d9ab
72045ed38b128255a35080098a22a68284ecab98c5bcdfe00b4b1a65e2e53217
```

Проходження тесту:

```text
falcon@Makohons-MBP LAB_5 % sudo make test-app
======================================================================== test session starts ========================================================================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tests
collected 4 items

test_app.py ....                                                                                                                                              [100%]

========================================================================= 4 passed in 0.12s =========================================================================
```

#### 10. Зупинив проект натиснувши Ctrl+C та почистив всі ресурси `Docker` за допомогою `make`.

```text
"docker rm" requires at least 1 argument.
See 'docker rm --help'.

Usage:  docker rm [OPTIONS] CONTAINER [CONTAINER...]

Remove one or more containers
Total reclaimed space: 0B
Total reclaimed space: 0B
Total reclaimed space: 0B
```

#### 11. Створив директиву `docker-push` в Makefile для завантаження створених імеджів у мій Docker Hub репозиторій.

Деректива `docker-push`:

```text
docker-push:
	@docker login \
	&& docker push $(REPO):app \
	&& docker push $(REPO):tests
```

#### 12. Видалив створені та закачані імеджі. Команда `docker images` виводить пусті рядки. Створив директиву в Makefile яка автоматизує процес видалення моїх імеджів.

Деректива `images-delete`:

```text
images-delete:
	@docker rmi $$(docker images -q)
```

Запуск:

```text
falcon@Makohons-MBP LAB_5 % sudo docker images
REPOSITORY     TAG       IMAGE ID       CREATED         SIZE
makohon/lab4   tests     70cc7f8ed657   9 minutes ago   302MB
makohon/lab4   app       717937653158   9 minutes ago   301MB
redis          latest    40c68ed3a4d2   9 days ago      113MB
falcon@Makohons-MBP LAB_5 % sudo make images-delete
Untagged: makohon/lab4:tests
Deleted: sha256:70cc7f8ed657573880b0cf5cb5dc79629784573455cae298f232adee9b207169
Untagged: makohon/lab4:app
Deleted: sha256:7179376531589fd8c9851485bbebe8669d5f9223d494a22e9b61842459853da5
Untagged: redis:latest
Untagged: redis@sha256:619af14d3a95c30759a1978da1b2ce375504f1af70ff9eea2a8e35febc45d747
Deleted: sha256:40c68ed3a4d246b2dd6e59d1b05513accbd2070efb746ec16848adc1b8e07fd4
Deleted: sha256:bec90bc59829e7adb36eec2a2341c7d39454152b8264e5f74988e6c165a2f6a2
Deleted: sha256:c881a068a82210f7964146ebc83e88889224831178f4b8a89ddb0fba91fe96cd
Deleted: sha256:8e9a414cbe1dc316cfa02c0ee912b9c0af0e086accda4e2f340a10c4870a5b35
Deleted: sha256:37d8a78bebeb894e21a8c3bd9041bd4fb600e77154fbb58491d57ef6e70584d5
Deleted: sha256:e8755b67e77af585d946a6078463f45313ec0f385bebdb5bbebadaafbe3b4a2c
```

#### 13. Перейшов до іншого варіанту з використанням `docker-compose.yaml`. Для цього створив даний файл у кореновій папці проекту та заповнив вмістом з прикладу. Проект який я буду розгортити за цим варіантом трохи відрізняється від першого тим що у нього зявляється дві мережі: приватна і публічна.

Файл `docker-compose.yaml`:

```text
version: '3.8'
services:
  hits:
    build:
      context: .
      dockerfile: Dockerfile.app
    image: makohon/lab4:compose-app
    container_name: app
    depends_on:
      - redis
    networks:
      - public
      - secret
    ports:
      - 80:5000
    volumes:
      - hits-logs:/hits/logs
  tests:
    build:
      context: .
      dockerfile: Dockerfile.tests
    image: makohon/lab4:compose-tests
    container_name: tests
    depends_on:
      - hits
    networks:
      - public
  redis:
    image: redis:alpine
    container_name: redis
    volumes:
      - redis-data:/data
    networks:
      - secret
volumes:
  redis-data:
    driver: local
  hits-logs:
    driver: local

networks:
  secret:
    driver: bridge
  public:
    driver: bridge
```

#### 14. Перевірив чи `Docker-compose` встановлений та працює у моїй системі, а далі просто запускаю `docker-compose`:

```text
docker-compose --version
sudo docker-compose -p lab5 up
```

```text
falcon@Makohons-MBP LAB_5 % docker-compose --version
sudo docker-compose -p lab5 up
docker-compose version 1.29.2, build 5becea4c
Creating network "lab5_secret" with driver "bridge"
Creating network "lab5_public" with driver "bridge"
Creating volume "lab5_redis-data" with local driver
Creating volume "lab5_hits-logs" with local driver
Pulling redis (redis:alpine)...
alpine: Pulling from library/redis
97518928ae5f: Pull complete
66f8c4150d27: Pull complete
09a8bf17a0bf: Pull complete
e547313af8e7: Pull complete
335eeadfbde0: Pull complete
7151fc2c01eb: Pull complete
Digest: sha256:50fc99c529b81432a592fa76354783d7fc3ba479a92fc810cbf669138c4138b7
Status: Downloaded newer image for redis:alpine
Building hits
[+] Building 1.4s (13/13) FINISHED
 => [internal] load build definition from Dockerfile.app                                                                                                        0.0s
 => => transferring dockerfile: 818B                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                                                                              1.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                   0.0s
 => [1/7] FROM docker.io/library/python:3.8-slim@sha256:87cdfdbf66e79dfb1d33aca671f9bee623e3710b1f6e0b8476c98c669d69deec                                        0.0s
 => [internal] load build context                                                                                                                               0.0s
 => => transferring context: 1.38kB                                                                                                                             0.0s
 => CACHED [2/7] RUN apt-get update     && apt-get upgrade -y    && apt-get install git -y    && pip install pipenv                                             0.0s
 => CACHED [3/7] WORKDIR /app                                                                                                                                   0.0s
 => CACHED [4/7] COPY my_app/requirements.txt ./                                                                                                                0.0s
 => CACHED [5/7] RUN pipenv install -r requirements.txt                                                                                                         0.0s
 => CACHED [6/7] COPY my_app/ ./                                                                                                                                0.0s
 => CACHED [7/7] RUN mkdir logs                                                                                                                                 0.0s
 => exporting to image                                                                                                                                          0.0s
 => => exporting layers                                                                                                                                         0.0s
 => => writing image sha256:7179376531589fd8c9851485bbebe8669d5f9223d494a22e9b61842459853da5                                                                    0.0s
 => => naming to docker.io/makohon/lab4:compose-app                                                                                                             0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
WARNING: Image for service hits was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Building tests
[+] Building 0.3s (11/11) FINISHED
 => [internal] load build definition from Dockerfile.tests                                                                                                      0.0s
 => => transferring dockerfile: 632B                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                                                                              0.2s
 => [internal] load build context                                                                                                                               0.0s
 => => transferring context: 2.52kB                                                                                                                             0.0s
 => [1/6] FROM docker.io/library/python:3.8-slim@sha256:87cdfdbf66e79dfb1d33aca671f9bee623e3710b1f6e0b8476c98c669d69deec                                        0.0s
 => CACHED [2/6] RUN apt-get update     && apt-get upgrade -y    && apt-get install git -y    && pip install pipenv                                             0.0s
 => CACHED [3/6] WORKDIR /tests                                                                                                                                 0.0s
 => CACHED [4/6] COPY tests/requirements.txt ./                                                                                                                 0.0s
 => CACHED [5/6] RUN pipenv install -r requirements.txt                                                                                                         0.0s
 => CACHED [6/6] COPY tests/ ./                                                                                                                                 0.0s
 => exporting to image                                                                                                                                          0.0s
 => => exporting layers                                                                                                                                         0.0s
 => => writing image sha256:70cc7f8ed657573880b0cf5cb5dc79629784573455cae298f232adee9b207169                                                                    0.0s
 => => naming to docker.io/makohon/lab4:compose-tests                                                                                                           0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
WARNING: Image for service tests was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating redis ... done
Creating app   ... done
Creating tests ... done
Attaching to redis, app, tests
redis    | 1:C 27 Nov 2021 21:42:50.162 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis    | 1:C 27 Nov 2021 21:42:50.162 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
redis    | 1:C 27 Nov 2021 21:42:50.162 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis    | 1:M 27 Nov 2021 21:42:50.164 * monotonic clock: POSIX clock_gettime
redis    | 1:M 27 Nov 2021 21:42:50.165 * Running mode=standalone, port=6379.
redis    | 1:M 27 Nov 2021 21:42:50.165 # Server initialized
redis    | 1:M 27 Nov 2021 21:42:50.165 * Ready to accept connections
app      |  * Serving Flask app 'app' (lazy loading)
app      |  * Environment: production
app      |    WARNING: This is a development server. Do not use it in a production deployment.
app      |    Use a production WSGI server instead.
app      |  * Debug mode: on
app      |  * Running on all addresses.
app      |    WARNING: This is a development server. Do not use it in a production deployment.
app      |  * Running on http://172.24.0.2:5000/ (Press CTRL+C to quit)
app      |  * Restarting with stat
app      |  * Debugger is active!
app      |  * Debugger PIN: 935-648-251
tests    | ============================= test session starts ==============================
tests    | platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
tests    | rootdir: /tests
tests    | collected 4 items
tests    |
app      | 172.24.0.3 - - [27/Nov/2021 21:42:52] "GET /hits HTTP/1.1" 200 -
app      | 172.24.0.3 - - [27/Nov/2021 21:42:52] "GET /logs HTTP/1.1" 200 -
app      | 172.24.0.3 - - [27/Nov/2021 21:42:52] "GET /hits HTTP/1.1" 200 -
app      | 172.24.0.3 - - [27/Nov/2021 21:42:52] "GET /logs HTTP/1.1" 200 -
app      | 172.24.0.3 - - [27/Nov/2021 21:42:52] "GET / HTTP/1.1" 200 -
tests    | test_app.py ....                                                         [100%]
tests    |
tests    | ============================== 4 passed in 0.12s ===============================
tests exited with code 0
```

#### 15. Перевірив чи працює веб-сайт. Дана сторінка відображається за адресою `http://localhost:5000`:

#### 16. Перевірив чи компоуз створив докер імеджі. Всі теги коректні і назва репозиторія вказана коректно:

```text
falcon@Makohons-MBP LAB_5 % sudo docker images
REPOSITORY     TAG             IMAGE ID       CREATED          SIZE
makohon/lab4   compose-tests   70cc7f8ed657   14 minutes ago   302MB
makohon/lab4   compose-app     717937653158   14 minutes ago   301MB
redis          alpine          5c08f13a2b92   2 weeks ago      32.4MB
```

#### 17. Зупинив проект натиснувши `Ctrl+C` і почистітив ресурси створені компоуз командою `docker-compose down`.

#### 18. Завантажив створені імеджі до Docker Hub репозиторію за допомого команди `sudo docker-compose push`.

#### 19. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`? - На мою думку `Makefile` при використанні більш інтуїтивно зрозумілий, адже можна в ньому побачити які команди запускаються, але і в одночас треба знати які команди використовувати.`docker-compose.yaml` описує, як повинен бути розгорнутий образ, тобто все, що необхідно для створення контейнера. `Makefile` в свою чергу, спрощує процеси за рахунок автоматизації дій.

#### 20. (Завдання) Оскільки Ви навчились створювати docker-compose.yaml у цій лабораторній то потрібно:

- Cтворив `docker-compose.yaml` для лабораторної №4. Компоуз повинен створити два імеджі для `Django` сайту та моніторингу, а також їх успішно запустити.
  Файлик `docker-compose.yaml`:

```text
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: makohon/lab4:compose-jango
    container_name: django
    networks:
      - public
    ports:
      - 8000:8000
  monitoring:
    build:
      context: .
      dockerfile: Dockerfile.site
    image: makohon/lab4:compose-monitoring
    container_name: monitoring
    network_mode: host

networks:
  public:
    driver: bridge
```

#### 21. Після успішного виконання роботи я відредагував свій `README.md` у цьому репозиторію та створив pull request.
