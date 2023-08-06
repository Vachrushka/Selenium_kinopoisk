import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.kinopoisk.ru"

driver = webdriver.Chrome()
driver.get(url)

# клик по кнопке Расширенный поиск
xpath = f"//*[@aria-label='Расширенный поиск']"
btn_find = driver.find_element(By.XPATH, xpath)
btn_find.click()

# клик по кнопке поиск лучших фильмов
xpath = '//h1/a'
btn_best = driver.find_element(By.XPATH, xpath)
btn_best.click()

wait = WebDriverWait(driver, 2)
xpath = "//td/h1[contains(text(), 'Навигатор по лучшим фильмам')]"
element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
if element is None:
    raise ValueError("Заголовок не найден")
else:
    print("Заголовок найден")

genre_list = driver.find_element(By.ID, "genreListTitle")
genre_list.click()
ul_element = genre_list.parent.find_element(By.TAG_NAME, "ul")

# выбор жанров
first_genre = ul_element.find_element(By.XPATH, "//li/label[contains(text(), 'аниме')]")
first_genre.click()
sec_genre = ul_element.find_element(By.XPATH, "//li/label[contains(text(), 'для взрослых')]")
sec_genre.click()

# клик показать фильмы
time.sleep(3)
btn_find = driver.find_element(By.CSS_SELECTOR, "input.nice_button")
btn_find.click()

# проверка результата
wait = WebDriverWait(driver, 5)
navigator_div = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="navigator"]/div')))
text_result = navigator_div.text
if text_result != "1—4 из 4":
    raise ValueError("Неверный результат поиска, {0}".format(text_result))
print("Результат поиска 1—4 из 4")

div_with_films = driver.find_element(By.ID, "itemList")
child_divs = div_with_films.find_elements(By.XPATH, "./div")

if len(child_divs) == 4:
    print("Выбрано 4 фильма")
else:
    raise ValueError("Неверный результат поиска, {0} фильма, вместо 4".format(len(child_divs)))

driver.quit()
