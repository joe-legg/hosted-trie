from fastapi.testclient import TestClient

from server import api

client = TestClient(api)

def test_api():
    # Insert
    res = client.post("/trie/test")
    assert res.status_code == 201
    assert res.json() == { "success": True }

    # Check if exists
    res = client.get("/trie/test")
    assert res.status_code == 200
    assert res.json() == { "keywords": ["test"] }

    # Delete
    res = client.delete("/trie/test")
    assert res.status_code == 200
    assert res.json() == { "success": True }

    # Should not exist after being deleted
    res = client.get("/trie/test")
    assert res.json() == { "keywords": [] }

    # Test autocomplete suggestions

    client.post("/trie/test")
    client.post("/trie/tea")
    client.post("/trie/cake")

    res = client.get("/trie/te")

    assert set(res.json()["keywords"]) == set(["test", "tea"])

    # Test getting a list of all keywords
    res = client.get("/trie")
    assert res.status_code == 200
    assert set(res.json()["keywords"]) == set(["test", "tea", "cake"])
