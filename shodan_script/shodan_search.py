import shodan
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get the Shodan API key from environment variables
SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

# Initialize the Shodan API
api = shodan.Shodan(SHODAN_API_KEY)


def get_user_input():
    """Prompt the user for a search query."""
    return input("Enter the search query: ")


def run_search(query):
    """Run the Shodan search."""
    try:
        return api.search(query)
    except shodan.APIError as e:
        print(f"Error: {e}")
        return None


def check_vulnerabilities(results):
    """Check for vulnerabilities in the search results."""
    return [result for result in results['matches'] if 'vuln' in result]


def save_results_to_file(results, filename='results.json'):
    """Save the first 10 results to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(results[:10], file)
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"File error: {e}")


def refine_results(results):
    """Refine the results to include only specific fields."""
    return [
        {
            'ip': result['ip_str'],
            'port': result['port'],
            'organization': result.get('org', 'N/A'),
            'hostnames': result.get('hostnames', [])
        }
        for result in results[:10]
    ]


def display_results(results):
    """Display the refined results."""
    for result in results:
        print(json.dumps(result, indent=4))


def main():
    """Main function to orchestrate the Shodan search and processing."""
    query = get_user_input()
    results = run_search(query)

    if results:
        check_vulnerabilities(results)
        save_results_to_file(results['matches'])
        refined_results = refine_results(results['matches'])
        display_results(refined_results)


if __name__ == "__main__":
    main()
