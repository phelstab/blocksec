# Blockchain Security Lecture Book Repository

This is a lecture book for the IT-security topic, security of blockchains.

## Usage

### Building the book

```sh
python -m venv venv
UNIX: source venv/bin/activate
WIN: .\venv\scripts\activate
pip install -r requirements.txt
# remove any existing builds
jupyter-book clean .
# build
jupyter-book build .
```

A fully-rendered HTML version of the book will be built in `blocksec/_build/html/`.
