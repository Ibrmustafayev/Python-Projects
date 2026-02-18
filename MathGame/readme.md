Add files via upload
🧮 Math Quiz Game (Python)
A console-based math quiz game written in Python.
The game is divided into multiple stages with increasing difficulty, scoring rules, and a final high-risk End Game question.
This project was created for learning purposes and to practice Python fundamentals such as control flow, functions, classes, error handling, and randomness.

🎮 Game Overview
The game consists of 4 stages:
🔹 Part 1
10 questions
Operations: + - * /
Each correct answer: +1 point
One mistake = game over
Up to 3 invalid inputs allowed
🔹 Part 2
7 questions
Increased difficulty
Each correct answer: +2 points
2 mistakes allowed
Up to 2 invalid inputs
🔹 Part 3
5 questions
Higher numbers and difficulty
Each correct answer: +3 points
3 mistakes allowed
Only 1 invalid input allowed
🔹 End Game
1 extremely difficult question
Correct answer: +60 points
Wrong answer: game over
If all previous questions are correct, the player earns +1 bonus point, allowing a maximum score of 100

🧠 Features
Randomly generated math expressions
Dynamic difficulty scaling
Multiple players supported
Healing (mistake) system
Input validation with elimination rules
Scoreboard and winner announcement
Uses Python standard libraries only

⚙️ Technologies Used
Python 3
  Standard libraries:
    random
    operator
    math
    time
No external dependencies required.

📌 Important Notes
Division results are rounded down to one decimal place
Example:
7 / 4 → 1.7 (not 1.75)
Players must enter valid numeric input
Invalid inputs are limited and can eliminate the player

🎯 Purpose of This Project
This project was built to:
Practice Python programming fundamentals
Learn game logic and flow control
Work with randomness and probability
Improve error handling and user interaction
Build confidence before moving to larger projects
