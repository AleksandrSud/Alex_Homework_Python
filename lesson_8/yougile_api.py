import requests


class YougileApi:
    def __init__(self, base_url="https://ru.yougile.com"):
        self.base_url = base_url

    # POST: Получить API ключ
    def get_api_key(self, login, password, company_id):
        url = f"{self.base_url}/api-v2/auth/keys"
        data = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        resp = requests.post(url, json=data)
        return resp.json()

    # POST: Создать проект
    def create_project(self, title, api_key):
        url = f"{self.base_url}/api-v2/projects"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {"title": title}
        resp = requests.post(url, json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    # GET: Получить проект по ID
    def get_project(self, project_id, api_key):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        headers = {'Authorization': f'Bearer {api_key}'}
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

    # PUT: Обновить проект
    def update_project(self, project_id, title, api_key):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {"title": title}
        resp = requests.put(url, json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    # DELETE: Удалить проект (только для очистки в тестах)
    def delete_project(self, project_id, api_key):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        headers = {'Authorization': f'Bearer {api_key}'}
        resp = requests.delete(url, headers=headers)
        return resp.json()

    # GET: Получить все проекты
    def get_all_projects(self, api_key):
        url = f"{self.base_url}/api-v2/projects"
        headers = {'Authorization': f'Bearer {api_key}'}
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()
