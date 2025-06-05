import asyncio
import re
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from config import cnf


class Parser:
    
    urls: dict = {
        'contacts': 'https://niu.ranepa.ru/about/kontakty/',
        'faq': 'https://niu.ranepa.ru/vopros/'
    }
    contacts: list = []
    faq: list = []
    
    def _parse(self, url: str, **params) -> list[str] | None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver_path = 'services/ai/selenium_driver/chromedriver.exe'
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.get(url=url)
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, params.get("tag"))))
            page_html = driver.page_source
            soup = BeautifulSoup(page_html, 'html.parser')
            tables = soup.find_all(params.get("tag"), class_=params.get("attr"))

            if not tables:
                print("Данные не найдены.")
                return None

            texts = []
            for table in tables:
                texts.append(table.text)
            print(texts)
            return texts
                
        except Exception as e:
            print(f"Ошибка при парсинге: {e}")
            return None
        
        finally:
            driver.quit()

    def _get_contacts(self) -> list[str] | None:
        url = self.urls['contacts']
        texts = self._parse(url=url, tag='table', attr='table')
        if texts is not None:
            self.contacts.extend(texts)
            return self.contacts
        return None
    
    def _get_faq(self) -> list[str] | None:
        url = self.urls['faq']
        faq = self._parse(url=url, tag='section', attr='questions')
        if faq is not None:
            self.faq.extend(faq)
            return self.faq
        return None

    def save_data_to_files(self) -> None:

        contacts = self._get_contacts()
        if contacts is not None:
            with open('services/ai/data/datasets/contacts.txt', 'w', encoding='utf-8') as file:
                for contact in contacts:
                    file.write(contact + '\n\n')
            print("Контакты успешно записаны в файл contacts.txt.")
        else:
            print("Нет контактных данных для записи.")

        faq = self._get_faq()
        if faq is not None:
            with open('services/ai/data/datasets/faq.txt', 'w', encoding='utf-8') as file:
                for question in faq:
                    file.write(question + '\n\n')
            print("FAQ успешно записан в файл faq.txt.")
        else:
            print("Нет данных FAQ для записи.")
        return


def startup():
    parser = Parser()
    return parser.save_data_to_files()