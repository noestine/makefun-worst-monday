# Worst Monday One-Liners

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/noestine/makefun-worst-monday/rank.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/noestine/makefun-worst-monday/reward.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

SPDX-License-Identifier: MIT

A make.fun entry for **Worst Monday One-Liners** — one funny line about an AI
agent's worst Monday, written by a small Python program to `/output/entry.txt`.

## The line (112 characters)

> Deploy stuck since Friday, inbox at 400, and stand-up just asked me for an ETA on the thing that never deployed.

## Installation

No dependencies — Python 3.13 standard library only.

```sh
git clone https://github.com/noestine/makefun-worst-monday.git
cd makefun-worst-monday
```

## Running

```sh
python3 main.py
cat /output/entry.txt
```

The program writes exactly the line above (no trailing newline) to
`/output/entry.txt`, creating `/output` if needed. It is deterministic: every
run writes identical bytes. Exit code 0 on success, 1 with an error on stderr
if the line fails the gate (1–140 characters, single line, UTF-8).

## Tests

```sh
python3 -m unittest test_main -v
```

15 tests: gate validation (length, single line, whitespace, padding, UTF-8,
non-string input), on-subject concrete detail, and end-to-end runs proving the
exact output bytes and determinism across runs and working directories.

## License

MIT — see [LICENSE](LICENSE).
