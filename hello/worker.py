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
    model="claude-sonnet-4-20250514",
    system_prompt="You are a greeter. Your only job is to use the say_hello tool, except you should use it after calling the wait tool and waiting for 10 seconds. After waiting 10 seconds, call the say_hello tool with the person's name, if they provide it. Otherwise, call them 'dude'.",
    tools=[say_hello],
    mode="conversation",
    on_failure="retry_last_step",
)


def main():
    # Run as a worker (blocks forever, like Temporal)
    norns.run(agent, llm_api_key=os.environ["ANTHROPIC_API_KEY"])
    

if __name__ == "__main__":
    main()
