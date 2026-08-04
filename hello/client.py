import os

from norns import NornsClient


def main():
    client = NornsClient(
        os.environ.get("NORNS_URL", "http://localhost:4001"),
        api_key=os.environ["NORNS_API_KEY"],
    )

    # A conversation key keeps every message in this exchange pointed at the
    # same agent process. It matters below: the answer has to reach the agent
    # that asked the question. Without a key, each send_message starts a fresh
    # run instead.
    conversation = "hello-demo"

    result = client.send_message(
        "hello-bot", "Hello!", conversation_key=conversation, wait=True, timeout=60
    )

    # wait=True returns as soon as the agent parks on a question — it can't
    # make progress without you. Answering is just another message.
    while result.is_waiting:
        print(f"\nAgent asks: {result.waiting_for.question}")
        answer = input("> ")
        result = client.send_message(
            "hello-bot", answer, conversation_key=conversation, wait=True, timeout=60
        )

    print(f"\nRun {result.run_id}: {result.status}")
    print(f"Output: {result.output}")


if __name__ == "__main__":
    main()
