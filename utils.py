from tkinter import Tk, ttk, StringVar, messagebox
from html.parser import HTMLParser

def GUI(URL, SEARCH_TERM, CLASS_TERM, START_DATE, END_DATE):
    window = Tk()
    window.title('TJSP Webscrapper')
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')
    
    #URL = StringVar(URL)
    #SEARCH_TERM = StringVar(SEARCH_TERM)
    #CLASS_TERM = StringVar(CLASS_TERM)
    #START_DATE = StringVar(START_DATE)
    #END_DATE = StringVar(END_DATE)
    
    url_tk = ttk.Entry(justify = 'center', exportselection = 0)
    
    url_tk.grid(row=2, column=2, padx=25, pady=10)

def process_PDF(text):
    pass

class TJSPParser(HTMLParser):
            def __init__(self):
                super().__init__()
                
            def handle_starttag(self, TAG, ATTRS):
                pass