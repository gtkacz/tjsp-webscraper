import pandas as pd
from selenium import webdriver
from tkinter import Tk
from pathlib import Path

def main():
    CUR_DIR = Path(__file__).parent
    PROGRAM = 'chromedriver.exe'
    PATH = CUR_DIR / PROGRAM
    
    URL = 'https://esaj.tjsp.jus.br/cjpg/'
    SEARCH_TERM = 'covid'
    CLASS_TERM = 'despejo'
    START_DATE = '01/01/2020'
    END_DATE = '31/12/2020'
    
    try:
        DRIVER = webdriver.Chrome(PATH)
        DRIVER.get(URL)
        
    except:
        OPTIONS = webdriver.ChromeOptions()
        OPTIONS.binary_location = 'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        DRIVER = webdriver.Chrome(PATH, chrome_options=OPTIONS)
        DRIVER.get(URL)
    
    SEARCHBAR = DRIVER.find_element_by_id('iddadosConsulta.pesquisaLivre')
    SEARCHBAR.send_keys(SEARCH_TERM)
    
    CLASS = DRIVER.find_element_by_id('classe_selectionText')
    CLASS.send_keys(CLASS_TERM)
    
    FROM = DRIVER.find_element_by_id("iddadosConsulta.dtInicio")
    FROM.send_keys(START_DATE)
    TO = DRIVER.find_element_by_id("iddadosConsulta.dtFim")
    TO.send_keys(END_DATE)
    
    #DRIVER.quit()
    
if __name__ == "__main__":
    main()