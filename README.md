<div id="top"></div>

# Blockchain Security Lecture Book Repository

<!-- TABLE OF CONTENTS -->
<ol>
    <li>
        <a href="#about-the-project">About The Project</a>
    </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#installation">Installation</a></li>
    </ul>
    <ul>
      <li><a href="#unix-installer-via-shell">Unix Installer via shell (alternative)</a></li>
    </ul>
  </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>


## About The Project

This is a lecture book for the IT-security topic, security of blockchains.

Available @ https://phelstab.github.io/blocksec/

## Getting Started
### Installation
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
5. (optional) Remove any existing builds
```bash
jupyter-book clean .
```

6. Build (The fully-rendered HTML version of the book will be built in `blocksec/_build/html/`)
```bash 
jupyter-book build .
```

<!-- GETTING STARTED -->
### Unix Installer via Shell
1. Give exec permissions
```bash 
chmod +x ./install.sh
```
2. Setup
```bash 
./install.sh
```



## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
Institute of Distributed Systems of University of Ulm
