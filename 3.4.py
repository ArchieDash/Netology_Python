from urllib.parse import urlencode
import requests


class YandexMetricaUser:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Authorization": "OAuth {}".format(self.token),
            "Content_Type": "application/json"
        }

    def get_counter(self):
        headers = self.get_headers()
        response = requests.get("https://api-metrika.yandex.ru/management/v1/counters", headers=headers,
                                params={"pretty": 1}).json()
        return response["counters"][0]["id"]


class Counter(YandexMetricaUser):

    @property
    def get_counter_visits(self):
        headers = self.get_headers()
        params = {
            "id": YandexMetricaUser.get_counter(self),
            "metrics": "ym:s:visits"
        }
        response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", params, headers=headers)
        return response.json()

    @property
    def get_counter_views(self):
        headers = self.get_headers()
        params = {
            "id": YandexMetricaUser.get_counter(self),
            "metrics": "ym:s:pageviews"
        }
        response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", params, headers=headers)
        return response.json()

    @property
    def get_counter_users(self):
        headers = self.get_headers()
        params = {
            "id": YandexMetricaUser.get_counter(self),
            "metrics": "ym:s:users"
        }
        response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", params, headers=headers)
        return response.json()


def main():
    app_id = "49121f1b1940443bbbf77f890338ef05"
    auth_url = "https://oauth.yandex.ru/authorize"
    auth_url_data = {
        "response_type": "token",
        "client_id": app_id
    }
    print("?".join((auth_url, urlencode(auth_url_data))))
    token = input("Type your token:")
    counter = Counter(token)
    visits = counter.get_counter_visits
    views = counter.get_counter_views
    users = counter.get_counter_users
    print("Total visits: {}".format(int(visits["totals"][0])))
    print("Total views: {}".format(int(views["totals"][0])))
    print("Total users: {}".format(int(users["totals"][0])))


main()