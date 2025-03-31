GET запрос для вывода всего каталога - GET /api/products/
/admin/ - Админ-панель

Фильтры:
    фитрация по имени - GET /api/products/?name=название товара (например банан)
    фильтрация по цене - GET /api/products/?price=цена (например 100)
    фильтрация по атрибуту - GET /api/products/?value=значение атрибута (например красный)

Кол-во уникальных категорий параметров отображено внизу:
    "parameter_count": {
        "параметр1": 3,
        "параметр2": 1
    }

Уникальные значения параметров:
    "unucal_params": [
        "красный",
        "зеленый",
        "жёлтый",
        "оранжевый"
    ]

Краткий экскурс по архитектуре, попутно в файлах оставил комментарии с более подробным поянением функционала:
catalog_project\catalog\models.py - модели для бд
catalog_project\catalog\views.py - основная логика отображения
catalog_project\catalog\serializers.py - сериализеры для Django Rest framework
catalog_project\catalog\fixtures - фикстуры с тестовыми данными 
catalog_project\catalog\admin.py - настройка админки
catalog_project\media - папка, куда сохраняются фото из бд
catalog_project\db.sqlite3 - база данных
catalog_project\requirements.txt - файл со всеми зависимостями (использованные технологии)

Запуск проекта:
    cd путь до папки с проектом\catalog_project
    python manage.py runserver