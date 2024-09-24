import requests
import sys
from prettytable import PrettyTable

def fetch_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching user: {response.status_code} - {response.reason}")
        sys.exit(1)

    return response.json()

def display_user_info(user):
    table = PrettyTable()
    table.field_names = ["Field", "Value"]

    data = [
        ["Username", user.get("login")],
        ["ID", user.get("id")],
        ["Avatar URL", user.get("avatar_url")],
        ["Profile URL", user.get("html_url")],
        ["Name", user.get("name")],
        ["Bio", user.get("bio")],
        ["Followers", user.get("followers")],
        ["Following", user.get("following")],
    ]

    for row in data:
        table.add_row(row)

    print(table)

def main():
    if len(sys.argv) != 2:
        print("Usage: fetchi <username>")
        sys.exit(1)

    username = sys.argv[1]
    user_info = fetch_user_info(username)
    display_user_info(user_info)

if __name__ == "__main__":
    main()
