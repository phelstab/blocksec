## Task 1: 51% Attack
```json
{
	"name": "51_percent_attack",
	"peers": {
		"NODE_1": {
			"name": "Node 1",
			"ID": "NODE_1",
			"power": 25,
			"latency": 10,
			"outgoingPeers": {
				"NODE_4": 10,
				"NODE_3": 10,
				"NODE_2": 10
			},
			"incomingPeers": [
				"NODE_4",
				"ATTACKER"
			],
			"bandwidth": {
				"downlink": 10,
				"uplink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"NODE_2": {
			"name": "Node 2",
			"ID": "NODE_2",
			"power": 25,
			"latency": 10,
			"outgoingPeers": {
				"NODE_3": 10
			},
			"incomingPeers": [
				"NODE_4",
				"NODE_3",
				"NODE_1"
			],
			"bandwidth": {
				"downlink": 10,
				"uplink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"NODE_3": {
			"name": "Node 3",
			"ID": "NODE_3",
			"power": 25,
			"latency": 10,
			"outgoingPeers": {
				"NODE_2": 10
			},
			"incomingPeers": [
				"NODE_2",
				"NODE_1"
			],
			"bandwidth": {
				"downlink": 10,
				"uplink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"NODE_4": {
			"name": "Node 4",
			"ID": "NODE_4",
			"power": 25,
			"latency": 10,
			"outgoingPeers": {
				"NODE_1": 10,
				"NODE_2": 10
			},
			"incomingPeers": [
				"NODE_1"
			],
			"bandwidth": {
				"downlink": 10,
				"uplink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"ATTACKER": {
			"name": "Attacker",
			"ID": "ATTACKER",
			"power": 101,
			"latency": 10,
			"outgoingPeers": {
				"NODE_1": 10
			},
			"incomingPeers": [],
			"bandwidth": {
				"downlink": 10,
				"uplink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ff0000"
		}
	},
	"difficulty": 0.01,
	"blockSize": 1000000,
	"useSHA256": false,
	"ID_Registry": {
		"NODE_1": null,
		"NODE_2": null,
		"NODE_3": null,
		"NODE_4": null,
		"ATTACKER": null
	},
	"miningThreads": {},
	"minimumBlockchainPurgeLength": 100,
	"maximumBlockchainPurgeLength": 200,
	"logging": {
		"columns": {
			"Sample": true,
			"Sample time": true,
			"Sample tag": false,
			"Miner name": true,
			"Balance": true,
			"Balance %": false,
			"Power (hash/s)": true,
			"Power %": false,
			"Blockchain IDs": true,
			"Blockchain num hops": true,
			"Blockchain travel time (ms)": true,
			"Artificial travel time (ms)": false,
			"Network buffer size limit": true,
			"Blocks in flight": true,
			"Latency (ms)": true,
			"Downlink (MBps)": true,
			"Uplink (MBps)": true,
			"Block height": true,
			"Total blocks found": true,
			"Stale blocks found": true,
			"Max fork length": true,
			"Number of network partitions": true,
			"Diameter of the network (number of hops)": false,
			"Diameter of the network (latency)": false,
			"Number of edges (ignoring bidirectional)": false,
			"Number of edges (including bidirectional)": false,
			"Estimated time for a block to reach all nodes": false,
			"Estimated time for a block to reach 50% of nodes": false
		},
		"logNetworkData": false,
		"msPerSample": 20000,
		"codeBeforeSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\nconsole.log('Sampling started at ', Date.now());\n}",
		"codeBetweenSamples": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\n// NODE_1.power += 10;\nif(numSamples >= 100000) toggleSampling(false);\n}",
		"codeAfterSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\nconsole.log('Sampling ended at ', Date.now());\n}",
		"logSamples": false,
		"resetBlockchainAfterEachSample": true,
		"updateTableAfterEachSample": true,
		"logAveragesOnlyCheckbox": true,
		"canvasVisualizerCode": "{miner.lastAcceptedBlock}"
	}
}
```
1.	**Why is it significant for a single entity to control more than 50% of the network’s hash rate?**

_Controlling more than 50% of the network’s hash rate means that a single entity can consistently generate the longest blockchain, effectively allowing them to override the consensus rules. This control enables them to double-spend coins, prevent transactions from being confirmed, and invalidate the blocks mined by other nodes. It undermines the decentralized nature of the blockchain, leading to potential centralization and loss of trust._
2.	**What did you observe about the block generation process once the attacker node started mining?**

_Once the attacker node starts mining, it generates blocks more frequently than the rest of the network combined. This results in the attacker’s blocks being accepted into the blockchain while the blocks mined by the honest nodes are often orphaned or rejected, leading to a disproportionate increase in the attacker’s block reward balance._

3. **How does the attacker’s ability to create the longest chain impact the other nodes’ blocks?**

_The attacker’s ability to create the longest chain causes the blockchain network to recognize their chain as the valid one. Consequently, blocks mined by other nodes are discarded and become stale blocks. This discourages honest miners and can lead to loss of mining rewards and increased forking._ 

4. **What are the potential real-world consequences of a successful 51% attack on a popular cryptocurrency?** 

_Real-world consequences include double-spending attacks where the attacker spends coins on the main chain and then invalidates the transaction by creating a longer chain without it. This erodes trust in the cryptocurrency, leading to potential loss of value, decreased user confidence, and reduced network security. It can also lead to exchanges halting trades, negatively impacting liquidity and adoption._


## Task 2: Partitioning Attack

```json
{
	"name": "partitioning_attack",
	"peers": {
		"N1": {
			"name": "Node 1",
			"ID": "N1",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"A1": 10,
				"N2": 10,
				"N3": 10
			},
			"incomingPeers": [
				"A1",
				"N2",
				"N3"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#FFFF00"
		},
		"N2": {
			"name": "Node 2",
			"ID": "N2",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"N3": 10,
				"N1": 10
			},
			"incomingPeers": [
				"N1",
				"N3"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#7efba0"
		},
		"N3": {
			"name": "Node 3",
			"ID": "N3",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"N1": 10,
				"N5": 10,
				"N4": 10,
				"N2": 10
			},
			"incomingPeers": [
				"N2",
				"N1",
				"N5",
				"N4"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#7BE141"
		},
		"N4": {
			"name": "Node 4",
			"ID": "N4",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"N5": 10,
				"A1": 10,
				"N3": 10
			},
			"incomingPeers": [
				"N3",
				"A1",
				"N5"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#EB7DF4"
		},
		"N5": {
			"name": "Node 5",
			"ID": "N5",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"N3": 10,
				"N4": 10
			},
			"incomingPeers": [
				"N4",
				"N3"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#AD85E4"
		},
		"A1": {
			"name": "Attacker",
			"ID": "A1",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"N1": 10,
				"N4": 10
			},
			"incomingPeers": [
				"N1",
				"N4",
				"NODE_6"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#f51b00"
		},
		"NODE_6": {
			"name": "Node 6",
			"ID": "NODE_6",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_8": 10,
				"A1": 10,
				"NODE_7": 10
			},
			"incomingPeers": [
				"NODE_8",
				"NODE_7"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"NODE_7": {
			"name": "Node 7",
			"ID": "NODE_7",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_8": 10,
				"NODE_6": 10
			},
			"incomingPeers": [
				"NODE_8",
				"NODE_6"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		},
		"NODE_8": {
			"name": "Node 8",
			"ID": "NODE_8",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_6": 10,
				"NODE_7": 10
			},
			"incomingPeers": [
				"NODE_7",
				"NODE_6"
			],
			"bandwidth": {
				"uplink": 10,
				"downlink": 10
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#ffffff"
		}
	},
	"difficulty": 0.01,
	"blockSize": 1000000,
	"useSHA256": false,
	"ID_Registry": {
		"N1": null,
		"N2": null,
		"N3": null,
		"N4": null,
		"N5": null,
		"A1": null,
		"NODE_6": null,
		"NODE_7": null,
		"NODE_8": null
	},
	"miningThreads": {},
	"minimumBlockchainPurgeLength": 100,
	"maximumBlockchainPurgeLength": 200,
	"logging": {
		"columns": {
			"Sample": true,
			"Sample time": true,
			"Sample tag": false,
			"Miner name": true,
			"Balance": true,
			"Balance %": false,
			"Power (hash/s)": true,
			"Power %": false,
			"Blockchain IDs": true,
			"Blockchain num hops": true,
			"Blockchain travel time (ms)": true,
			"Artificial travel time (ms)": false,
			"Network buffer size limit": true,
			"Blocks in flight": true,
			"Latency (ms)": true,
			"Downlink (MBps)": true,
			"Uplink (MBps)": true,
			"Block height": true,
			"Total blocks found": true,
			"Stale blocks found": true,
			"Max fork length": true,
			"Number of network partitions": true,
			"Diameter of the network (number of hops)": false,
			"Diameter of the network (latency)": false,
			"Number of edges (ignoring bidirectional)": false,
			"Number of edges (including bidirectional)": false,
			"Estimated time for a block to reach all nodes": false,
			"Estimated time for a block to reach 50% of nodes": false
		},
		"logNetworkData": false,
		"msPerSample": 20000,
		"codeBeforeSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\nconsole.log('Sampling started at ', Date.now());\n}",
		"codeBetweenSamples": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\n// NODE_1.power += 10;\nif(numSamples >= 100000) toggleSampling(false);\n}",
		"codeAfterSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\nconsole.log('Sampling ended at ', Date.now());\n}",
		"logSamples": false,
		"resetBlockchainAfterEachSample": true,
		"updateTableAfterEachSample": true,
		"logAveragesOnlyCheckbox": true,
		"canvasVisualizerCode": "{miner.lastAcceptedBlock}"
	}
}
```
1. **Why are forks and competing chains problematic for blockchain security?**

_Forks and competing chains create uncertainty about the true state of the blockchain. They can lead to double-spending as transactions may be accepted in one chain and invalidated in another. This weakens the trust in the immutability and finality of transactions, critical aspects of blockchain security. It also wastes computational resources and can lead to network instability._

2. **What were the effects on the blockchain within each partition during the attack?**

_Each partition of the network starts to operate independently, creating its own separate chain of blocks. Transactions and blocks generated within one partition are not recognized by the other, leading to inconsistencies and a lack of consensus across the entire network. This results in multiple versions of the blockchain coexisting, with no single authoritative version._

3. **What vulnerabilities in the blockchain protocol does a partitioning attack exploit?**

_Partitioning attacks exploit the reliance of blockchain on network connectivity and consensus. They take advantage of the lack of coordination and communication between network segments to create isolated groups that can’t validate each other’s transactions and blocks. This fragmentation undermines the decentralized consensus mechanism._

4. **What would happen if the smaller group is now reconnected to the network?**

_Upon reconnection, the smaller group’s blocks are typically rejected if they are not part of the longest chain. The nodes in the smaller partition will switch to the longer chain of the larger partition, causing all the blocks mined in the smaller partition to become stale. This leads to a loss of mining rewards and transaction validations within the smaller partition, causing potential disruptions and inconsistencies._

## Task 3: DoS-Attack

```json
{
	"name": "DoS_attack",
	"peers": {
		"NODE_1": {
			"name": "Node 1",
			"ID": "NODE_1",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_4": 10,
				"NODE_2": 10,
				"NODE_3": 10
			},
			"incomingPeers": [
				"ATTACKER",
				"NODE_4"
			],
			"bandwidth": {
				"uplink": 100,
				"downlink": 100
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#97C2FC"
		},
		"NODE_2": {
			"name": "Node 2",
			"ID": "NODE_2",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_3": 10
			},
			"incomingPeers": [
				"NODE_1",
				"NODE_3"
			],
			"bandwidth": {
				"uplink": 100,
				"downlink": 100
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#FFFF00"
		},
		"NODE_3": {
			"name": "Node 3",
			"ID": "NODE_3",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_4": 10,
				"NODE_2": 10
			},
			"incomingPeers": [
				"NODE_2",
				"NODE_1",
				"NODE_4"
			],
			"bandwidth": {
				"uplink": 100,
				"downlink": 100
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#FB7E81"
		},
		"NODE_4": {
			"name": "Node 4",
			"ID": "NODE_4",
			"power": 10,
			"latency": 10,
			"outgoingPeers": {
				"NODE_1": 10,
				"NODE_3": 10
			},
			"incomingPeers": [
				"NODE_1",
				"NODE_3"
			],
			"bandwidth": {
				"uplink": 100,
				"downlink": 100
			},
			"sendInvalidMaliciousBlocks": false,
			"color": "#7BE141"
		},
		"ATTACKER": {
			"name": "Attacker",
			"ID": "ATTACKER",
			"power": 200,
			"latency": 10,
			"outgoingPeers": {
				"NODE_1": 10
			},
			"incomingPeers": [],
			"bandwidth": {
				"uplink": 1000,
				"downlink": 1000
			},
			"sendInvalidMaliciousBlocks": true,
			"color": "#e00000"
		}
	},
	"difficulty": 0.01,
	"blockSize": 1000000,
	"useSHA256": false,
	"ID_Registry": {
		"NODE_1": null,
		"NODE_2": null,
		"NODE_3": null,
		"NODE_4": null,
		"ATTACKER": null
	},
	"miningThreads": {},
	"minimumBlockchainPurgeLength": 100,
	"maximumBlockchainPurgeLength": 200,
	"logging": {
		"columns": {
			"Sample": true,
			"Sample time": true,
			"Sample tag": false,
			"Miner name": true,
			"Balance": true,
			"Balance %": false,
			"Power (hash/s)": true,
			"Power %": false,
			"Blockchain IDs": true,
			"Blockchain num hops": true,
			"Blockchain travel time (ms)": true,
			"Artificial travel time (ms)": false,
			"Network buffer size limit": false,
			"Blocks in flight": true,
			"Latency (ms)": true,
			"Downlink (MBps)": true,
			"Uplink (MBps)": true,
			"Block height": true,
			"Total blocks found": true,
			"Stale blocks found": true,
			"Max fork length": true,
			"Number of network partitions": true,
			"Diameter of the network (number of hops)": false,
			"Diameter of the network (latency)": false,
			"Number of edges (ignoring bidirectional)": false,
			"Number of edges (including bidirectional)": false,
			"Estimated time for a block to reach all nodes": false,
			"Estimated time for a block to reach 50% of nodes": false
		},
		"logNetworkData": true,
		"msPerSample": 100000,
		"codeBeforeSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\nNODE_1.networkBuffer.bufferSizeLimit = 1000;\nNODE_2.networkBuffer.bufferSizeLimit = 1000;\nNODE_3.networkBuffer.bufferSizeLimit = 1000;\nNODE_4.networkBuffer.bufferSizeLimit = 1000;\n}",
		"codeBetweenSamples": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\n\n}",
		"codeAfterSampling": "{\nlet numSamples = updateToolOptions.numSamples, samplerData = updateToolOptions.samplerData;\nfunction setTag(tag) {\n\tupdateToolOptions.sampleTag = tag.toString();\n}\n\n\n}",
		"logSamples": false,
		"resetBlockchainAfterEachSample": false,
		"updateTableAfterEachSample": true,
		"logAveragesOnlyCheckbox": true,
		"canvasVisualizerCode": "{miner.networkBuffer.buffer}"
	}
}
```

1. **What impact did the DoS attack have on the victim node’s ability to process and broadcast blocks?** 

_The DoS attack overwhelms the victim node with excessive traffic, significantly impairing its ability to process new blocks and broadcast them to the network. The node becomes congested, leading to delays and dropped packets, which prevent it from effectively participating in the network consensus._

2. **How did the attack affect the overall network performance and block propagation?** 

_The attack causes a bottleneck at the victim node, leading to slower block propagation times across the network. Other nodes may not receive blocks from the victim in a timely manner, resulting in increased stale blocks and potential forks. This degradation in network performance reduces overall efficiency and can disrupt the regular functioning of the blockchain._

3. **Why do nodes continue to mine valid blocks during a DoS attack, yet fail to broadcast them?** 

_Nodes continue to mine valid blocks because the mining process itself is unaffected by the network congestion. However, the excessive traffic caused by the DoS attack clogs the network buffer and bandwidth, preventing the nodes from broadcasting their mined blocks to the rest of the network. As a result, these blocks do not get included in the blockchain, and the mining efforts go unrewarded._

4. **Also pay close attention to the balance of the victim. What are you observing?**

_Interestingly, the balance of the victim node varies due to the DoS attack. While the inability to broadcast and validate most of its mined blocks, some blocks are still accepted by the network. However, some rewards may become nullified later on, as the blocks are replaced by oder nodes' blocks due to the delayed or dropped block propagation. This results in an inconsistent balance for the victim node, reflecting the impact of the DoS attack on its mining rewards and transaction processing capabilities._