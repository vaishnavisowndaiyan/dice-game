# 🎲 Dice Game

A simple Python command-line dice rolling game built as a beginner-friendly project. The game allows the user to roll two dice repeatedly, tracks how many times the dice were rolled in a session, and exits cleanly on user request.

This project focuses on **clean structure**, **basic input handling**, and **good coding practices** such as using functions and readable naming.

---

## 🚀 Features

* Roll **two six-sided dice**
* Random values generated using Python’s `random` module
* Tracks the **number of rolls per session**
* Input validation for user choices
* Clean exit with a session summary

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** `random` (standard library)

No external dependencies required.

---

## ▶️ How to Run

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/dice-game.git
   ```

3. Navigate to the project folder:

   ```bash
   cd dice-game
   ```

4. Run the game:

   ```bash
   python dice_rolling_game.py
   ```

---

## 🎮 Example Gameplay

```
Roll the dice? (y/n): y
(3, 6)
Roll the dice? (y/n): y
(1, 4)
Roll the dice? (y/n): n

You have rolled the dice 2 times in this session.
Thanks for playing!
```

---

## 🧠 What I Learned

* Using functions to separate logic (`roll_dice`)
* Handling user input safely with `.strip()` and `.lower()`
* Managing program flow with loops and conditionals
* Writing clean, readable Python code
* Writing reusable functions and maintaining program state


---

## 📌 Possible Improvements

* Better formatted output instead of raw tuples
* Option to roll more than two dice
* GUI or web-based version
* Unit tests for dice logic

---

## 📄 License

This project is open-source and available for learning and practice purposes.

---

⭐ If you’re learning Python, feel free to fork this repo and experiment!
