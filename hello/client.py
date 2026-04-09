import os
from norns import NornsClient


def main():
    client = NornsClient(os.environ.get("NORNS_URL", "http://localhost:4001"), api_key=os.environ["NORNS_API_KEY"])

    # Send a message and wait for the result
    result = client.send_message("hello-bot", "Hello, I'm Anson.", wait=True, timeout=60)
    print(f"Run {result.run_id}: {result.status}")
    print(f"Output: {result.output}")

    # Send a follow-up
    # result2 = client.send_message("hello-bot", "Hello, I'm Alex.", wait=True, timeout=60)
    # print(f"Run {result2.run_id}: {result2.status}")
    # print(f"Output: {result2.output}")


if __name__ == "__main__":
    main()
