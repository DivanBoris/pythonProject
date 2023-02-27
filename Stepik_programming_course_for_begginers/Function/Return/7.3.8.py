def get_domain_name(url):
    delete = ['https://www.', 'http://www.', 'www.', 'http://', 'http://', 'https://', '.com', '.co.jp', '.ru']
    for i in delete:
        if i in url:
            url = url.replace(i, '/\/')
    url = url.split('/\/')
    return url[1]


print(get_domain_name("http://google.com"))
