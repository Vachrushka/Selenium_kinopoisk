import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def select_option_by_value(driver_, select_locator, option_value):
    select = Select(driver_.find_element(*select_locator))
    select.select_by_value(option_value)


url = "https://www.kinopoisk.ru"

driver = webdriver.Chrome()
driver.get(url)

# клик по кнопке
xpath = "//*[@aria-label='Расширенный поиск']"
btn_find = driver.find_element(By.XPATH, xpath)
btn_find.click()

# выбор имени
input_name = driver.find_element(By.ID, "find_film")
input_name.send_keys("12")

# выбор страны
selector_country = (By.ID, "country")
select_option_by_value(driver, selector_country, "13")

# выбор жанра
selector_genre = (By.ID, "m_act[genre]")
select_option_by_value(driver, selector_genre, "6")
select_option_by_value(driver, selector_genre, "10")

# выбор создателей
selector_creator = (By.ID, "cr_search_field_1_select")
select_option_by_value(driver, selector_creator, "actor")

selector_creator_2 = (By.ID, "cr_search_field_2_select")
select_option_by_value(driver, selector_creator_2, "director")

# ввод имен
input_name_actor = driver.find_element(By.ID, "cr_search_field_1")
input_name_actor.send_keys("Арчил Гомиашвили")
input_name_actor.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
input_name_actor.send_keys(Keys.ARROW_DOWN)

input_name_dir = driver.find_element(By.ID, "cr_search_field_2")
input_name_dir.send_keys("Леонид Гайдай")
input_name_dir.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
input_name_dir.send_keys(Keys.ARROW_DOWN)

# кнопка поиск
time.sleep(1)
btn_search = driver.find_element(By.ID, "btn_search_6")
btn_search.click()

# проверка результата
navigator_div = driver.find_element(By.XPATH, '//*[@class="navigator"]/div')
text_result = navigator_div.text
if text_result != "1—1 из 1":
    raise ValueError("Неверный результат поиска, {0}".format(text_result))
print("Результат поиска 1—1 из 1")

elements_with_class_element = driver.find_elements(By.CSS_SELECTOR, "div.element")
if len(elements_with_class_element) != 1:
    raise ValueError("Неверный результат поиска, {0}".format(len(elements_with_class_element)))
print("Найдена одна карточка")

# div для проверки
film_card_div = elements_with_class_element[0]

year_span = film_card_div.find_element(By.CSS_SELECTOR, "span.year")
if year_span.text != "1971":
    raise ValueError("Неверный год")
print("Год 1971")

info_div = film_card_div.find_element(By.CSS_SELECTOR, "div.info")
try:
    duration_span = info_div.find_element(By.XPATH, "//span[contains(text(), '153 мин')]")
except Exception:
    raise ValueError("Неверное время фильма")
else:
    print("Время 153 мин")

film_link = info_div.find_element(By.LINK_TEXT, "12 стульев")
if not film_link.is_displayed():
    raise ValueError("Название-ссылка не найдено")
print("Название-ссылка присутствует")

# переход на карточку фильма
film_link.click()

# проверка наличия заголовка

time.sleep(0.5)
page_source = driver.page_source
expected_title = "12 стульев (1971)"
if expected_title in page_source:
    print("Заголовок фильма найден")
else:
    # print("Заголовок фильма  не найден")
    raise ValueError("Заголовок фильма не найден")

# проверка наличия тайтла "О фильме"
expected_title_2 = "О фильме"
if expected_title_2 in page_source:
    print("Заголовок 'О фильме' найден")
else:
    # print("Заголовок 'О фильме' не найден")
    raise ValueError("Заголовок 'О фильме' не найден")

# проверка страны
country_div = driver.find_element(By.XPATH, "//div/div[contains(text(), 'Страна')]")
country_value_element = country_div.find_element(By.XPATH, "//a[contains(text(), 'СССР')]")
if country_value_element is None:
    raise ValueError("Страна не верна")
else:
    print("Страна верна")

# проверка режиссера
director_div = driver.find_element(By.XPATH, "//div/div[contains(text(), 'Режиссер')]")
director_value_element = director_div.find_element(By.XPATH, "//a[contains(text(), 'Леонид Гайдай')]")
if director_value_element is None:
    raise ValueError("Режиссер не верный")
else:
    print("Режиссер верный")

# проверка списка жанров
genres_list = ["комедия", "приключения"]
genre_div = driver.find_element(By.XPATH, "//div/div[contains(text(), 'Жанр')]")
genre_value_element = genre_div.parent.find_elements(By.TAG_NAME, "a")
a_content_list = [a.text for a in genre_value_element]
if all(genre in a_content_list for genre in genres_list):
    print("Все жанры верны")
else:
    raise ValueError("Не все жанры верны")

driver.quit()
