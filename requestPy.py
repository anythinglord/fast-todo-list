import requests

try:
    # POST
    data = {"title": "New Task", "description": "New Task created", "completed": False}
    post_response = requests.post("http://localhost:8000/api/v1/tasks", json=data)
    post_response.raise_for_status()
    print("\nPOST exitoso:")
    print(post_response.json())
    
except requests.exceptions.HTTPError as errh:
    print(f"Error HTTP: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error de Conexión: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Algo salió mal: {err}")
