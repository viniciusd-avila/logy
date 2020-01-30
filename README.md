# Logy

Logic statement evaluator and naive theorem prover.

| Name | Type| Gate | Token |
| ------------- | :-----:| :-------------:| ---:|
| Variable | Propositional variable | N/A | [A-Z] |
| Negation |Unary operator| NOT | ¬|
| Conjunction |Binary operator| AND | ^ |
| Disjunction |Binary operator| OR | v |
| Exclusive disjunction | Binary operator | XOR | x |
| Material conditional |Binary operator| IMPLY | -> |
| Biconditional | Binary operator | XNOR | <-> |
| Tautology | Boolean | N/A| t |
| Contradiction | Boolean | N/A | f |

The logic statement evaluator only accepts booleans and operators, while the theorem prover accepts variables and expands all its possible values using a truth table. Moving forward we'd like to parse sequents and implement the analytic tableux method.

The adoption of [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) makes the use of parenthesis optional. For example, the statement `(P (P Q ->) ^ Q ->)` can be written as `P P Q -> ^ Q ->` without any issues for the parser.