from selenium.webdriver.common.by import By


class FromPagesLocators:
    # first test
    #1
    # FIND_BUTTON = (By.XPATH, "//*[@aria-label='Расширенный поиск']")
    #2
    # NAME_INPUT = (By.ID, "find_film")
    # COUNTRY_SELECTOR = (By.ID, "country")
    # GENRE_SELECTOR = (By.ID, "m_act[genre]")
    # CREATOR_SELECTOR = (By.ID, "cr_search_field_1_select")
    # CREATOR_2_SELECTOR = (By.ID, "cr_search_field_2_select")
    # ACTOR_NAME_INPUT = (By.ID, "cr_search_field_1")
    # DIRECTOR_NAME_INPUT = (By.ID, "cr_search_field_2")
    # INPUT_RESULT_SPAN = (By.XPATH, '//*[@id="ui-id-555"]/span')
    FILM_COUNT_A = (By.XPATH, "//a[contains(text(), '1 фильм')]")
    SEARCH_BUTTON = (By.ID, "btn_search_6")
    #3
    NAVIGATOR_DIV = (By.XPATH, '//*[@class="navigator"]/div')
    ELEMENTS_DIV = (By.CSS_SELECTOR, "div.element")
    YEAR_SPAN = (By.CSS_SELECTOR, "span.year")
    INFO_DIV = (By.CSS_SELECTOR, "div.info")
    DURATION_SPAN = (By.XPATH, "//span[contains(text(), '153 мин')]")
    FILM_LINK = (By.LINK_TEXT, "12 стульев")
    COUNTRY_DIV = (By.XPATH, "//div/div[contains(text(), 'Страна')]")
    COUNTRY_VALUE_A = (By.XPATH, "//a[contains(text(), 'СССР')]")
    DIRECTOR_DIV = (By.XPATH, "//div/div[contains(text(), 'Режиссер')]")
    DIRECTOR_VALUE_A = (By.XPATH, "//a[contains(text(), 'Леонид Гайдай')]")
    GENRE_DIV = (By.XPATH, "//div/div[contains(text(), 'Жанр')]")
    GENRE_VALUE_A = (By.TAG_NAME, "a")
    #second test
    BEST_BUTTON = (By.XPATH, '//h1/a')
    LABEL_H1 = (By.XPATH, "//td/h1[contains(text(), 'Навигатор по лучшим фильмам')]")
    GENRE_LIST = (By.ID, "genreListTitle")
    GENRE_UL = (By.TAG_NAME, "ul")
    FIRST_GENRE_LABEL = (By.XPATH, "//li/label[contains(text(), 'аниме')]")
    SECOND_GENRE_LABEL = (By.XPATH, "//li/label[contains(text(), 'для взрослых')]")
    FINDER_BUTTON = (By.CSS_SELECTOR, "input.nice_button")
    FLOAT_NAVIGATOR_DIV = (By.XPATH, '//div[@class="navigator"]/div')
    FILMS_DIV = (By.ID, "itemList")
    CHILDS_DIV = (By.XPATH, "./div")
