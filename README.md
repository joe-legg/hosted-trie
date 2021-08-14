# Trie
An implementation of a trie.
Currently hosted at `https://hosted-trie.herokuapp.com`.

Dependencies:
- FastAPI
- requests
- pytest
- uvicorn

## Starting the server
Run the following command to start the server.
```bash
uvicorn server:api --port 8000
```

## API Documentation
Start the server then go to http://127.0.0.1:8000/docs

## Testing
Run `pytest` to test the API.

## Using the CLI
The CLI provides the following commands:
- `./cli.py --help` print help
- `./cli.py insert <keyword>` insert a new keyword into the trie
- `./cli.py delete <keyword>` delete a keyword from the trie
- `./cli.py search <keyword>` check if a keyword exists in the trie
- `./cli.py suggest <keyword>` get autocomplete suggestions for a prefix
- `./cli.py list <keyword>` get a list of all the words in the trie
