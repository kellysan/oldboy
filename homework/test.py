import  requests




def get_url_status(url):
   con = requests.get(url)
   return con.status_code


def run():
    url_list = ["http://www.baidu.com", "http://www.163.com"]
    for url in url_list:
        status = get_url_status(url)
        if status == 200:
            print("{} 正常".format(url))
        else:
            print("{} 异常".format(url))


if __name__ == '__main__':
    run()