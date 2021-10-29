# **Лабораторна робота №2**

---

## Послідовність виконання лабораторної роботи:

#### 1. Створюю папку **_Lab_2_** в якій ствоюю **_README.md_**.

#### 2. За допомогою пакетного менеджера **_PIP_** інсталював **_pipenv_** та створив ізольоване середовище для **_Python_**. Використовуючи команди:

```text
sudo pip install pipenv
sudo pipenv --python 3.7
sudo pipenv shell
```

Ознайомився з командаю `pipenv -h` і виконав її.

```text
falcon@Makohons-MBP LAB_2 % pipenv -h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

#### 3. Встановив бібліотеку **_requests_** в моєму середовищі. Ця бібліотека дозволяє створювати HTTP запити до заданих Web сторінок. А також встановив бібліотеку **_ntplib_** яка працює з часом.

Використав команди:

```text
pipenv install requests
pipenv install ntplib
```

#### 4. Створив **_app.py_** файл. Скопіював код програми із репозиторію викладача до себе. Для кращого розуміння програми ознайомився з **_Python tutorial_**.

#### 5. Запускаю програму за допомогою команди `sudo python app.py`.

Результат виконання:

```text
(LAB_2) falcon@Makohons-MBP LAB_2 % python app.py
========================================
Результат без параметрів:
No URL passed to function
========================================
Результат з правильною URL:
Time is:  08:15:48 PM
Date is:  10-29-2021
success
```

#### 6. Встановив бібліотеку `pytest` за допомогою команди `pipenv install pytest`. Для кращого розуміння ознайомився з документацією **_pytest_**.

#### 7. Створив папку **_tests_**, в якій створив файли **_tests.py_** і **\_**init**.py\_**. Скопіював код програми із репозиторію викладача до себе. Запускаю програму за допомогою команди `pytest tests/tests.py`.

Виконанння програми:

```text
(LAB_2) falcon@Makohons-MBP LAB_2 % pytest tests/tests.py
===================================== test session starts =====================================
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/falcon/Desktop/Projects/Pavlo_Makohon_IK_31/LAB_2
collected 5 items

tests/tests.py .....                                                                    [100%]

====================================== 5 passed in 0.70s ======================================

```

#### 8. ❗ (Захист) У програмі дописав функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Доброго дня/ночі.

Код програми:

```python
def home_work(daytime=datetime.today().strftime("%H:%M %p")):
    message = ""
    if "AM" in daytime:
        message = "Доброго дня"
    elif "PM" in daytime:
        message = "Доброї ночі"
    return message
```

#### 9. ❗ (Захист) Написав тест що буде перевіряти правильність виконання моєї функції.

Код тесту:

```python
def test_home_work(self):
        self.assertEqual(home_work("09:53 PM"), "Доброї ночі")
        self.assertEqual(home_work("02:07 AM"), "Доброго дня")
```

Виконання тесту:

```text
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/falcon/Desktop/Projects/Pavlo_Makohon_IK_31/LAB_2
collected 5 items

tests/tests.py .....                                                     [100%]

============================== 5 passed in 0.64s ===============================
```

#### 10. Перенаправляю результат виконання тестів у файл **_results.txt_** за допомогою команди `pytest tests/tests.py > results.txt`, а також додаю результат виконання програми у кінець цього ж файл за допомогою команди `python app.py >> results.txt`.

#### 11. Зробив коміт із змінами до свого репозиторію.

#### 12. Заповнив **_Makefile_** необхідними командами (bash) для повної автоматизації процесу СІ мого проекту:

Вміст **_Makefile_**:

```text
.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Installing pipenv and dependencies."
	@echo "--------------------------------------------"
	@echo " "
	sudo pip install pipenv
	sudo pipenv --python 3.8
	sudo pipenv install requests
	sudo pipenv install ntplib
	sudo pipenv install pytest

test:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Start tests."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run pytest tests/tests.py > results.txt

run:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Run Python app."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run python3 app.py >> results.txt

deploy:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Adding and Committing results.txt to git."
	@echo "--------------------------------------------"
	@echo " "
	git add results.txt
	git commit -m "Automatic commit by MakeFile"
	git push
```

#### 13. Закомітив зміни в Makefile до власного репозиторію.

#### 14. Склонував **_git_** репозиторій на віртуальну машину Ubuntu. Перейшов у папку з лабораторною роботою та запустив **_Makefile_** файл за допомогти команди `make`.

Результатом виконання цієї команди є створено ізольоване середовище, виконано тести, запущено програму та закомічено файл у git репозеторій.

```text
falcon@Makohons-MBP LAB_2 % make 
 
--------------------------------------------
Installing pipenv and dependencies.
--------------------------------------------
 
sudo pip install pipenv
WARNING: The directory '/Users/falcon/Library/Caches/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Requirement already satisfied: pipenv in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (2021.5.29)
Requirement already satisfied: virtualenv in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipenv) (20.9.0)
Requirement already satisfied: pip>=18.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipenv) (21.3.1)
Requirement already satisfied: certifi in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipenv) (2021.10.8)
Requirement already satisfied: setuptools>=36.2.1 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipenv) (57.4.0)
Requirement already satisfied: virtualenv-clone>=0.2.5 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pipenv) (0.5.7)
Requirement already satisfied: backports.entry-points-selectable>=1.0.4 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from virtualenv->pipenv) (1.1.0)
Requirement already satisfied: six<2,>=1.9.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from virtualenv->pipenv) (1.16.0)
Requirement already satisfied: platformdirs<3,>=2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from virtualenv->pipenv) (2.4.0)
Requirement already satisfied: filelock<4,>=3.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from virtualenv->pipenv) (3.3.2)
Requirement already satisfied: distlib<1,>=0.3.1 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from virtualenv->pipenv) (0.3.3)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
sudo pipenv --python 3.8
Virtualenv already exists!
Removing existing virtualenv...
Warning: the environment variable LANG is not set!
We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
Creating a virtualenv for this project...
Pipfile: /Users/falcon/Desktop/Projects/Pavlo_Makohon_IK_31/LAB_2/Pipfile
Using /usr/bin/python3 (3.8.2) to create virtualenv...
⠦ Creating virtual environment...created virtual environment CPython3.8.2.final.0-64 in 400ms
  creator CPython3macOsFramework(dest=/Users/falcon/.local/share/virtualenvs/LAB_2-RRnC0dtm, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/falcon/Library/Application Support/virtualenv)
    added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/falcon/.local/share/virtualenvs/LAB_2-RRnC0dtm
sudo pipenv install requests
Installing requests...
Adding requests to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 9/9 — 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
sudo pipenv install ntplib
Installing ntplib...
Adding ntplib to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
sudo pipenv install pytest
Installing pytest...
Adding pytest to Pipfile's [packages]...
✔ Installation Succeeded 
Installing dependencies from Pipfile.lock (18d437)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
 
--------------------------------------------
Start tests.
--------------------------------------------
 
sudo pipenv run pytest tests/tests.py > results.txt
 
--------------------------------------------
Run Python app.
--------------------------------------------
 
sudo pipenv run python3 app.py >> results.txt
 
--------------------------------------------
Adding and Committing results.txt to git.
--------------------------------------------
 
git add results.txt
git commit -m "Automatic commit by MakeFile"
[master 04057f0] Automatic commit by MakeFile
 1 file changed, 2 insertions(+), 2 deletions(-)
git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 490 bytes | 490.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/IFalcoNI/Pavlo_Makohon_IK_31.git
   9011bc8..04057f0  master -> master
falcon@Makohons-MBP LAB_2 %   
```
