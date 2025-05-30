# mcp

Some tests with pydantic_ai & mcp.

For g4f (need to patch pydantic):

- I had to patch `pydantic/main.py` (see the file `patch_pydantic_main_fix.py`)
- However, g4f does not seem to work with mcp
- It works perfectly with a real Gemini (and probably also with GPT/Claude)


## Setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

## 2 mcp server tests

### mcp-server-test

The "mcp-server-test" directory (created with https://github.com/modelcontextprotocol/create-python-server?tab=readme-ov-file) is managed via 'uv' (it has its own .venv). To activate it in the console:

    $ cd mcp-server-test
    $ uv sync --dev --all-extras
    $ uv run mcp-server-test

### mcp2-server-test

The "mcp2-server-test" is as mcp server using fastmcp (it is managed via 'uv' too (it has its own .venv))
