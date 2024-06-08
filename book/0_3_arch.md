# 3. Security Aspects and Technical Fundamentals of Blockchain Technology <!-- (*20 Minuten*) -->

## The Idea
The core idea is to provide a system that is through

<!-- Die Kernidee hinter der Blockchain liegt darin ein System zu schaffen das es ermöglicht komplett Dezentral und somit ohne jegliche Intermediäre und damit auch ohne Treuhänder, Transaktionen zwischen Agenten zu ermöglichen.  -->
The core idea behind blockchain technology is to create a decentralized system that allows transactions between parties (agents) without the need for intermediaries or trusted third parties.
<!-- Dabei übernehmen Mathematische Modelle die auf der Berechenbarkeit und Komplexität Kryptographische verschlüsselungen ermgöglichen, die Aufgaben eines Intermediärs und verteilen diese Aufgaben auf alle Agenten die Teil des Systems sind auch wenn diese eine Aufgabe erhalten die nicht ihrer eigenen Transaktion dient. -->
Mathematical models that enable cryptographic encryption based on computability and complexity take on the tasks of an intermediary. The system itself distribute these tasks to all agents in the system, even if they receive a task that is not related to their own transactions.

It is replaced as follows:
| The Object | Centralized FIAT Object | Blockchain |
|-----------|-----------|-----------|
| The Storage of Value | Bank Account / Physical Wallet | Public + Private Key linked to realised transactions held by the system |
| Transaction | (Digital) Transaction through trustee (middleman) or physical handover between parties | Publishing that an object, has a new owner by its current owner to the whole system through a cryptographic signature |



<!--
1. **Bedingungen** die nicht gebrochen werden dürfen und durch Krypto geschützt werden
   1. 
   2. 
2. **Aufgaben** die verteilt werden müssen und in eine P2P Architektur verteilt werden
   1. Teilnehmer (Full nodes, Halfnodes etc.)
   2. Überwachung der einhaltung von Bedingungen
   3. Validierung der Transaktionen
   
-->

## Conditions


## Tasks



## 3.1 Cryptography



### 3.1.1 Cryptographic Hash Functions




#### SHA-256


#### Merkle-Damgård transform

### 3.1.2 Signing
#### Elliptic Curve Digital Signature Algorithm (ECDSA)
##### Secp256k1


## 3.2 Data Structures in Blockchains
### 3.1.1 Merkle Trees

### 3.1.2 UTXO

## 3.3 Distributed Computing Architectures
### 3.3.1 Peer-2-Peer Networks
<!-- (https://developer.bitcoin.org/reference/p2p_networking.html) -->



## 3.3 The Wallet
<!-- (https://developer.bitcoin.org/reference/wallets.html) -->


## 3.5 The Communication 
<!-- Remote Procedure Calls (RPS)  -->
<!-- (https://developer.bitcoin.org/reference/rpc/index.html) -->




## Security Problems
<!-- (Überleitung) -->


<!-- Sehr sehr wichtig: -->
<!-- https://bitcoin.org/en/bitcoin-core/features/validation -->