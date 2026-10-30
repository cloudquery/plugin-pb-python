# plugin-pb-python

This is a low-level auto-generated gRPC client and server for CloudQuery plugin from [plugin-pb protos](https://github.com/cloudquery/plugin-pb).

## Development

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)

### Install dependencies

```bash
uv sync
```

### Regenerate gRPC code

```bash
make clone-proto # This is needed only once
make gen
```
