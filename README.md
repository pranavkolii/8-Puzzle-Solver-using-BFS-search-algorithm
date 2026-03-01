# 8-Puzzle-Solver-using-BFS-search-algorithm
This repository contains the implementation of a Breadth-First Search (BFS) algorithm to solve the classic 8-Puzzle problem.

## 🚀 Project Overview
The project focuses on finding the optimal path from an initial scrambled state to a goal configuration. By utilizing a BFS approach, the solver guarantees the shortest path to the solution while maintaining efficiency through optimized data structures.

## 📂 Repository Structure
```text
├── proj1_pranavjagdish_koli.py               # Main BFS solver and file generator
├── Animate.py                # Pygame visualization script
├── Nodes.txt                 # List of all explored states
├── NodesInfo.txt             # Table of Node Index, Parent Index, and State
├── nodePath.txt              # The specific solution path
└── README.md                 # Project documentation
```

## ⚙️ Installation & Setup
### Prerequisites
* Ubuntu 22.04
* Python 3.10+
* NumPy and Pygame libraries

```bash
# Install dependencies
pip install numpy pygame
```

### Build Instructions
```bash
# Setup the directory structure and clone the repo
mkdir -p ~/Project1
cd ~/Project1
git@github.com:pranavkolii/8-Puzzle-Solver-using-BFS-search-algorithm.git

# Install dependencies
pip install numpy pygame
```

## Outcomes
* Implemented the BFS search algorithm capable of solving complex 8-puzzle configurations within the time constraint.
* Successfully integrated data structures to handle state-space complexity, ensuring unique node exploration and efficient backtracking.
* Generated structured text reports documenting the search tree and the specific solution path for audit and visualization.
