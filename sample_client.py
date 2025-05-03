import asyncio
import asyncclick as click  # Using asyncclick for async main
from a2a_common.utils.color_logging import colorize
from a2a_common.client import A2AClient
from uuid import uuid4


@click.command()
@click.option(
    "--agent-url",
    default="http://localhost:10003",  # Default to the port used in server __main__
    help="URL of the PocketFlow A2A agent server.",
)
async def main(agent_url: str):
    print(colorize("bright_magenta", f"Connecting to agent at: {agent_url}"))
    a2a_client = A2AClient(url=agent_url)
    sessionId = uuid4().hex  # Generate a new session ID for this run
    print(colorize("gray", f"Using Session ID: {sessionId}"))
    agent_card = await a2a_client.get_agent_card()
    print(colorize("green", f"Agent card: {agent_card}"))


if __name__ == "__main__":
    asyncio.run(main())
