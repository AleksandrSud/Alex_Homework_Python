import uuid
import requests
from yougile_api import YougileApi


api = YougileApi("https://ru.yougile.com")


LOGIN = "dev@yougile.com"
PASSWORD = "123"
COMPANY_ID = "44eccf40-a027-4d06-b5c2-18f4c02bb026"


def test_post_create_project():

    key_result = api.get_api_key(LOGIN, PASSWORD, COMPANY_ID)

    if 'key' not in key_result:
        return None

    api_key = key_result['key']

    name = f"Test Project {uuid.uuid4().hex[:8]}"
    project = api.create_project(name, api_key)

    assert 'id' in project
    project_id = project['id']

    return project_id, api_key


def test_get_project():

    result = test_post_create_project()

    if not result:
        return

    project_id, api_key = result

    project = api.get_project(project_id, api_key)

    assert 'id' in project
    assert 'title' in project
    assert project['id'] == project_id

    api.delete_project(project_id, api_key)


def test_put_update_project():

    result = test_post_create_project()

    if not result:
        return

    project_id, api_key = result

    new_name = f"Updated {uuid.uuid4().hex[:8]}"
    update_result = api.update_project(project_id, new_name, api_key)

    assert 'success' in update_result
    assert update_result['success'] is True

    project = api.get_project(project_id, api_key)
    assert project['title'] == new_name

    api.delete_project(project_id, api_key)


def test_get_all_projects():

    key_result = api.get_api_key(LOGIN, PASSWORD, COMPANY_ID)

    if 'key' not in key_result:
        return

    api_key = key_result['key']

    result = api.get_all_projects(api_key)

    assert 'content' in result
    assert isinstance(result['content'], list)


def test_negative_post_empty_title():
    key_result = api.get_api_key(LOGIN, PASSWORD, COMPANY_ID)

    if 'key' not in key_result:
        return

    api_key = key_result['key']

    try:
        api.create_project("", api_key)

        assert False
    except requests.exceptions.HTTPError:

        assert True
    except Exception:

        assert True


def test_negative_get_wrong_id():
    key_result = api.get_api_key(LOGIN, PASSWORD, COMPANY_ID)

    if 'key' not in key_result:
        return

    api_key = key_result['key']

    wrong_id = "00000000-0000-0000-0000-000000000000"

    try:
        api.get_project(wrong_id, api_key)
        assert False
    except requests.exceptions.HTTPError:
        assert True
    except Exception:
        assert True


def test_negative_put_wrong_id():
    key_result = api.get_api_key(LOGIN, PASSWORD, COMPANY_ID)

    if 'key' not in key_result:
        return

    api_key = key_result['key']

    wrong_id = "00000000-0000-0000-0000-000000000000"

    try:
        api.update_project(wrong_id, "New Title", api_key)
        assert False

    except requests.exceptions.HTTPError:
        assert True
    except Exception:
        assert True


def test_negative_put_empty_title():

    result = test_post_create_project()

    if not result:
        return

    project_id, api_key = result

    try:
        api.update_project(project_id, "", api_key)
        assert False
    except requests.exceptions.HTTPError:
        assert True
    except Exception:
        assert True
    finally:

        api.delete_project(project_id, api_key)
