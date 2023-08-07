import json
import allure
import pytest
from allure_commons.types import AttachmentType

from pages.check_film_page import CheckFilmPage


class TestSearchFilm:

    @allure.feature('Проверка поиска фильма, первая часть')
    @allure.story('Поиск фильма')
    def test_search(self, driver):
        url = "https://www.kinopoisk.ru"
        check_film_page = CheckFilmPage(driver, url)
        check_film_page.open()

        with allure.step('Переходим на страницу расширенного поиска'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.click_wide_find()

        with allure.step('Вводим данные фильтра'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.setup_filter()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.click_filtered_find()

        with allure.step('Проверка результата и полей карточки'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.check_card_fields()

        with allure.step('Проверка страницы фильма'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.check_page_fields()

    @allure.feature('Проверка поиска фильмов, вторая часть')
    @allure.story('Поиск лучших фильмов')
    def test_search_best(self, driver):
        url = "https://www.kinopoisk.ru"
        check_film_page = CheckFilmPage(driver, url)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        check_film_page.open()

        with allure.step('Переходим на страницу расширенного поиска'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.click_wide_find()

        with allure.step('Переходим на страницу поиска лучших фильмов'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.click_best_film_page()

        with allure.step('Настройка фильтра на странице поиска лучших фильмов'):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.check_navigate_best_films()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot_after_actions",
                          attachment_type=AttachmentType.PNG)

        with allure.step('Проверка результата поиска'):
            check_film_page.click_find_best_button()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            check_film_page.check_finded_best_films()


