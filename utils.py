from tkinter import Tk, ttk
from tkcalendar import DateEntry
from html.parser import HTMLParser
import re

def GUI(URL = 'https://esaj.tjsp.jus.br/cjpg/', SEARCH_TERM = 'covid', CLASS_TERM = 'despejo', START_DATE = '01/01/2020', END_DATE = '31/12/2020', TIMEOUT = 10):
    window = Tk()
    window.title('TJSP Webscrapper')
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')
    
    URL_FINAL, SEARCH_TERM_FINAL, CLASS_TERM_FINAL, START_DATE_FINAL, END_DATE_FINAL, TIMEOUT_FINAL = URL, SEARCH_TERM, CLASS_TERM, START_DATE, END_DATE, TIMEOUT
    
    URL_ENTRY = ttk.Entry(justify = 'center', exportselection = 0, cursor = 'arrow')
    URL_ENTRY.insert(-1, URL)
    URL_ENTRY.configure(state='disabled')
    URL_LABEL = ttk.Label(text = 'Insira o URL:', justify = 'center')
    
    SEARCH_TERM_ENTRY = ttk.Entry(justify = 'center', exportselection = 0)
    SEARCH_TERM_ENTRY.insert(-1, SEARCH_TERM)
    SEARCH_TERM_LABEL = ttk.Label(text = 'Insira o termo da pesquisa livre:', justify = 'center')
    
    CLASS_TERM_ENTRY = ttk.Entry(justify = 'center', exportselection = 0)
    CLASS_TERM_ENTRY.insert(-1, CLASS_TERM)
    CLASS_TERM_ENTRY.configure(state='disabled')
    CLASS_TERM_LABEL = ttk.Label(text = 'Insira a classe:', justify = 'center')
    
    START_DATE_ENTRY = ttk.Entry(justify = 'center', exportselection = 0)
    #START_DATE_ENTRY = DateEntry()
    START_DATE_ENTRY.insert(-1, START_DATE)
    START_DATE_LABEL = ttk.Label(text = 'Insira a data inicial:', justify = 'center')
    
    END_DATE_ENTRY = ttk.Entry(justify = 'center', exportselection = 0)
    #END_DATE_ENTRY = DateEntry()
    END_DATE_ENTRY.insert(-1, END_DATE)
    END_DATE_LABEL = ttk.Label(text = 'Insira a data final:', justify = 'center')
    
    TIMEOUT_ENTRY = ttk.Entry(justify = 'center', exportselection = 0)
    TIMEOUT_ENTRY.insert(-1, '10')
    TIMEOUT_LABEL = ttk.Label(text = 'Insira o tempo máximo de\nespera pelo servidor (s):', justify = 'center')
        
    def isClickedFunction():
        nonlocal URL_FINAL, SEARCH_TERM_FINAL, CLASS_TERM_FINAL, START_DATE_FINAL, END_DATE_FINAL, TIMEOUT_FINAL
        
        URL_FINAL = URL_ENTRY.get()
        SEARCH_TERM_FINAL = SEARCH_TERM_ENTRY.get()
        CLASS_TERM_FINAL = CLASS_TERM_ENTRY.get()
        START_DATE_FINAL = START_DATE_ENTRY.get()
        END_DATE_FINAL = END_DATE_ENTRY.get()
        TIMEOUT_FINAL = int(TIMEOUT_ENTRY.get())
        
        window.destroy()
    
    BUTTON = ttk.Button(text = 'Pesquisar', command = isClickedFunction)
    
    URL_LABEL.grid(row=0, column=0, pady=10)
    URL_ENTRY.grid(row=1, column=0, padx=25)
    
    SEARCH_TERM_LABEL.grid(row=0, column=1, pady=10)
    SEARCH_TERM_ENTRY.grid(row=1, column=1, padx=25)
    
    CLASS_TERM_LABEL.grid(row=0, column=2, pady=10)
    CLASS_TERM_ENTRY.grid(row=1, column=2, padx=25)
    
    START_DATE_LABEL.grid(row=2, column=0, pady=10)
    START_DATE_ENTRY.grid(row=3, column=0, padx=25)
    
    END_DATE_LABEL.grid(row=2, column=1, pady=10)
    END_DATE_ENTRY.grid(row=3, column=1, padx=25)
    
    TIMEOUT_LABEL.grid(row=2, column=2, pady=10)
    TIMEOUT_ENTRY.grid(row=3, column=2, padx=25)
    
    BUTTON.grid(row=4, column=1, pady=15)
    
    window.mainloop()
    
    return URL_FINAL, SEARCH_TERM_FINAL, CLASS_TERM_FINAL, START_DATE_FINAL, END_DATE_FINAL, TIMEOUT_FINAL

def process_PDF(text):
    pass

class TJSPParser(HTMLParser):
    def __init__(self):
        super().__init__()
        
    def handle_starttag(self, TAG: str, ATTRS: list):
        if TAG == 'tr':
            pass
            
def tag_cleanup(html):
    html = str(html)
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', html)

if __name__ == '__main__':
    GUI()