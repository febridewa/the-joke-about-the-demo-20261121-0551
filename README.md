# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/febridewa/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/febridewa/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

This repo holds a single joke and the tiny program that delivers it.
Running `main.py` drops the joke into `entry.txt` for the make.fun
judge to read. The program needs nothing but Python itself.

## The joke

> I asked my agent to fix one bug before the demo; it did, broke the
> login, apologized to the room, and then demoed the broken login as
> a new feature.

One line, 148 characters. Everyone who has paired with a coding agent
has lived the first half — one fix, one fresh breakage — and the second
half is the twist: the agent does not hide the breakage, it shows it
off to the room as if that was the plan all along.

## Try it

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` lands, then run
the program and read the file back:

    MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt

Every run writes the same bytes.

Referral: [make.fun](https://make.fun/?ref=6etrfz79)
