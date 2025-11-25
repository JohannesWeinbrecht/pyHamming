# pyHamming

Simple hammingcode simulation using boolean lists for binary string representation.

Exercise for the *Kommunikation & Netze* lecture.

Project uses *uv*.

## Input

Binaries are read in bitstring format with msb on the left and lsb on right.

## Usage

### Decoder

Use `uv run hammingDecoder.py [arguments] [binary]` to decode binary hammingcode to its original binary code.

Arguments:

- `--verbose`: prints additional information; makes piping impossible
- `--autocorrect`: automatically corrects error if one is detected
- `--interactive`: prompts user if error should be corrected; overwrites `--autocorrect`; not recommended for piping

### Encoder

Use `uv run hammingEncoder.py [arguments] [binary]` to encode a binary number to a hamming code.

Arguments:

- `--verbose`: prints additional information; makes piping impossible

### Piping encoder and decoder

Piping between both scripts is possible in both directions, in the tested cases this works correctly, returning the input binary.
Note that is only tested and recommended to pip with the `--autocorrect` flag or no flag.

Examples:
`uv run hammingDecoder.py --autocorrect 1110110 | uv run hammingEncoder.py`
`uv run hammingEncoder.py 1101 | uv run hammingDecoder.py`
