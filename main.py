import pandas as pd
import requests
from selenium import webdriver
from tkinter import Tk, ttk, StringVar
from pathlib import Path
from selenium.common.exceptions import WebDriverException
from html.parser import HTMLParser

def GUI(URL, SEARCH_TERM, CLASS_TERM, START_DATE, END_DATE):
    window = Tk()
    window.title('TJSP Webscrapper')
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')
    
    URL=StringVar(URL)
    SEARCH_TERM=StringVar(SEARCH_TERM)
    CLASS_TERM=StringVar(CLASS_TERM)
    START_DATE=StringVar(START_DATE)
    END_DATE=StringVar(END_DATE)
    
    url_tk = ttk.Entry(justify = 'center', exportselection = 0)

def process_PDF(text):
    pass

def main():
    CUR_DIR = Path(__file__).parent
    PROGRAM = 'chromedriver.exe'
    PATH = CUR_DIR / PROGRAM
    
    URL = 'https://esaj.tjsp.jus.br/cjpg/'
    SEARCH_TERM = 'covid'
    CLASS_TERM = 'despejo'
    START_DATE = '01/01/2020'
    END_DATE = '31/12/2020'
    
    #GUI(URL, SEARCH_TERM, CLASS_TERM, START_DATE, END_DATE)
    
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--headless')
    
    try:
        DRIVER = webdriver.Chrome(PATH, chrome_options=OPTIONS)
        DRIVER.get(URL)
        
    except WebDriverException:
        OPTIONS.binary_location = 'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        DRIVER = webdriver.Chrome(PATH, chrome_options=OPTIONS)
        DRIVER.get(URL)
    
    SEARCHBAR = DRIVER.find_element_by_id('iddadosConsulta.pesquisaLivre')
    SEARCHBAR.send_keys(SEARCH_TERM)
    
    CLASS = DRIVER.find_element_by_id('classe_selectionText')
    CLASS.send_keys(CLASS_TERM)
    
    FROM = DRIVER.find_element_by_id('iddadosConsulta.dtInicio')
    FROM.send_keys(START_DATE)
    TO = DRIVER.find_element_by_id('iddadosConsulta.dtFim')
    TO.send_keys(END_DATE)
    
    CONSULT = DRIVER.find_element_by_id('pbSubmit')
    CONSULT.click()
    
    PARSEURL = DRIVER.current_url()
    PARSE = requests.request('GET', PARSEURL)
    
    print(PARSE)
    
    DRIVER.quit()
    
if __name__ == '__main__':
    main()