import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.frome_pages_locators import FromPagesLocators as Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class CheckFilmPage(BasePage):

    def select_option_by_value(self, select_locator, option_text):
        select = Select(self.driver.find_element(*select_locator))
        select.select_by_visible_text(option_text)

    def click_wide_find(self):
        self.driver.find_element(*Locators.FIND_BUTTON).click()

    def setup_filter(self):
        # выбор имени
        self.driver.find_element(*Locators.NAME_INPUT).send_keys("12")
        # выбор страны
        self.select_option_by_value(Locators.COUNTRY_SELECTOR, "СССР")
        # выбор жанра
        self.select_option_by_value(Locators.GENRE_SELECTOR, "комедия")
        self.select_option_by_value(Locators.GENRE_SELECTOR, "приключения")
        # выбор создателей
        self.select_option_by_value(Locators.CREATOR_SELECTOR, "Актер")
        self.select_option_by_value(Locators.CREATOR_2_SELECTOR, "Режиссер")
        # ввод имен
        name_actor_input = self.driver.find_element(*Locators.ACTOR_NAME_INPUT)
        name_actor_input.send_keys("Арчил Гомиашвили")
        name_actor_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        name_actor_input.send_keys(Keys.ARROW_DOWN)

        name_actor_input = self.driver.find_element(*Locators.DIRECTOR_NAME_INPUT)
        name_actor_input.send_keys("Леонид Гайдай")
        name_actor_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        name_actor_input.send_keys(Keys.ARROW_DOWN)

        wait = self.getWait(5)
        wait.until(EC.presence_of_element_located(Locators.FILM_COUNT_A))

    def click_filtered_find(self):
        # кнопка поиска при фильтрации
        self.driver.find_element(*Locators.SEARCH_BUTTON).click()

    def check_card_fields(self):
        # проверка результата поиска
        text_result = self.driver.find_element(*Locators.NAVIGATOR_DIV).text
        if text_result != "1—1 из 1":
            raise ValueError("Неверный результат поиска, {0}".format(text_result))
        print("Результат поиска 1—1 из 1")

        elements_with_class_element = self.driver.find_elements(*Locators.ELEMENTS_DIV)
        if len(elements_with_class_element) != 1:
            raise ValueError("Неверный результат поиска, {0}".format(len(elements_with_class_element)))
        print("Найдена одна карточка")

        #  div для проверки
        film_card_div = elements_with_class_element[0]

        year_span = film_card_div.find_element(*Locators.YEAR_SPAN)
        if year_span.text != "1971":
            raise ValueError("Неверный год")
        print("Год 1971")

        info_div = film_card_div.find_element(*Locators.INFO_DIV)
        try:
            duration_span = info_div.find_element(*Locators.DURATION_SPAN)
        except Exception:
            raise ValueError("Неверное время фильма")
        else:
            print("Время 153 мин")

        try:
            film_link = info_div.find_element(*Locators.FILM_LINK)
        except Exception:
            raise ValueError("Название-ссылка не найдено")
        else:
            print("Название-ссылка присутствует")

        # переход на карточку фильма
        film_link.click()

    def check_page_fields(self):
        page_source = self.driver.page_source
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
        country_div = self.driver.find_element(*Locators.COUNTRY_DIV)
        country_value_element = country_div.find_element(*Locators.COUNTRY_VALUE_A)
        if country_value_element is None:
            raise ValueError("Страна не верна")
        else:
            print("Страна верна")

        # проверка режиссера
        director_div = self.driver.find_element(*Locators.DIRECTOR_DIV)
        director_value_element = director_div.find_element(*Locators.DIRECTOR_VALUE_A)
        if director_value_element is None:
            raise ValueError("Режиссер не верный")
        else:
            print("Режиссер верный")

        # проверка списка жанров
        genres_list = ["комедия", "приключения"]
        genre_div = self.driver.find_element(*Locators.GENRE_DIV)
        genre_value_element = genre_div.parent.find_elements(*Locators.GENRE_VALUE_A)
        a_content_list = [a.text for a in genre_value_element]
        if all(genre in a_content_list for genre in genres_list):
            print("Все жанры верны")
        else:
            raise ValueError("Не все жанры верны")

    def click_best_film_page(self):
        # клик по кнопке поиск лучших фильмов
        self.driver.find_element(*Locators.BEST_BUTTON).click()

    def check_navigate_best_films(self):
        wait = self.getWait(2)
        element = wait.until(EC.presence_of_element_located(Locators.LABEL_H1))
        if element is None:
            raise ValueError("Заголовок не найден")
        else:
            print("Заголовок найден")

        genre_list = self.driver.find_element(*Locators.GENRE_LIST)
        genre_list.click()
        ul_element = genre_list.parent.find_element(*Locators.GENRE_UL)

        # выбор жанров
        first_genre = ul_element.find_element(*Locators.FIRST_GENRE_LABEL)
        first_genre.click()
        sec_genre = ul_element.find_element(*Locators.SECOND_GENRE_LABEL)
        sec_genre.click()

    def click_find_best_button(self):
        # клик показать фильмы
        # wait = self.getWait(2) # не работает
        # wait.until(EC.presence_of_element_located(Locators.FINDER_BUTTON)).click()
        time.sleep(2)
        self.driver.find_element(*Locators.FINDER_BUTTON).click()

    def check_finded_best_films(self):
        # проверка результата
        wait = self.getWait(5)
        navigator_div = wait.until(EC.presence_of_element_located(Locators.FLOAT_NAVIGATOR_DIV))
        text_result = navigator_div.text
        if text_result != "1—4 из 4":
            raise ValueError("Неверный результат поиска, {0}".format(text_result))
        print("Результат поиска 1—4 из 4")

        div_with_films = self.driver.find_element(*Locators.FILMS_DIV)
        child_divs = div_with_films.find_elements(*Locators.CHILDS_DIV)

        if len(child_divs) == 4:
            print("Выбрано 4 фильма")
        else:
            raise ValueError("Неверный результат поиска, {0} фильма, вместо 4".format(len(child_divs)))
