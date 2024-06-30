## Exercise 1: Simulating Blockchain Attacks Using the Proof-of-Work Network Simulator



### Getting started

Open the simulator using the following link: [Blockchain Simulator](https://simewu.com/blockchain-simulator/)

For guidance on how to use the simulator, please refer to the [cheat sheet](https://phelstab.github.io/blocksec/book/1_exercise_cheatsheet.html)



### Task 1: 51% Attack

> A 51% attack occurs when a malicious miner or group of miners control more than 50% of the network’s mining hash rate. This allows them to manipulate the blockchain by preventing other miners from completing blocks, reversing transactions, and double-spending coins.

1. **Configure Network**
   - Set up a network with at least five nodes
   - Ensure all nodes have equal hash rates except the attacker node
2. **Set up the Attack**
   - Designate one node as the attacker with a hash rate higher than the combined hash rate of all other nodes (e.g. four honest nodes with a hash rate of 25 hashes/s -> attacker’s hash rate needs to be at least 101 hashes/s)

3. **Execute the Simulation**



#### Questions:

1. Why is it significant for a single entity to control more than 50% of the network’s hash rate? 
2. What did you observe about the block generation process once the attacker node started mining? 
3. How does the attacker’s ability to create the longest chain impact the other nodes blocks? 
4. What are the potential real-world consequences of a successful 51% attack on a popular cryptocurrency?



### Task 2: Partitioning Attack

> A partitioning attack divides the network into separate segments that cannot communicate with each other. This can lead to forks and multiple competing chains, weakening the blockchain’s security.

1. **Configure Network**
   - Set up a network with at least eight nodes arranged in two groups (e.g., 3 & 5)
   - Ensure there are connections between nodes within each group, but no connections between the groups
2. **Set up the Attack**
   - Introduce an attacker node between the two groups, effectively partitioning the network
     - Connect the smaller network with a unidirectional link to the attacker node and fully integrate the attacker node to the bigger network

3. **Execute the Simulation**



#### Questions

1. Why are forks and competing chains problematic for blockchain security? 
2. What were the effects on the blockchain within each partition during the attack? 
3. What vulnerabilities in the blockchain protocol does a partitioning attack exploit?
4. What would happen if the smaller group is now reconnected to the network?



## Task 3: DoS-Attack

> A Denial of Service (DoS) attack involves overwhelming the network or specific nodes with excessive traffic, causing disruptions and preventing normal operations.

1. **Configure Network**
   - Set up a network with at least four nodes and set the bandwidth of each node to 100 MBps
   - Set the buffer size limit of the individual nodes by using the code execution window (*unfortunately, there is a bug when setting it directly in the tree*)
     - Set the buffer size limit to ```1000``` in the “Run before sampling” editor and start the sampling once (you can terminate it right after, check if it worked in the tree)
     - *HINT*: you can use ```NODE_ID.networkBuffer.bufferSizeLimit``` to modify the values
   - Start the miners to establish a baseline
2. **Set up the Attack**
   - Introduce an attacker node with greater mining power (e.g. 100), a bandwidth of 1000 MBps and check the box ```sendInvalidMaliciousBlocks```
   - Use a unidirectional link to connect the attacker to one node (the victim)
3. **Execute the Simulation**
   - After letting the network run for some time, toggle the attacker node and observe the attack
   - *TIP*: Use ```miner.networkBuffer.buffer``` to visualize the buffer of the individual nodes in the Time Plot



#### Questions

1. What impact did the DoS attack have on the victim node’s ability to process and broadcast blocks? 
2. How did the attack affect the overall network performance and block propagation? 
3. Why do nodes continue to mine valid blocks during a DoS attack, yet fail to broadcast them? 
4. Also pay close attention to the balance of the victim. What are you observing?

