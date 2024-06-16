import os
import requests
import json
import yaml

# Конфигурация Zabbix
ZABBIX_URL = 'http://IP:PORT/api_jsonrpc.php'
API_TOKEN = 'TOKEN'
HEADERS = {
    'Content-Type': 'application/json-rpc',
    'Authorization': f'Bearer {API_TOKEN}'
}

# Путь к основной директории с шаблонами
TEMPLATES_DIR = 'PATH to templates'

def import_template(template_data):
    import_payload = {
        'jsonrpc': '2.0',
        'method': 'configuration.import',
        'params': {
            'format': 'yaml',
            'rules': {
                'templates': {
                    'createMissing': True,
                    'updateExisting': True
                }
            },
            'source': template_data
        },
        'auth': None,  # Токен уже включен в заголовок
        'id': 1
    }
    import_response = requests.post(ZABBIX_URL, headers=HEADERS, data=json.dumps(import_payload))
    result = import_response.json()
    if 'error' in result:
        raise Exception(f"Error importing template: {result['error']['data']}")
    return result

def main():
    for root, dirs, files in os.walk(TEMPLATES_DIR):
        for filename in files:
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                file_path = os.path.join(root, filename)
                print(f"Processing file: {file_path}")
                with open(file_path, 'r') as file:
                    template_data = file.read()
                    try:
                        result = import_template(template_data)
                        #print(f"Successfully imported template from {file_path}: {result}")
                    except Exception as e:
                        print(f"Failed to import template from {file_path}: {e}")

if __name__ == "__main__":
    main()

