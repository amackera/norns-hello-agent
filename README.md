# hello-bot

A simple hello-world agent on [Norns](https://github.com/nornscode/norns). Demonstrates how to build a worker and client using the [norns Python SDK](https://github.com/nornscode/norns-sdk-python).

## Quickstart

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- [nornsctl](https://github.com/nornscode/nornsctl) CLI

### Run

Start a local Norns server:

```sh
brew install nornscode/tap/nornsctl
nornsctl dev
```

Start the worker:

```sh
uv sync
uv run hello-worker
```

In another terminal, send a message via the client:

```sh
uv run hello-client
```

## License

MIT
