# Direct Blockchain Attack Vectors
*by Paul Helstab & Daniel Stucke*

This book is a collection of notes on blockchain security and corresponding attack vectors. The contents cover the lecture and the exercise on June 9, 2024, in the lecture "Praktische IT-Sicherheit"

## Structure
The book is structured into two parts: The lecture and the exercise. The lecture part contains the theoretical background of the topic, while the exercise part contains practical examples and tasks. If any questions arise during the lecture or the exercise, feel free to ask us. In between the lecture and the exercise there will be a short break (~15 min).

## Prerequisites & Requirements
The lecture will give a broad overview of the blockchain technology and will highlight certain parts more detailed. To take part in the exercise you will need a stable internet connection and an IDE that supports Jupyter Notebooks (e.g. VS Code or PyCharm). There will be some light programming in Python - please download and install the following Python libraries as well:
* blockcypher
* binascii
* mnemonic
* bip-utils
* ecdsa

### Lecture (approx. ~60 minutes)
The lecture covers the following topics:
* Introduction to blockchain technology
* Blockchain fundamentals and principles 
* Security fundamentals of Blockchain technology
* Attack vectors on Blockchains

### Break (15 minutes)

### Exercise (approx. ~90 minutes)
The exercise covers the following topics:
* Performing PoW Blockchain Attacks in a simulated environment
  * 51% Attack
  * Partitioning Attack
  * DoS Attacks to Blockchain Nodes

* Blockchain oriented CTF challenges
  * Unlocking a bitcoin transaction
  * Reverse a wallet adress from mnemonik phrases
  * Getting access to bitcoin wallets (signing messages) via nonce reuse attack