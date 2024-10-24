# GitHub Key Management System

This is a Python script to manage SSH keys on your GitHub account. It allows you to create, list, and delete SSH keys using the GitHub API.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pwphs/key-sys.git
    cd key-sys
    ```

2. Install the required dependencies:
    ```sh
    pip install requests
    ```

## Usage

To use this script, you need to have a GitHub personal access token with the appropriate permissions to manage SSH keys.

### Command Line Usage

1. **Create a new SSH key:**
    ```sh
    python key.py <token> create <title> <key>
    ```
    - `<token>`: Your GitHub personal access token.
    - `<title>`: The title for the new SSH key.
    - `<key>`: The SSH key content.

    Example:
    ```sh
    python key.py ghp_yourtokenhere create "My Laptop Key" "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr..."
    ```

2. **List all SSH keys:**
    ```sh
    python key.py <token> list
    ```
    - `<token>`: Your GitHub personal access token.

    Example:
    ```sh
    python key.py ghp_yourtokenhere list
    ```

3. **Delete an SSH key:**
    ```sh
    python key.py <token> delete <key_id>
    ```
    - `<token>`: Your GitHub personal access token.
    - `<key_id>`: The ID of the SSH key to delete.

    Example:
    ```sh
    python key.py ghp_yourtokenhere delete 12345678
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



