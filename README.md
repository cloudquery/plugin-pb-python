# plugin-pb-python

This is a low-level auto-generated gRPC client and server for CloudQuery plugin from [plugin-pb protos](https://github.com/cloudquery/plugin-pb).

## Development

### Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)

we recommend using virtualenv to manage your python environment.

```bash
virtualenv -p python3.7 venv # or any python >= 3.7
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Regenerate gRPC code

```bash
make clone-proto # This is needed only once
make gen
```

