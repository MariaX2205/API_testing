from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    BASE_URL = 'https://httpbin.org'

    def list_html(self):
        # method: get
        # routs: /html
        # status: 200

        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots_txt(self):
        # mehod: get
        # routs: /robots.txt
        # status: 200
        url = self.BASE_URL + "/robots.txt"
        return self.get(url)

    def bin_org(self):
        # method: get
        # routs: /robots.txt
        # status: 200
        url = self.BASE_URL + "/ip"
        return self.get(url)


http_bin_api = HttpBinApi()
