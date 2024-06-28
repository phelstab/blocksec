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