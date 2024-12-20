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

def insertion_sort(routes):
    n = len(routes)
    for i in range(1, n):
        key = routes[i]
        j = i - 1
        while j >= 0 and routes[j]['distance'] > key['distance']:
            routes[j + 1] = routes[j]
            j -= 1
        routes[j + 1] = key
    return routes

# test_url = "https://hackdiversity.xyz/api/test/mockRoutes"
# test_response = requests.get(test_url, headers=headers)
# mock_routes = test_response.json()
# accessible_routes = filter_accessible_routes(mock_routes)
# sorted_routes = insertion_sort(accessible_routes)
# print("Sorted Accessible Routes:", sorted_routes)


accessible_routes = filter_accessible_routes(routes)
sorted_routes = insertion_sort(accessible_routes)
#print("Sorted Accessible Routes:", sorted_routes)


# submit_url = "https://hackdiversity.xyz/api/test/submit-sorted-routes"
# submission = {"routes": sorted_routes}
# submit_response = requests.post(submit_url, json=submission, headers=headers)
# print(f"Response Status Code: {submit_response.status_code}")
# print(f"Response Text: {submit_response.text}")
# if submit_response.status_code == 200:
#     print("Test Submission Success:", submit_response.json())

final_submission_url = "https://hackdiversity.xyz/api/navigation/sorted_routes"
submission = submission = {"routes": sorted_routes}
submit_reponse = requests.post (final_submission_url, json=submission, headers=headers)


status_url = "https://hackdiversity.xyz/api/navigation/status"
status_response = requests.get(status_url, headers={"Authorization": f"Bearer {session_id}"})
if status_response.status_code == 200:
    print("Submission Status:", status_response.json())

