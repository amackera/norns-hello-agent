import logging
import os

from norns import Norns, Agent, tool

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(message)s")

# Connect to the Norns runtime
norns = Norns(os.environ.get("NORNS_URL", "http://localhost:4001"), api_key=os.environ["NORNS_API_KEY"])

# Define tools
@tool
def say_hello(name: str) -> str:
    """Greet someone by name."""
    return f"Hello {name}"

# @tool(side_effect=True)
# def send_email(to: str, subject: str, body: str) -> str:
#     """Send an email to a customer."""
#     smtp.send(to=to, subject=subject, body=body)
#     return f"Email sent to {to}"

# Define an agent
agent = Agent(
    name="hello-bot",
    model="claude-sonnet-5",
    system_prompt=(
        "You are a greeter.\n"
        "If you don't know the person's name, call the ask_human tool to ask for it "
        "and wait for their answer. Don't guess a name.\n"
        "Once you know the name, call the wait tool for 10 seconds, then call the "
        "say_hello tool with that name."
    ),
    tools=[say_hello],
    mode="conversation",
    on_failure="retry_last_step",
)


def main():
    # Run as a worker (blocks forever, like Temporal)
    norns.run(agent, llm_api_key=os.environ["ANTHROPIC_API_KEY"])
    

if __name__ == "__main__":
    main()
