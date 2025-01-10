# Portfolio Tracker
A simplistic portfolio analyser for tracking the percentage of my option positions. 

## Roadmap
- [ ] Support tracking crypto positions.
- [ ] CLI interface for editing / CRUD.

## Installation
```bash
$ cd path/to/this/project
$ pip install -r requirements.txt
$ ./portfolio
```

If you don't want to prepend `./` to your command every time, add the script to your `$PATH`:
```bash
$ cd path/to/this/project
$ echo export PATH="$(pwd):$PATH" >> ~/.zshrc
$ source ~/.zshrc

$ portfolio
| ASSET TYPE                    | AMOUNT   |
|:------------------------------|:---------|
| UNLEVERAGED                   |          |
| Stock                         | 2800     |
| Revolut                       | 1500     |
| Crypto Spot                   | 3700     |
| TOTAL UNLEVERAGED POSITION    | 8000     |
| CASH IN UNLEVERAGED           | 0        |
| ACCOUNTS                      |          |
| ----------------------------- | -------- |
| LEVERAGED                     |          |
| Lbhk                          | 1750     |
| Lbsg                          | 2800     |
| TOTAL LEVERAGED POSITION      | 4550     |
| CASH IN LEVERAGED             | 3554     |
| ACCOUNTS                      |          |
| ----------------------------- | -------- |
| TOTAL CASH                    | 3554     |
| TOTAL POSITION                | 12550    |
| TOTAL PORTFOLIO               | 16104    |
| PERCENTAGE LEVERAGED ASSETS   | 36.3%    |

$ portfolio -f "/path/to/my_portfolio.yaml"
```

## `portfolio.yaml`

If not provided your portfolio.yaml file with `-f`, `portfolio` will search the default path for the yaml file (`~/.portfolio.yaml` and `./portfolio.yaml`).

`leveraged` and `unleveraged` fields are fixed. The subfields under them are customizable according to your needs.

For every record `key:value` , the value is either an int, or a list of two ints. If it is just one single int, the amount would be fully counted as your position. If you have cash left on that account, please enter `[position_value, cash_value]` instead.