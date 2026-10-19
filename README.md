# demoblaze-cart-test

Автотест на Python (Playwright + pytest) для сайта https://www.demoblaze.com/.

## Сценарий

1. Открыть страницу https://www.demoblaze.com/
2. Нажать на товар «Samsung galaxy s6»
3. На странице товара нажать «Add to cart»
4. Нажать «OK» в pop-up
5. Нажать кнопку «Cart» в шапке сайта

**Ожидаемый результат:** в корзине отображается единственный элемент «Samsung galaxy s6».

## Запуск

Требуется Python 3.9+ и установленный Git.

### 1. Клонировать репозиторий и перейти в папку проекта

```bash
git clone https://github.com/pokachnov/demoblaze-cart-test.git
cd demoblaze-cart-test
```

### 2. Создать, активировать виртуальное окружение и установить зависимости с браузером

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash)
# source .venv/bin/activate      # Linux / macOS
pip install -r requirements.txt
playwright install chromium
```

### 3. Запустить тест

```bash
pytest
```

Запуск с видимым окном браузера:

```bash
pytest --headed
```

Запуск с видимым окном браузера с паузой в конце для проверки результата:

```bash
PAUSE=1 pytest --headed
```

### Результат

В консоли должна появиться строка вида:

```
tests/test_cart.py::test_add_samsung_galaxy_s6_to_cart[chromium] PASSED
1 passed in 15.54s
``` 
## Структура

```
tests/
    test_cart.py   # тест
requirements.txt     # зависимости
pytest.ini           # настройки pytest
```

## Примечание
Примеры запуска написаны для терминала Bash (Git Bash на Windows, Linux, macOS)