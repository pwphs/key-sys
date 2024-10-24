import requests

class GitHubKeySystem:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"

    def get_headers(self):
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def create_key(self, title, key):
        url = f"{self.base_url}/user/keys"
        headers = self.get_headers()
        data = {
            "title": title,
            "key": key
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    def list_keys(self):
        url = f"{self.base_url}/user/keys"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def delete_key(self, key_id):
        url = f"{self.base_url}/user/keys/{key_id}"
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            return {"message": "Key deleted successfully"}
        else:
            response.raise_for_status()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python key.py <token> <command> [<args>]")
        sys.exit(1)

    token = sys.argv[1]
    command = sys.argv[2]
    key_system = GitHubKeySystem(token)

    if command == "create":
        if len(sys.argv) != 5:
            print("Usage: python key.py <token> create <title> <key>")
            sys.exit(1)
        title = sys.argv[3]
        key = sys.argv[4]
        result = key_system.create_key(title, key)
        print(result)
    elif command == "list":
        result = key_system.list_keys()
        print(result)
    elif command == "delete":
        if len(sys.argv) != 4:
            print("Usage: python key.py <token> delete <key_id>")
            sys.exit(1)
        key_id = sys.argv[3]
        result = key_system.delete_key(key_id)
        print(result)
    else:
        print("Unknown command")
        sys.exit(1)



