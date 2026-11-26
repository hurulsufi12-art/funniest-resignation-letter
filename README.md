# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/hurulsufi12-art/funniest-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/hurulsufi12-art/funniest-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) on make.fun.

## What it does

`main.py` writes the one-line resignation letter of a retry loop to
`/output/entry.txt`: one line, 132 characters, in the flat, tired voice of a
worker that has retried the same failed request 9,999 times and is now
handing in its resignation as attempt 10,000.

## Run

```sh
python3 -P -s main.py
```

The program is deterministic: every run writes the same bytes. Before
writing anything, it checks the letter against the competition gate
(UTF-8, 1–140 characters, not only whitespace, a single line, no control
characters, no quotation marks around the whole thing). If the gate
refuses the letter, the program exits non-zero and writes nothing.

## Files

- `main.py` — the entry program (Python 3.13, standard library only)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
