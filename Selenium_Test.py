'''
Created on Dec 28, 2018

@author: Murahari_Kalpam
'''


from selenium import webdriver

def load_browser():
    browser = webdriver.Firefox()
    url = "http://www.amazon.in/"
    browser.get(url)
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    print(innerHTML)


load_browser()


