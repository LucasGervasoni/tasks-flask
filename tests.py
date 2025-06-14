import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

#create
def test_create_task():
    new_task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])
    
#read
def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert "id" in response_json
        assert response_json['id'] == task_id
        
#update
def test_update_task():
    if tasks:
        task_id = tasks[0]
        updated_data = {
            'title': 'Updated Test Task',
            'description': 'This is an updated test task.',
            'completed': True
        }
        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=updated_data)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

#delete
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        tasks.remove(task_id)