import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_create_task():
    response = requests.post(f'{BASE_URL}/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task'
    })
    print('Create Task:', response.json())
    assert response.status_code == 201

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    print('Get Tasks:', response.json())
    assert response.status_code == 200

def test_update_task():
    response = requests.put(f'{BASE_URL}/tasks/1', json={
        'title': 'Updated Task',
        'description': 'This is an updated test task',
        'done': True
    })
    print('Update Task:', response.json())
    assert response.status_code == 200

def test_delete_task():
    response = requests.delete(f'{BASE_URL}/tasks/1')
    print('Delete Task:', response.status_code)
    assert response.status_code == 204

def run_tests():
    test_create_task()
    test_get_tasks()
    test_update_task()
    test_delete_task()

if __name__ == '__main__':
    run_tests()