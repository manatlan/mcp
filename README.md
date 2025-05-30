# mcp

qques test pydantic_ai & g4f, avec mcp

pour g4f:

- j'ai du patcher le pydantic/main.py
- mais g4f semble ne pas fonctionner pas avec les mcp
- ca fonctionne nickel avec un vrai gemini (certainement aussi avec un gpt/claude)


## setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Le répertoire "mcp-server-test" (créé avec https://github.com/modelcontextprotocol/create-python-server?tab=readme-ov-file) est géré via 'uv' (il possède sont propre .venv). Pour l'activer en console :

    $ cd mcp-server-test
    $ uv sync --dev --all-extras
    $ uv run mcp-server-test
