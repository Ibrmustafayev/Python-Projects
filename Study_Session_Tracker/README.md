<div align="center">

# 📚 Study Session Tracker

![Language](https://img.shields.io/badge/Language-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Concepts](https://img.shields.io/badge/Concepts-OOP%20%7C%20File%20I%2FO%20%7C%20API-informational?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

*A command-line study session tracker with persistent storage and motivational quotes.*

</div>

---

## 📌 Overview

Study Session Tracker lets you log and manage your study sessions by subject. Track how long you studied, add notes, view stats per subject, and get a motivational quote — all from a simple numbered menu. Data is saved to a JSON file and persists between runs.

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | **Add Session** | Log a study session with subject, duration, and a note |
| 2 | **View All Sessions** | Display every session grouped by subject |
| 3 | **Stats per Subject** | Show total time, session count, and average duration per subject |
| 4 | **Overall Summary** | Show total study time and most-studied subject |
| 5 | **Motivational Quote** | Fetch a random quote from the ZenQuotes API |

---

## 🧠 Concepts Used

- OOP — three-class architecture: `Session`, `Subject`, `Tracker`
- `json` — persistent storage via `sessions.json`
- `datetime` — automatic timestamping of each session
- `requests` — live quote fetching from [ZenQuotes API](https://zenquotes.io/)
- Composition — `Tracker` owns `Subject` objects, `Subject` owns `Session` objects

---

## 🖥️ Menu Preview

```
=== Study Session Tracker ===
1. Add a study session
2. View all sessions
3. View stats per subject
4. View overall summary
5. Get a motivational quote on startup
6. Exit
```

---

## 🔧 How to Run

**Requirements:** Python 3.x, `requests` library

```bash
pip install requests
python Study_Session_Tracker.py
```

---

## 📁 Structure

```
StudySessionTracker/
├── Study_Session_Tracker.py   # Main application
├── sessions.json              # Auto-generated data file
└── README.md
```

---

## 📜 License

Released under the [MIT License](../LICENSE).
