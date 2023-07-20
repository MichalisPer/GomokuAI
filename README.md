# GomokuAI <img src="https://play-lh.googleusercontent.com/epVaPgYRkmgZWgjLzDxLq9ytsprYC3oXJum8zCV-Ydbcqq6rJYOehuRGZ8-vFQyej00k=w512"  width="3%" height="3%">

[![GitHub stars](https://img.shields.io/github/stars/MichalisPer/GomokuAI.svg?style=social)](https://github.com/MichalisPer/GomokuAI/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/MichalisPer/GomokuAI.svg?style=social)](https://github.com/MichalisPer/GomokuAI/network/members)

GomokuAI is a project that showcases a Python-based implementation of an artificial intelligence 
player for the classic Gomoku board game. Gomoku, also known as Five in a Row, is a strategy-based 
game where players aim to connect five stones in a row on a grid-like board.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 📋 Prerequisites
- `Python` (Version `3.11.4`)
- `NumPy` (Version `1.25.1`)

### ⚙️ Installation

1. Clone the repository to your local machine.
```bash
git clone https://github.com/MichalisPer/GomokuAI.git
```
2. Open the project in your preferred IDE and create a virtual environment. How to create virtual environment in PyCharm can be found on the following link: [PyCharm Virtual Environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html). (_optional_)
```bash
# run the following to activate virtual environment
venv\Scripts\activate
```
3. Install all prerequisites by running the requirements file.
```bash
pip install -r requirements.txt
```

## 📖 Usage

To run the above project you firstly have to navigate in the gomoku folder and run the following command.
```bash
# cd gomoku (to navigate in the folder) and then run the command
python gomoku.py MasterPlayer DecentPlayer
```
where the 3 arguments are:
1. the file name
2. `Player 1`, represented with `1` on the grid.
3. `Player 2`, represented with `-1` on the grid.

Currently, there are 3 players in the project:
- Master Player: an implementation of a `min-max` algorithm optimized with `a-b pruning`.
- Decent Player: an implementation of a `min-max` algorithm.
- Random Player: random moves within the grid.

Each of the above player has its own directory, and they all inherit from the `GomokuAgent` class that sits within 
the `gomokuAgent.py` module. Each agent implements the `move(self, board)` method that return a `tuple` with two int that
represent a position in the grid.

## 🤝 Contributing

**Please Note:** This project is currently closed for direct contributions. However, I highly encourage you to fork this 
repository, create your own player and compete with the MasterPlayer to prove yourself. For some of you it might be easy
for other it might be challenging. Try to not have a look on the current implementation, so it will be enjoyable for you.

### How to create your own player

In order to create your own player follow the steps:
1. Create a folder within the gomoku folder and name it as you like (this will be the name of your player, so think wise).
2. Within that folder create a `player.py` file and simply inherit the `GomokuAgent` class from `gomokuAgent.py`. 
3. Implement the `move(self, board)` method to return a tuple with 2 integers that represent a position on the grid.

At last, run the project as shown in the [Usage](#usage) section replacing the DecentPlayer with the name of the folder
you choose at step 1.

### Stay in Touch

I would love to see what you come up with! Feel free to open an issue on this repository and let us know about your fork.
I will be happy to add a link to it in this README. If you have any questions or need assistance with your fork, 
don't hesitate to reach out to me.

