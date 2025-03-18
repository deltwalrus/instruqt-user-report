# instruqt-user-report
Python script wrapper for GraphQL query to parse organization(s) for members and their Instruqt roles

## Requirements
`pip` packages:
- `requests`
- `json`
- `argparse`

## Usage
`python user_report.py --api_key team-abcd1234 --api-key team-xyz-5678 ...`

Accepts an arbitrary number (greater than zero) of API keys as arguments and formats output nicely by org.

## Acknowledgements
Harpreet for the initial script and (most improtably) the GraphQL query that makes this go
Adé Mochtar for suggesting this approach
Josh Clough for his guidance on getting this done
