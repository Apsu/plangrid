def test_hello(client):
    response = client.get("/", headers={})
    assert response.status_code == 200
    assert b"<p>Hello, World</p>" in response.data

def test_hello_accept(client):
    response = client.get("/", headers={"Accept": "application/json"})
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "Good morning" in data["message"]
