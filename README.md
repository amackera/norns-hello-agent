# Mimir

Product knowledge agent on [Norns](https://github.com/amackera/norns). Ask it how features work, when things ship, how to flip a flag — it searches your docs and remembers what you tell it.

Uses the [norns Python SDK](https://github.com/amackera/norns-sdk-python).

## Architecture

Mimir is a norns worker. Norns orchestrates; Mimir does the actual LLM calls and tool execution.

```
User (Slack, CLI, API)
  │
  ▼
NornsClient.send_message() ──────────► Norns Server (orchestrator)
                                            │
                                            │ dispatches tasks
                                            ▼
                                      Mimir Worker (Python)
                                        ├── LLM calls (Anthropic)
                                        └── Tool execution
                                             ├── search_knowledge
                                             ├── remember
                                             └── search_memory
```

Two SDK entry points:
- `norns.Norns` — the worker. Connects via WebSocket, handles LLM and tool tasks.
- `norns.NornsClient` — the client. Sends messages, polls runs, streams events.

## v0

Keeping it simple:

- One Python worker, three tools
- Markdown files as the knowledge source (keyword search, no vector DB yet)
- `/remember` for ad-hoc facts that stick across conversations
- CLI to ask questions
- Runs in conversation mode so follow-ups work

Details in [docs/v0-plan.md](docs/v0-plan.md) and [docs/design.md](docs/design.md).

## Setup

- Python 3.14+
- [Norns](https://github.com/amackera/norns) running locally (`docker compose up`)
- `ANTHROPIC_API_KEY`

## Status

Design and planning done. Implementation not started yet.

Next up:
1. Wire up the worker + client with `norns-sdk`
2. Build markdown loader + `search_knowledge` tool
3. Build `/remember` + `search_memory` tool

## License

MIT
