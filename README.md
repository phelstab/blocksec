# Blockchain Security Lecture Book Repository

This is a lecture book for the IT-security topic, security of blockchains.

Available @ https://phelstab.github.io/blocksec/

### Installation / Building the book
1. 
```bash
python -m venv venv
```
2. UNIX: Activate
```bash
source venv/bin/activate
```
3. WIN: Activate
```bash
.\venv\scripts\activate
```
4. Install libraries
```bash
pip install -r requirements.txt
```
5. Remove any existing builds
```bash
jupyter-book clean .
```

6. Build (The fully-rendered HTML version of the book will be built in `blocksec/_build/html/`)
```bash 
jupyter-book build .
```










