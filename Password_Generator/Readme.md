🔐 Password Generator (Python + Colorama)
A secure and customizable password generator built with Python.
This console-based tool allows users to generate strong passwords by selecting length and character types, with input validation and colored terminal output for better user experience.
This project was created for learning and practice purposes, focusing on clean logic, user interaction, and error handling.

🧠 Project Overview
The Password Generator helps users create passwords based on their preferences:
-Password length
-Uppercase letters
-Digits
-Special characters
The program ensures:
-The password meets the minimum length requirement
-Required character types are included when selected
-Errors are handled gracefully
-Output is clearly displayed using colored text

✨ Features
Custom password length (minimum 4 characters)
Optional inclusion of:
    Uppercase letters
    Digits
    Special characters
Guaranteed inclusion of selected character types
Randomized password generation
Input validation with clear error messages
Colored terminal output using Colorama
Simple and user-friendly interface

⚙️ How It Works
The user enters the desired password length
The program validates the input:
    Must be a number
    Must be at least 4
The user selects which character types to include
The program:
    Ensures selected character types appear at least once
    Fills the remaining length randomly
    Shuffles characters for better randomness
The final password is displayed in green

🧰 Technologies Used
Python 3
  Standard libraries:
    random
    string
  External library:
    colorama (for colored terminal output)

📌 Notes
The program uses the random module, which is suitable for learning purposes
Passwords are generated randomly and shuffled to improve unpredictability
Colored output improves readability but is optional
