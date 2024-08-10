import requests

proxy_url = 'http://127.0.0.1:8083/proxy'
data = {
    'method': 'DELETE',
    'request_url': 'https://jsonplaceholder.typicode.com/posts/1',
    'headers': {
        'Content-Type': 'application/json'
    }
}


try:
        response = requests.post(proxy_url, json=data)
        response.raise_for_status() 
        response_json = response.json()
        print("Response JSON:")
        print(f"Status Code: {response_json.get('status_code')}")
        print("Headers:")
        for key, value in response_json.get('headers', {}).items():
            print(f"  {key}: {value}")
        print("Body:")
        print(response_json.get('body'))
except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
except Exception as err:
        print(f"An error occurred: {err}")
