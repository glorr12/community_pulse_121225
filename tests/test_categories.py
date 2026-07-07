import os

os.environ['FLASK_ENV'] = 'testing'

from app import create_app
from app.models import db


def make_client():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app.test_client(), app


def test_create_category():
    client, app = make_client()
    resp = client.post('/categories/', json={'name': 'Politics'})

    assert resp.status_code == 201
    data = resp.get_json()
    assert data['name'] == 'Politics'
    assert 'id' in data


def test_list_categories():
    client, app = make_client()
    client.post('/categories/', json={'name': 'Politics'})
    client.post('/categories/', json={'name': 'Sports'})

    resp = client.get('/categories/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['count'] == 2


def test_update_category():
    client, app = make_client()
    created = client.post('/categories/', json={'name': 'Politics'}).get_json()

    resp = client.put(f"/categories/{created['id']}", json={'name': 'World Politics'})
    assert resp.status_code == 200
    assert resp.get_json()['name'] == 'World Politics'


def test_delete_category():
    client, app = make_client()
    created = client.post('/categories/', json={'name': 'Politics'}).get_json()

    resp = client.delete(f"/categories/{created['id']}")
    assert resp.status_code == 204

    resp = client.get(f"/categories/{created['id']}")
    assert resp.status_code == 404


def test_get_missing_category_returns_404():
    client, app = make_client()
    resp = client.get('/categories/9999')
    assert resp.status_code == 404
