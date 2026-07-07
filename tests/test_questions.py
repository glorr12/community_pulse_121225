import os

os.environ['FLASK_ENV'] = 'testing'

from app import create_app
from app.models import Question, Category, db


def make_client():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app.test_client(), app


def create_category(client, name='General'):
    resp = client.post('/categories/', json={'name': name})
    return resp.get_json()['id']


def test_create_question():
    client, app = make_client()
    category_id = create_category(client)
    resp = client.post('/questions/', json={'text': 'How are you?', 'category_id': category_id})

    assert resp.status_code == 201
    data = resp.get_json()
    assert data['text'] == 'How are you?'
    assert data['category']['id'] == category_id
    assert 'id' in data



def test_create_question_with_spaces():
    client, app = make_client()
    category_id = create_category(client)
    resp = client.post('/questions/', json={'text': '       How are you, BRO?     ', 'category_id': category_id})

    assert resp.status_code == 201
    data = resp.get_json()
    assert data['text'] == 'How are you, BRO?'
    assert 'id' in data


def test_create_question_requires_category():
    client, app = make_client()
    resp = client.post('/questions/', json={'text': 'No category here'})

    assert resp.status_code == 400


def test_list_questions():
    client, app = make_client()
    category_id = create_category(client)

    resp = client.post('/questions/', json={'text': 'Question 1', 'category_id': category_id})
    resp = client.post('/questions/', json={'text': 'Question 2', 'category_id': category_id})


    resp = client.get('/questions/')
    assert resp.status_code == 200
    data = resp.get_json()

    assert data['count'] == 2
    assert data['items'][0]['category']['id'] == category_id
