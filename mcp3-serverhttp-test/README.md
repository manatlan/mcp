using fastmcp/http


# dev

    $ deactivate 
    $ uv sync
    $ uv run fastmcp dev server.py

# run 

    $ uv run server.py

or

    $ uv run fastmcp run server.py --transport streamable-http --port 4200