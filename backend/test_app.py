
# pytest automatically injects fixtures
# that are defined in conftest.py
# in this case, client is injected
def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["result"]["content"] == "hello world!"


def test_mirror(client):
    res = client.get("/mirror/Tim")
    assert res.status_code == 200
    assert res.json["result"]["name"] == "Tim"


def test_get_contacts(client):
    res = client.get("/contacts")
    assert res.status_code == 200

    res_users = res.json["result"]["contacts"]
    assert len(res_users) == 4
    assert res_users[0]["name"] == "Angad"


def tests_get_contacts_with_hobby(client):
    res = client.get("/contacts?hobby=weeb")
    assert res.status_code == 200

    res_users = res.json["result"]["contacts"]
    assert len(res_users) == 1
    assert res_users[1]["name"] == "Roy"


def test_get_contacts_id(client):
    res = client.get("/contacts/1")
    assert res.status_code == 200

    res_user = res.json["result"]["contacts"]
    assert res_user["name"] == "Angad"
    assert res_user["hobby"] == "dirty-ing"
