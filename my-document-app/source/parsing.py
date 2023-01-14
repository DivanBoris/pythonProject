import requests
from bs4 import BeautifulSoup
import ssl
from time import sleep

def parse_ssr():
    sleep(3.3)
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-Us; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}
    url = "https://www.marinetraffic.com/vesselDetails/latestPosition/shipid:339942"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
def main():
    parse_ssr()


if __name__ == '__main__':
    main()
















# def get_request(id):
#     api_key = '4bd75bbc69f5b22bf5b44c46a35e449999a0cfeb'
#     params = {'shipid': id, 'v': '1'}
#     command = requests.get(f'https://services.marinetraffic.com/api/exportvessel/{api_key}', params=params)
#     if command.status_code == 200:
#         return command.text
#     if command.status_code != 200:
#         return "Error with the vessel determination"