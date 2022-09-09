# PyJack

PyJack is a Python implementation of the classic game of Blackjack.

- **Persistent data:** Balance and other information is stored in seperate files, meaning that you can continue where you left off.
- **Modular design:** Most commands are stored in their own file, making development easier.

## Installation

This assumes you already have [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/) installed.

```
git clone https://github.com/qtchaos/PyJack.git
cd PyJack
python main.py
```

## Commands

- **blackjack** - Starts the game of Blackjack.
- **bal, balance, money** - View your current balance in the game.
- **set_bal** _[int]_ - Allows you to set your balance in the game. **DEV REQUIRED**
- **dev** - Enables developer mode.
- **reset** - Resets all of your data.
- **loadanim** - Previews the load animation.
- **exit** - Exits the game.

## License

This project uses the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/), these are the conditions:

- **Disclose source:** Source code must be made available when the licensed material is distributed.
- **License and copyright notice:** A copy of the license and copyright notice must be included with the licensed material.
- **Same license:** Modifications must be released under the same license when distributing the licensed material. In some cases a similar or related license may be used.
- **State changes:** Changes made to the licensed material must be documented.
