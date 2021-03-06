# demo_shop
Демо интернет-магазина на Flask.

Магазин состоит из двух страниц:
- страница со списком всех товаров;
- страница с данными конкретного товара.

## Требования
Для работы проекта требуется python3, библиотеки alembic, click, Flask,
Flask-Migrate, Flask-SQLAlchemy, itsdangerous, Jinja2, Mako,
MarkupSafe, python-dateutil, python-editor, six, SQLAlchemy, Werkzeug.

Зависимости проекта приведены в файле requirements.txt.
Для установки зависимостей выполните следующую команду:

**pip3 install -r requirements.txt**


## Запуск
Клонируйте репозиторий следующей командой:

**git clone https://github.com/evmaksimenko/demo_shop.git**

или 

**git clone git@github.com:evmaksimenko/demo_shop.git**

Для запуска выполните команду в директории проекта 

**python demo_shop.py**

После этого откройте при помощи браузера страницу приложения localhost:5000.
По умолчанию отобразится страница со списком всех товаров. 
Про клику на изображение товара, его цену или наименование, откроется 
страница с описанием конкретного товара.