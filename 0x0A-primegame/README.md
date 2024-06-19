# Prime Game

## Description

The "Prime Game" is a competitive game where two players, Maria and Ben, take turns picking prime numbers from a set of consecutive integers starting from 1 up to and including `n`. Upon picking a prime number, the player removes that number and all its multiples from the set. The game continues until no moves can be made, and the player who cannot make a move loses. Maria always goes first, and both players play optimally. The objective of this project is to determine the winner of each game based on different values of `n`.

## Features

- Determines the winner between Maria and Ben for each game round.
- Uses the Sieve of Eratosthenes for efficient prime number calculation.
- Employs dynamic programming to optimize game play and result computation.
- Capable of handling multiple game rounds with varying values of `n`.