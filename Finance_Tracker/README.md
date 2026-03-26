# 💸 Finance Tracker CLI — Professional Edition

<p align="center">
  <b>A clean, structured, and extensible command-line finance tracker built with Python.</b><br>
  <i>Designed with real-world practices: OOP, persistence, and scalable architecture.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Core Features](#-core-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)
- [License](#-license)

---

## 🚀 Overview

**Finance Tracker CLI** is a minimal yet powerful application that enables users to track income and expenses directly from the terminal.

This project focuses on **clean code principles**, **data persistence**, and **modular design**, making it a strong foundation for scaling into GUI or web-based applications.

---

## ✨ Core Features

- ➕ Add transactions (income / expense)
- 📋 View all transactions with formatted output
- 📊 Generate financial summaries
- 🔍 Filter transactions by category
- 💾 Persistent storage using JSON
- ⚠️ Input validation for safer data handling

---

## 🧠 Architecture

The application is structured using **Object-Oriented Programming (OOP)**:

### `Transaction`
Represents a single financial record:
- amount
- category
- description
- type (income / expense)

### `Tracker`
Handles:
- Data storage & retrieval
- Business logic (summary, filtering)
- File operations (JSON persistence)

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
python try1.py
