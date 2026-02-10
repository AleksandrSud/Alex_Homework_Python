import requests


class CompanyApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить список компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url+'/company/'+str(id))
        return resp.json()

    # Получить токен авторизации
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    # Добавить компанию:
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company/create',
                             json=company)
        return resp.json()
