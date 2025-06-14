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
        'faq': 'https://niu.ranepa.ru/vopros/',
        'yuris-fak': 'https://niu.ranepa.ru/about/fakultety/yuridicheskiy-fakultet/sotrudniki-i-kontakty/',
        'manage-fak': 'https://niu.ranepa.ru/about/fakultety/fakultet-upravleniya/sotrudniki-i-kontakty/',
        'eco-fak-security': 'https://niu.ranepa.ru/about/fakultety/fakultet-ekonomiki/kafedry-ef/k-eioeb/pps/',
        'eco-fak-math': 'https://niu.ranepa.ru/about/fakultety/fakultet-ekonomiki/kafedry-ef/k-mmveiu/pps/',
        'eco-fak-finance': 'https://niu.ranepa.ru/about/fakultety/fakultet-ekonomiki/kafedry-ef/k-fiprfr/pps/',
        'eco-fak-lang': 'https://niu.ranepa.ru/about/fakultety/fakultet-ekonomiki/kafedry-ef/k-inyaz/pps/'
    }
    contacts: list = []
    faq: list = []
    yuris: list = []
    manage: list = []
    eco: list = []
    
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
    
    def _get_yuris(self) -> list[str] | None:
        url = self.urls['yuris-fak']
        yuris = self._parse(url=url, tag='table', attr='table')
        if yuris is not None:
            self.yuris.extend(yuris)
            return self.yuris
        return None
    
    def _get_manage(self) -> list[str] | None:
        url = self.urls['manage-fak']
        manage = self._parse(url=url, tag='table', attr='table')
        if manage is not None:
            self.manage.extend(manage)
            return self.manage
        return None
    
    def _get_eco(self) -> list[str] | None:
        urls_to_parse = []
        for key in self.urls.keys():
            if 'eco' in key:
                urls_to_parse.append(self.urls[key]) 
                
        for url in urls_to_parse:
            eco = self._parse(url=url, tag='table', attr='table')
            if eco is not None:
                self.eco.extend(eco)
        
        return self.eco if self.eco else None
    
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
            
        yuris = self._get_yuris()
        if yuris is not None:
            with open('services/ai/data/datasets/yuris.txt', 'w', encoding='utf-8') as file:
                for question in yuris:
                    file.write(question + '\n\n')
            print("yuris успешно записан в файл yuris.txt.")
        else:
            print("Нет данных yuris для записи.")
            
        manage = self._get_manage()
        if manage is not None:
            with open('services/ai/data/datasets/manage.txt', 'w', encoding='utf-8') as file:
                for question in manage:
                    file.write(question + '\n\n')
            print("manage успешно записан в файл manage.txt.")
        else:
            print("Нет данных manage для записи.")
        
        eco = self._get_eco()
        if eco is not None:
            with open('services/ai/data/datasets/eco.txt', 'w', encoding='utf-8') as file:
                for question in eco:
                    file.write(question + '\n\n')
            print("eco успешно записан в файл eco.txt.")
        else:
            print("Нет данных eco для записи.")
        return


def startup():
    parser = Parser()
    return parser.save_data_to_files()