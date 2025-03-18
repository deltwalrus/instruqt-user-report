#!/usr/bin/env python3
import argparse
import requests
import json

def query_instruqt(api_key):
    endpoint = "https://play.instruqt.com/graphql"
    query = """query {
        teams {
            id
            name
            users {
                id
                node {
                    profile {
                        display_name
                    }
                }
                role
            }
        }
    }"""

    headers = {"Authorization": "Bearer " + api_key}
    response = requests.post(endpoint, headers=headers, json={"query": query})

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        return

    print(f"\n=== Results for API Key: {api_key} ===\n")
    if 'data' in data and 'teams' in data['data']:
        teams = data['data']['teams']
        if teams:
            for team in teams:
                print(f"Team Name: {team['name']} (ID: {team['id']})")
                print("Users:")
                for user in team['users']:
                    display_name = user['node']['profile'].get('display_name') if user.get('node') and user['node'].get('profile') else "No Display Name"
                    role = user.get('role', "No Role")
                    print(f"  - {display_name} (Role: {role})")
                print("\n" + "=" * 50 + "\n")
        else:
            print("No teams found for this API key.")
    else:
        print("Error in response for this API key:")
        print(json.dumps(data, indent=2))

def main():
    parser = argparse.ArgumentParser(
        description="Query Instruqt API for teams and user roles using one or more API keys."
    )
    parser.add_argument(
        "--api-key",
        action="append",
        required=True,
        help="API key for Instruqt API. Use multiple --api-key switches to run for more than one key."
    )
    args = parser.parse_args()

    for key in args.api_key:
        query_instruqt(key)

if __name__ == "__main__":
    main()
