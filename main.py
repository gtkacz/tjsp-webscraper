import urllib.request, time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import Tk, messagebox
from pathlib import Path
from utils import *
from urllib.parse import unquote_plus
from bs4 import BeautifulSoup

def main():
    CUR_DIR = Path(__file__).parent
    PROGRAM = 'chromedriver.exe'
    PATH = CUR_DIR / PROGRAM
    
    URL_FINAL, SEARCH_TERM_FINAL, CLASS_TERM_FINAL, START_DATE_FINAL, END_DATE_FINAL, TIMEOUT = GUI()
    
    OPTIONS = webdriver.ChromeOptions()
    #OPTIONS.add_argument('--headless')
    OPTIONS.add_argument("--window-size=%s" % '1920,1080')
    
    try:
        DRIVER = webdriver.Chrome(PATH, options=OPTIONS)
        DRIVER.get(URL_FINAL)
        
    except WebDriverException:
        OPTIONS.binary_location = 'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        DRIVER = webdriver.Chrome(PATH, options=OPTIONS)
        DRIVER.get(URL_FINAL)
    
    SEARCHBAR = DRIVER.find_element_by_id('iddadosConsulta.pesquisaLivre')
    SEARCHBAR.send_keys(SEARCH_TERM_FINAL)
    
    FROM = DRIVER.find_element_by_id('iddadosConsulta.dtInicio')
    FROM.send_keys(START_DATE_FINAL)
    TO = DRIVER.find_element_by_id('iddadosConsulta.dtFim')
    TO.send_keys(END_DATE_FINAL)
    
    #CLASS = DRIVER.find_element_by_id('classe_selectionText')
    CLASS_SEARCH = DRIVER.find_element_by_id('botaoProcurar_classe')
    CLASS_SEARCH.click()
    
    CONSULT = DRIVER.find_element_by_id('pbSubmit')
    
    try:
        WebDriverWait(DRIVER, TIMEOUT).until(expected_conditions.presence_of_element_located((By.ID, 'classe_treeSelectContainer')))
        
        CLASS_SEARCH_BAR = DRIVER.find_element_by_id('classe_treeSelectFilter')
        CLASS_SEARCH_BUTTON = DRIVER.find_element_by_id('filtroButton')
        CHECKBOX = DRIVER.find_element_by_id('classe_tree_node_8554')
        CONFIRM = DRIVER.find_element_by_class_name('spwBotaoDefaultGrid')
        
        CLASS_SEARCH_BAR.send_keys(CLASS_TERM_FINAL)
        CLASS_SEARCH_BUTTON.click()
        CHECKBOX.click()
        CONFIRM.click()
        CONSULT.click()
        
        try:
            WebDriverWait(DRIVER, TIMEOUT).until(expected_conditions.presence_of_element_located((By.ID, 'divDadosResultado')))
            PARSEURL = DRIVER.current_url
            
            with urllib.request.urlopen(urllib.request.Request(PARSEURL, headers={'User-Agent': 'Chrome'})) as HTML:
                PAGE = HTML.read()
                
            #PAGE = unquote_plus(str(PAGE))
            
            TREE = BeautifulSoup(PAGE, 'lxml')
            #HTML = TREE.prettify()
            
            DATA = [[], [], [], [], [], [], [], []]
            
            for TABLE in TREE.find_all('tr', class_ = 'fundocinza1'):
                for LINE in TABLE.find_all('tr', class_ = 'fonte'):
                    for EXTRA in LINE.find_all('td', attrs = {'align': 'left', 'colspan': '2'}):
                        EXTRA.replaceWith('')
                    for LINE2 in LINE.find_all('td', attrs = {'align': 'left'}):
                        for PROCESS in LINE2.find_all('span', class_ = 'fonteNegrito'):
                            DATA[0].append(tag_cleanup(PROCESS)[1:-1])
                        for CONTENT in LINE2.find_all('strong'):
                            CONTENT.replaceWith('')
                        print('---------------------------------------------------------------------------------------')
                        print(LINE2.prettify())
        
        except TimeoutException:
            DRIVER.quit()
            root = Tk()
            root.withdraw()
            messagebox.showerror('Timeout', 'O site demorou demais para responder, tente novamente.')
            root.destroy()
            
    except TimeoutException:
        DRIVER.quit()
        root = Tk()
        root.withdraw()
        messagebox.showerror('Timeout', 'O site demorou demais para responder, tente novamente.')
        root.destroy()
    
if __name__ == '__main__':
    main()