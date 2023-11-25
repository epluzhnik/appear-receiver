ML API
--

API для предсказания по тексту обращения темы, группы тем и исполнителя.

---
### Запуск (docker)

1. Сборка контейнера
   ```bash
   docker build -t appear-api:latest .
   ```

2. Запуск контейнера
   ```bash
   docker run --rm --name appear-api -p="8000:8000" appear-api:latest
   ```

### Запуск (без docker)
1. Если не установлен `poetry>1.6`
   ```bash
   curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.6.1 python3 -
   ```

2. Настройка окружения
   ```bash
   poetry install
   ```
   
3. Запуск
   ```bash
   poetry install
   ```
   
---
> **Swagger - http://0.0.0.0:8000/docs**

### Фичи

1. Сбор и хранение статистики по предсказанным темам, группам тем, исполнителям, для просто первичного анализа по
   необходимости.
2. Обнаружение инцидентов. Если за небольшой промежуток времени будет много обращений по одной группе тем, то API
   обнаружит это и сообщит при обработке текста, который породит инцидент.
3. При непонятном обращении модель предсказывает "нулевой" класс, что позволяет попросить пользователя уточнить свой
   запрос.


### Модели

ИТОГОВЫЕ ВЕРСИИ МОДЕЛИ:
1) Предсказание Исполнителя: https://drive.google.com/file/d/1Ilvt-mq3C8fW8la2iMcuoCYu35Xu0Fjl/view
2) Предсказание Группы тем: https://drive.google.com/drive/folders/11DleA6bBUpUW3CRkVw4hKZJ-z6lR7-YS?usp=sharing
3) Предсказание Темы: https://drive.google.com/file/d/1fbMygBAYLOUgvybxF2LLfFTX2k-9MpAc/view?usp=sharing
