# hello-bot

A simple hello-world agent on [Norns](https://github.com/amackera/norns). Demonstrates how to build a worker and client using the [norns Python SDK](https://github.com/amackera/norns-sdk-python).

## Quickstart

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- [Norns](https://github.com/amackera/norns) running locally (`docker compose up`)

### Environment

Create a `.env` file (loaded automatically via direnv):

```sh
NORNS_API_KEY=<your norns api key>
ANTHROPIC_API_KEY=<your anthropic api key>
```

### Install

```sh
uv sync
```

### Run

Start the worker:

```sh
uv run hello-worker
```

In another terminal, send a message via the client:

```sh
uv run hello-client
```

## License

MIT
