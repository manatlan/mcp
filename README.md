# mcp

Some tests with pydantic_ai & mcp.

## Setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

## 4 mcp server tests

### mcp-server-time (package pypi)

An mcp server package, runned on the fly with uvx. see https://pypi.org/project/mcp-server-time/ (stdio)

### mcp-server-test (stdio)

The "mcp-server-test" directory (created with https://github.com/modelcontextprotocol/create-python-server?tab=readme-ov-file) is managed via 'uv' (it has its own .venv). To activate it in the console:

    $ cd mcp-server-test
    $ uv sync --dev --all-extras
    $ uv run mcp-server-test

it uses the low level "mcp" module

### mcp2-server-test (stdio)

The "mcp2-server-test" is as mcp server using fastmcp/stdio (it is managed via 'uv' too (it has its own .venv))

### mcp3-server-test (http)

The "mcp2-server-test" is as mcp server using fastmcp/http (it is managed via 'uv' too (it has its own .venv))

It manages "recettes" ("recipes" in english), and it can:

- add a recipe : title & content
- list all recipes
- produces an image/url (with g4f/image generation) (async method)
- give a recipe (it guess with g4f/text gpt-4o-mini generation) (async method)
