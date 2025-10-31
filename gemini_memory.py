from openmemory.client import OpenMemory
import argparse
import sys

class GeminiMemory:
    def __init__(self, api_key='your-secret-api-key-here', base_url='http://localhost:8080'):
        self.om = OpenMemory(api_key=api_key, base_url=base_url)

    def remember(self, fact: str, tags: list = None):
        """Stores a fact in the OpenMemory server."""
        try:
            response = self.om.add(content=fact, tags=tags)
            return response
        except Exception as e:
            print(f"Error remembering fact: {e}")
            return None

    def recall(self, query: str, k: int = 5):
        """Recalls information from the OpenMemory server."""
        try:
            response = self.om.query(query=query, k=k)
            return response['matches']
        except Exception as e:
            import traceback
            print(f"Error recalling information: {e}")
            traceback.print_exc()
            return []

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('--help')

    parser = argparse.ArgumentParser(description="Gemini Memory Command-Line Utility")
    parser.add_argument('--port', type=int, default=8080, help='Port of the OpenMemory server')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    remember_parser = subparsers.add_parser('remember', help='Store a fact in memory.')
    remember_parser.add_argument('fact', type=str, help='The fact to remember.')
    remember_parser.add_argument('--tags', nargs='*', default=[], help='A list of tags for the memory.')

    recall_parser = subparsers.add_parser('recall', help='Recall information from memory.')
    recall_parser.add_argument('query', type=str, help='The query to search for.')
    recall_parser.add_argument('-k', type=int, default=5, help='Number of results to return.')

    status_parser = subparsers.add_parser('status', help='Check the status of the OpenMemory server.')

    args = parser.parse_args()

    memory = GeminiMemory(base_url=f'http://localhost:{args.port}')

    if args.command == 'remember':
        response = memory.remember(args.fact, args.tags)
        if response:
            print("Memory stored successfully:")
            print(response)
        else:
            print("Failed to store memory.")
    elif args.command == 'recall':
        response = memory.recall(args.query, args.k)
        if response:
            print("Recalled memories:")
            for item in response:
                print(f"- {item['content']} (Score: {item['score']})")
        else:
            print("No memories found or an error occurred.")
    elif args.command == 'status':
        try:
            health = memory.om.health()
            if health.get('ok'):
                print("OpenMemory server is running and healthy.")
            else:
                print("OpenMemory server is not responding correctly.")
        except Exception as e:
            print(f"Error connecting to OpenMemory server: {e}")