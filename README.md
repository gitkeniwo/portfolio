# Portfolio Tracker
A simplistic portfolio analyser for tracking the percentage of my option positions. 

## Roadmap
- [ ] Support tracking crypto positions.
- [ ] CLI interface for editing / CRUD.

## Installation
```bash
cd path/to/this/project
pip install -r requirements.txt
./portfolio
```

If you don't want to prepend `./` to your command every time, add the script to your `$PATH`:
```bash
cd path/to/this/project
echo export PATH="$(pwd):$PATH" >> ~/.zshrc
source ~/.zshrc
portfolio
portfolio -f "/path/to/my_portfolio.yaml"
```

## `portfolio.yaml`

If not provided your portfolio.yaml file with `-f`, `portfolio` will search the default path for the yaml file (`~/.portfolio.yaml` and `./portfolio.yaml`).

`leveraged` and `unleveraged` fields are fixed. The subfields under them are customizable according to your needs.

For every record `key:value` , the value is either an int, or a list of two ints. If it is just one single int, the amount would be fully counted as your position. If you have cash left on that account, please enter `[position_value, cash_value]` instead.