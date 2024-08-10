# Run this file first and then start running the client requests separately.
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['POST'])
def proxy():
    request_data = request.get_json()
    
    method = request_data.get('method', 'POST')
    request_url = request_data.get('request_url')
    headers = request_data.get('headers', {})
    body = request_data.get('body', {})

    if method == 'POST':
        response = requests.post(request_url, headers=headers, json=body)
    elif method == 'GET':
        response = requests.get(request_url, headers=headers, params=body)
    elif method == 'PUT':
        response = requests.put(request_url, headers=headers, json=body)
    elif method == 'DELETE':
        response = requests.delete(request_url, headers=headers, json=body)
    else:
        return jsonify({'error': 'Unsupported HTTP method'}), 400
    
    return jsonify({
        'status_code': response.status_code,
        'headers': dict(response.headers),
        'body': response.json() if response.content else None
    })

if __name__ == '__main__':
    app.run(port=8083)