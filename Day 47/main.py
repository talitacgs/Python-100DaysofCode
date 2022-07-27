import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/Monitor-Portable-Plug-Play-Extender-Compatible/dp/B09GJN716F/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.9e69e792-0ff0-4e1a-b10c-a41b9d9b3ffc%3Aamzn1.sym.9e69e792-0ff0-4e1a-b10c-a41b9d9b3ffc&crid=22JMM0U9R6GKZ&cv_ct_cx=monitor%2Bportable&keywords=monitor%2Bportable&pd_rd_i=B09GJN716F&pd_rd_r=b1be3e41-f7b6-4f64-99ae-08aca36ad407&pd_rd_w=JjSlk&pd_rd_wg=hHBrG&pf_rd_p=9e69e792-0ff0-4e1a-b10c-a41b9d9b3ffc&pf_rd_r=06QRC5W66ZG9QYYANGPB&qid=1658886914&sprefix=monitor%2Bportable%2Caps%2C190&sr=1-3-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjRIR0UxU1pWQU02JmVuY3J5cHRlZElkPUEwNjM2Mzc3MkpETVRHMkdFSUVJMCZlbmNyeXB0ZWRBZElkPUEwNTcwNzM0R05DU1c4TDBROTRPJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"

# USER_AGENT and ACCEPT_LANGUAGE from http://myhttpheader.com/
USER_AGENT = os.environ.get("user_agent")
ACCEPT_LANGUAGE = os.environ.get("accept_language")
SET_PRICE = int(100)
MY_EMAIL = "youremail@gmail.com"

headers = {
    "useragent": USER_AGENT,
    "accept_language": ACCEPT_LANGUAGE,
}

response = requests.get(URL, headers=headers)
amazon_html = response.text

soup = BeautifulSoup(amazon_html, 'lxml')
price_text = soup.find(name='span', class_="a-price-whole")
price = int(price_text.getText().replace(',', ""))

name = soup.find(name='span', class_="product-title-word-break").getText()

if price < SET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg= f"Subject: Amazon Price Alert! \n\n{name} is now ${price}\n{URL}"
        )
