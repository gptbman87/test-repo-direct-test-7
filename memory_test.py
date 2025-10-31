
from openmemory import OpenMemory
from openmemory import OpenMemory

def main():
    om = OpenMemory(
        base_url="http://localhost:8080",
        api_key="your-secret-api-key-here"
    )

    # Add a memory
    try:
        added = om.add(
            content="The user wants me to have persistent memory.",
            tags=["user-request", "memory", "persistence"]
        )
        print(f"Added memory: {added}")

        # Query memory
        result = om.query(
            query="what does the user want?",
            k=3
        )

        print("Query result:")
        for item in result["matches"]:
            print(f"- {item['content']} (Score: {item['score']})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
