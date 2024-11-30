import requests

session_id = "0fb2b2f9-ccf3-4425-868e-4c7deb0e8b20"

url = "https://hackdiversity.xyz/api/navigation/routes"
headers = {"Authorization": f"Bearer {session_id}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    routes = response.json()

def filter_accessible_routes(routes):
    accessible_routes = []
    for route in routes:
        if route.get("accessible", False):
            accessible_routes.append(route)
    return accessible_routes


