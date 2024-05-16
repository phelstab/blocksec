# Lecture concept

## 1. Lecture (60 Minuten) - 14:00-15:00

1. Einführung (*10 Minuten*)
   * Überblick über Blockchain-Technologie und ihre Bedeutung
     * Ursprung und Entwicklung
     * Funktionsweise (Genesis Block, Miner, ...)
     * Anwendungsbereiche (Asset Management, Cryptocurrencies, ...)

2. Grundlegende Sicherheitskonzepte (*15 Minuten*)
   * Erklärung Aufbau von (Pow) Blockchains
     * Transactions
       * Hashfunktionen (nur für Zusammenhang)
       * Merkle Trees (Wichtig)
       * UTXO
       * https://developer.bitcoin.org/reference/transactions.html
     * Wallets
       * ECDSA 
       * https://developer.bitcoin.org/reference/wallets.html
     * P2P network
       * https://developer.bitcoin.org/reference/p2p_networking.html
     * RPC's
       * https://developer.bitcoin.org/reference/rpc/index.html
  
   * Vorstellung verschiedener Konsensmechanismen und deren Sicherheitsimplikationen
     * Proof of Work
     * Proof of Stake
     * Proof of Authority

   * Sicherheitsprobleme (Überleitung)

3. Direkte Angriffsvektoren auf Blockchains (*30 Minuten*)

  Der Fokus hier liegt hier bei:
    Relevanz,
    Bekanntheitsgrad
    Aktualität,
    Praktikablität und Umsetzbarkeit,
  weniger praktisch bzw. realistische Attacken sollen nur überflogen werden.

  * Blockchain Attack Taxonomy:
     * Consensus Attacks
       * **51% Attack:** Aufbau, Funktionsweise und Gegenmaßnahmen
       * **Finney Attack:**
       * **Block Withholding:** Aufbau, Funktionsweise und Gegenmaßnahmen
       * **Timejacking:** Aufbau, Funktionsweise und Gegenmaßnahmen
         * **Double Spending**
           * Race Attack:
             * Bei einem Race Attack sendet der Angreifer zwei konkurrierende Transaktionen gleichzeitig ins Netzwerk. Eine Transaktion geht an den Händler, während die andere an die eigene Wallet des Angreifers geht. Wenn die zweite Transaktion zuerst in einen Block aufgenommen wird, wird die erste Transaktion ungültig, und der Händler erhält keine Zahlung.
         * **Fork & Isolate**
       * ...
     * Transaction Attacks
       * **Transaction Replay Attack:**
       * ...
     * P2P Attack
       * **Sylbil:** Aufbau, Funktionsweise und Gegenmaßnahmen
       * **Eclipse:** Aufbau, Funktionsweise und Gegenmaßnahmen
       * ...
     * Encryption
       * **Cryptographic Attack:** 
     * Contract Attacks
       * **Reentrancy:** Aufbau, Funktionsweise und Gegenmaßnahmen
       * ...

1. Fragen und Antworten (5 Minuten)

## 2. Pause (10 Minuten) - 15:00-15:15

## 3. Übung (90 Minuten) - 15:15-17:00
- Idee: Aufbau einer eigenen Blockchain und Proof of Work wie Attacke ablaufen kann 
- Problem: Attacken benötigen mitunter viel Zeit und viele Ressourcen

### 3.1 (optional) Übungsvorberbereitung

- Server als Zentrale Blockchain-Node (z.B. Bitcoin Node)?
- Mining Node?
  - GPU Cluster?

### 3.2 Übungen (~ geschätzt 75 Minuten + 15 Minuten Puffer plus Zusatzübungen)

1. Analysieren von schädlichen/unfairen Transaktionen (Einstiegsübungen für ein tiefes Verständnis ~30 Minuten)
  Ziel ist es hier z. B. ein vorgegebenes Bitcoin Script UTXO historie als JSON Datei (see (#bitcoin-script)) algorithmisch zu analysieren, 
  auf die anfangs beschriebene Angriffsvektoren.

2. 0-Confirmation Double-Spend Attack sog. Transaction Race Attack (~30 Minuten)
  Ziel ist es hier durch eine praktische Übung eine 0 Confirmation Double Spend Attacke Praktisch durchzuführen um die Gefahr bei unkonfirmierten Transaktionen zu zeigen.

3. Lattice Attack (~15 Minuten)
   Private Key aus Noncen widerherstellen

Backlog Übungen falls zu schnell fertig:
Eine weitere Idee wäre es dieses Projekt https://github.com/fenilgmehta/CS765-Simulate-P2P-CryptoCurrency-Network zu forken und weitere Attacken neben der im Repo genannten Selfish Mining Attack durchzuführen

* 51% Attacke weiterentwickeln
* Sybil Attacke weiterentwickeln


## Bitcoin Fundamentals
### Fundamentals

<style>
.slides {
  display: none;
  width: 100%;
}

.animate-left {
  position: relative;
  animation: animateleft 0.8s
}
</style>


Fundamentals: <a href="../_static/L03-05-Bitcoin-Fundamentals_1713872355283_0.pdf">PDF</a>.

<button id="backbtn">Zurück</button>
<button id="fwdbtn">Vor</button>


<div id="slidescontainer">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00002.jpg" style="display: block" alt="Will display in deployed book">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00003.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00004.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00005.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00006.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00007.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00008.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00009.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00010.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00011.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00012.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00013.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00014.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00015.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00016.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00017.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00018.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00019.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00020.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00021.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00022.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00023.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00024.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00025.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00026.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00027.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00028.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00029.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00030.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00031.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00032.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00033.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00034.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00035.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00036.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00037.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00038.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00039.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00040.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00041.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00042.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00043.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00044.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00045.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00046.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00047.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00048.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00049.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00050.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00051.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00052.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00053.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00054.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00055.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00056.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00057.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00058.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00059.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00060.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00061.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00062.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00063.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00064.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00065.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00066.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00067.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00068.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00069.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00070.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00071.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00072.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00073.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00074.jpg">
  <img class="slides animate-left" src="../_static/images/blockchain_fundamentals/00075.jpg">
</div>


<script>
var next_slide = function() {
      slides[count].setAttribute("style", "display:none");
        count = count + 1;
        if(count >= slides.length) {
          count = 0;
        }
        slides[count].setAttribute("style","display:block");
        // Right pressed
}

var prev_slide = function() {
        slides[count].setAttribute("style", "display:none");
        count = count - 1;
        if(count < 0) {
          count = slides.length - 1;
        }
        slides[count].setAttribute("style","display:block");
}

var slides = document.querySelectorAll(".slides");
slides[0].setAttribute("style", "display:block");
//     for (i = 1; i < slides.length; i++) {
//       slides[i].setAttribute("style","display:none");
//     }
var count = 0;

document.addEventListener('keydown', function(event) {
    const key = event.key;
    switch (event.key) {
    case "ArrowLeft":
        prev_slide();
        break;
    case "ArrowRight":
        next_slide();
        break;
}  
});

document.getElementById('slidescontainer').onclick = function (event) {
   next_slide();
}

document.getElementById('fwdbtn').onclick = next_slide;
document.getElementById('backbtn').onclick = prev_slide;

</script>


### Bitcoin Script

Source: https://gist.github.com/bitjson/3dbe0d06961439966d774103430a636f

```json
{
	"description": "Definition file for Bitcoin Script Templates",
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "http://p2sh.cash/bst.schema.json",
	"title": "Bitcoin Script Template (BST) JSON Schema",
	"type": "object",
	"properties": {
		"v":{
			"description": "BST schema version",
			"type": "integer",
			"exclusiveMinimum": 0
		},
		"n":{
			"description": "Name for this BST template",
			"type": "string"
		},
		"d":{
			"description": "Description for this BST template",
			"type": "string"
		},
		"w":{
			"description": "[NOT-YET-IMPLEMENTED]List of warnings and notes to the user",
			"type": "array",
			"items": { "type": "string" }
		},
		"x":{
			"description": "User defined variables (not wallet friendly) which shall be selected or input by the user in the Template Options User Interface and may be referenced within the Locking and Unlocking Script Sections 'u' and 'l' for direct value replacement or controlling a 'repeat-*' type object.",
			"type": "array",
			"uniqueItems": true,
			"items": {
				"anyOf": [
					{
						"description": "opcode: A user defined opcode variable that will be selected via dropdown menu.",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a variable", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of variable", "type": "string", "oneOf": [ { "enum": [ "opcode" ] } ] },
							"d": { "description": "Description of the opcode variable", "type": "string" },
							"c": {
								"description": "Constraints on an opcode type user specified variable",
								"oneOf": [
									{ "description": "[DEPRECIATED]Min/max range of valid opcodes", "type": "array", "items": { "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2},
									{ "description": "[NOT-YET-IMPLEMENTED]Range of valid opcode (integer) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "[NOT-YET-IMPLEMENTED]Range of valid opcode (string) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "[NOT-YET-IMPLEMENTED]List of valid opcode (integer) values", "type": "object", "properties": { "l": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "[NOT-YET-IMPLEMENTED]List of valid opcode (string) values", "type": "object", "properties": { "l": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } }
								]
							}
						},
						"required": [ "n", "t" ]
					},
					{
						"description": "pushdata[NOT-YET-IMPLEMENTED]: User defined pushdata variable that will be provided by the user via text input box.",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a variable", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of variable", "type": "string", "oneOf": [ { "enum": [ "pushdata[NOT-YET-IMPLEMENTED]" ] } ] },
							"d": { "description": "Description of the pushdata variable", "type": "string" },
							"l": { "description": "Minimum and maximum byte length requirement [inclusive, exclusive]", "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2}
						},
						"required": [ "n", "t", "l" ]
					},
					{
						"description": "time-*[NOT-YET-IMPLEMENTED]: A user defined time as a UNIX timestamp in seconds (absolute) or blocks (relative), encoded in little-endian format",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a variable", "type": "string",  "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of variable", "type": "string", "oneOf": [ { "enum": [ "time-absolute[NOT-YET-IMPLEMENTED]", "time-relative[NOT-YET-IMPLEMENTED]" ] } ] },
							"d": { "description": "Description of the time variable", "type": "string" }
						}
					},
					{
						"description": "numeric[NOT-YET-IMPLEMENTED]: A user defined signed numeric type value encoded in little-endian format",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a variable", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of variable", "type": "string", "oneOf": [ { "enum": [ "numeric[NOT-YET-IMPLEMENTED]" ] } ] },
							"d": { "description": "Description of the numeric variable", "type": "string" }
						}
					}
				]
			}
		},
		"u": {
			"description": "Unlocking Script Templates (Note: There can be multiple unlocking script templates)",
			"type":"array",
			"uniqueItems": true,
			"minItems": 0,
			"items": {
				"description": "The unlocking script template",
				"type": "object",
				"properties": {
					"n": {
						"description": "Name of the unlocking script",
						"type": "string"
					},
					"s": {
						"description": "Script template for unlocking part of script",
						"type":"array",
						"items": {
							"anyOf": [
								{
									"description": "Integer is interpreted as an opcode value",
									"type": "integer",
									"oneOf": [ "valid_opcode_integers" ]
								},
								{
									"description": "String starting with 'OP_' is replaced by interpreter with a opcode integer value",
									"type": "string",
									"oneOf": [ "valid_opcode_strings" ]
								},
								{
									"description": "A string which shall match one of the user defined variables to be replaced by either the opcode or pushdata value selected by user in the template user options.",
									"type": "string",
									"pattern": "^(?!OP_)([A-Z0-9]+)$"
								},
								{
									"description": "opcode[NOT-YET-IMPLEMENTED]: A single user selectable opcode input that will be selected via dropdown menu.",
									"type": "object",
									"properties": {
										"n": { "description": "Name of a input", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
										"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "opcode[NOT-YET-IMPLEMENTED]" ] } ] },
										"d": { "description": "Description of the opcode input", "type": "string" },
										"c": {
											"description": "Constraints on an opcode type user specified input",
											"oneOf": [
												{ "description": "Range of valid opcode (integer) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array",  "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "Range of valid opcode (string) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "List of valid opcode (integer) values", "type": "object", "properties": { "l": { "type": "array",  "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "List of valid opcode (string) values", "type": "object", "properties": { "l": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } }
											]
										}
									},
									"required": [ "n", "t" ]
								},
								{
									"description": "repeat-opcode[NOT-YET-IMPLEMENTED]: Repeating user selectable opcode input that will be selected via dropdown menu.",
									"type": "object",
									"properties": {
										"n": { "description": "Name of a input", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
										"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "repeat-opcode[NOT-YET-IMPLEMENTED]" ] } ] },
										"d": { "description": "Description of the opcode input", "type": "string" },
										"x": { "description": "User defined variable that is controlling the input repetitions.", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$"},
										"c": {
											"description": "Constraints on an opcode type user specified input",
											"oneOf": [
												{ "description": "Range of valid opcode (integer) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "Range of valid opcode (string) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "List of valid opcode (integer) values", "type": "object", "properties": { "l": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "description": "List of valid opcode (string) values", "type": "object", "properties": { "l": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } }
											]
										}
									},
									"required": [ "n", "t", "x" ]
								},
								{
									"description": "pushdata: A single user input field for arbitrary data to be pushed onto the stack (NOTE: 'i' section options provide to unlocking script to signal wallet friendliness)",
									"type": "object",
									"properties": {
										"t": { "description": "Type of user input ('pushdata')", "type": "string", "oneOf": [ { "enum": [ "pushdata" ] } ] },
										"i": { "description": "Intent and purpose for user input", "type": "string", "oneOf": [ { "enum": [ "sig-ec", "data-sig-ec", "utf8", "hash160", "sha256" ] } ] },
										"n": { "description": "Display name of item to be created", "type": "string" },
										"d": { "description": "Description of the user input field", "type": "string" },
										"l": { "description": "Minimum and maximum byte length requirement [inclusive, exclusive]", "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2}
									},
									"required": [ "t", "n", "l" ]
								},
								{
									"description": "repeat-pushdata: Repeated user input field for arbitrary data to be pushed onto the stack",
									"type": "object",
									"properties": {
										"t": { "description": "Type of user input ('repeat-pushdata')", "type": "string", "oneOf": [ { "enum": [ "repeat-pushdata" ] } ] },
										"i": { "description": "Intent and purpose for user input", "type": "string", "oneOf": [ { "enum": [ "sig-ec", "data-sig-ec", "utf8", "hash160", "sha256" ] } ] },
										"n": { "description": "Display name of repeated item to be created (application should add '-#' after the name to provide user with a different name)", "type": "string" },
										"d": { "description": "Description of the user input field", "type": "string" },
										"x": { "description": "User defined variable that is controlling the input repetitions.", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$"},
										"l": { "description": "Minimum and maximum byte length requirement [inclusive, exclusive]", "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2}
									},
									"required": [ "t", "n", "x", "l" ]
								},
								{
									"description": "multiplex-opcode[NOT-YET-IMPLEMENTED]: Represents a range or list of opcode values that should be considered",
									"type": "object",
									"properties": {
										"t": { "description": "Type of object ('multiplex-opcode')", "type": "string", "oneOf": [ { "enum": [ "multiplex-opcode[NOT-YET-IMPLEMENTED]" ] } ] },
										"n": { "description": "Display name of repeated item to be created (application should add '-#' after the name to provide user with a different name)", "type": "string" },
										"d": { "description": "Description of the user input field", "type": "string" },
										"i": {
											"description": "Items to be used in multiplex-opcode.",
											"oneOf": [
												{ "type": "object", "properties": {
													"r": { "description": "Range of opcode (integer) values to consider [inclusive, exclusive]", "type": "array", "items": { "type":"integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "type": "object", "properties": {
													"r": { "description": "Range of opcode (string) values to consider [inclusive, exclusive]", "type": "array", "items": { "type":"string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
												{ "type": "object", "properties": {
													"l": { "description": "List of opcode (integer) values to consider", "type": "array", "items": { "type": "integer", "oneOf": [ "valid_opcode_integers" ] } } } },
												{ "type": "object", "properties": {
													"l": { "description": "List of opcode (string) values to consider", "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] } } } }
											]
										}
									},
									"required": [ "t", "n" ]
								}
							]
						}
					}
				},
				"required": [ "n", "s" ]
			}
		},
		"l":{
			"description": "Locking script template",
			"type":"array",
			"minItems": 0,
			"items": {
				"anyOf": [
					{
						"description": "Integer hard-coded into a template is interpreted as an opcode value",
						"type": "integer",
						"oneOf": [ "valid_opcode_integers" ]
					},
					{
						"description": "String hard-coded into a template starting with 'OP_' is replaced by interpreter with a opcode integer value",
						"type": "string",
						"oneOf": [ "valid_opcode_strings" ]
					},
					{
						"description": "String hard-coded into a template should be a named user defined variable from the 'x' section above to be replaced after user makes selection in options menu.",
						"type": "string",
						"pattern": "^(?!OP_)([A-Z0-9]+)$"
					},
					{
						"description": "script: A single instance of a pre-defined script hard-coded into the template as a string in hexadecimal format. Named user defined variables can be embedded using <XX> notation.",
						"type": "object",
						"properties": {
							"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "script" ] } ]},
							"d": { "description": "Description of the script", "type": "string" },
							"s": { "description": "The pre-defined script which may include user defined variables using <XX> syntax", "type": "string", "pattern": "^[0-9a-fA-F]+$" }
						},
						"required": [ "t", "s" ]
					},
					{
						"description": "repeat-script: Repeating pre-defined script stored in the template as a string in hexadecimal format. Named user defined variables can be embedded using <XX> notation.",
						"type": "object",
						"properties": {
							"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "repeat-script" ] } ] },
							"d": { "description": "Description of the script", "type": "string" },
							"x": { "description": "User defined variable controlling the number of repetitions for this script.", "type": "string" },
							"s": { "description": "The pre-defined script which may include user defined variables using <XX> syntax", "type": "string", "pattern": "^[0-9a-fA-F]+$" }
						},
						"required": [ "t", "s", "x" ]
					},
					{
						"description": "opcode[NOT-YET-IMPLEMENTED]: A single user selectable opcode input that will be selected via dropdown menu.",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a input", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "opcode[NOT-YET-IMPLEMENTED]" ] } ] },
							"d": { "description": "Description of the opcode variable", "type": "string" },
							"c": {
								"description": "Constraints on an opcode type user specified variable",
								"oneOf": [
									{ "description": "Range of valid opcode (integer) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "Range of valid opcode (string) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "List of valid opcode (integer) values", "type": "object", "properties": { "l": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "List of valid opcode (string) values", "type": "object", "properties": { "l": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } }
								]
							}
						},
						"required": [ "n", "t" ]
					},
					{
						"description": "repeat-opcode[NOT-YET-IMPLEMENTED]: Repeating user selectable opcode input that will be selected via dropdown menu.",
						"type": "object",
						"properties": {
							"n": { "description": "Name of a input", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$" },
							"t": { "description": "Type of input", "type": "string", "oneOf": [ { "enum": [ "repeat-opcode[NOT-YET-IMPLEMENTED]" ] } ] },
							"d": { "description": "Description of the opcode input", "type": "string" },
							"x": { "description": "User defined variable controlling the input repetitions.", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$"},
							"c": {
								"description": "Constraints on an opcode type user specified variable",
								"oneOf": [
									{ "description": "Range of valid opcode (integer) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "Range of valid opcode (string) values [inclusive, inclusive]", "type": "object", "properties": { "r": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "List of valid opcode (integer) values", "type": "object", "properties": { "l": { "type": "array", "items":{ "type": "integer", "oneOf": [ "valid_opcode_integers" ] }, "minItems": 2, "maxItems": 2 } } },
									{ "description": "List of valid opcode (string) values", "type": "object", "properties": { "l": { "type": "array", "items": { "type": "string", "oneOf": [ "valid_opcode_strings" ] }, "minItems": 2, "maxItems": 2 } } }
								]
							}
						},
						"required": [ "n", "t", "x" ]
					},
					{
						"description": "pushdata: A single user input field for arbitrary data to be pushed onto the stack. Special enum 'pubkey-ec' can be used to help a wallet determine which key to use for signing.",
						"type": "object",
						"properties": {
							"t": { "description": "Type of user input ('pushdata')", "type": "string", "oneOf": [ { "enum": [ "pushdata" ] } ] },
							"i": { "description": "Intent and purpose for user input", "type": "string", "oneOf": [ { "enum": [ "pubkey-ec", "hash160", "sha256", "utf8" ] } ] },
							"n": { "description": "Display name of item to be created", "type": "string" },
							"d": { "description": "Description of the user input field", "type": "string"},
							"l": { "description": "Minimum and maximum byte length requirement [inclusive, exclusive]", "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2}
						},
						"required": [ "t", "n" ]
					},
					{
						"description": "repeat-pushdata: Repeated user input field for arbitrary data to be pushed onto the stack",
						"type": "object",
						"properties": {
							"t": { "description": "Type of user input ('repeat-pushdata')", "type": "string", "oneOf": [ { "enum": [ "repeat-pushdata" ] } ] },
							"i": { "description": "Intent and purpose for user input", "type": "string", "oneOf": [ { "enum": [ "pubkey-ec", "hash160", "sha256", "utf8" ] } ] },
							"n": { "description": "Display name of repeated item to be created (application should add '-#' after the name to provide user with a different name)", "type": "string" },
							"d": { "description": "Description of the user input field", "type": "string" },
							"x": { "description": "User defined variable controlling the input repetitions.", "type": "string", "pattern": "^(?!OP_)([A-Z0-9]+)$"},
							"l": { "description": "Minimum and maximum byte length requirement [inclusive, exclusive]", "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2}
						},
						"required": [ "t", "n", "x" ]
					}
				]
			}
		}
	},
	"required": [ "v", "n", "l"	]
}
```