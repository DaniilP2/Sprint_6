from pages.base_page import BasePage
from locators.faq_locators import FAQLocators
from curl import *
import allure

class FAQPage(BasePage):
    
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step('Кликаем на кнопку вопроса с текстом {text}')
    def click_ask_button(self, text):
        self.click_by_text(text)

    @allure.step('Получаем текст активного ответа')
    def get_text_active_answer(self):
        return self.get_text(FAQLocators.ACTIVE_ANSWER_PANEL)