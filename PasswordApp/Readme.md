# 🔐 Password Suite

A feature-rich, neon-themed desktop password utility built with Python and Tkinter. Password Suite combines three tools in one sleek cyberpunk-styled GUI: a personal-data-based password generator, a cryptographically-sound random password generator, and an advanced password strength analyzer.

---

## ✨ Features

### 🏠 Main Menu
- Three-card navigation layout with a dark grid background
- Each module has its own distinct neon accent color
- Glowing animated neon borders on each card
- Instant navigation between all pages

---

### 🔵 Page 1 — Personal Data Password Generator
Generate memorable-yet-obscure passwords derived from personal information using three distinct algorithmic methods.

**Input Fields:**
- First name
- Last name
- Date of birth (`DD.MM.YYYY` format)

**Three Generation Algorithms:**

| Version | Method | Description |
|---|---|---|
| VER.1 | Abbreviated + Leet | Strips vowels from a structured pattern of name/date components, then applies leet-speak substitutions |
| VER.2 | Sentence Acronym | Builds an acronym-style phrase from initials + birth year + full month name + day, then applies leet substitutions |
| VER.3 | Sentence Phrase | Combines full name, short year, and month name with `*` delimiters, then applies leet substitutions |

**Leet-Speak Substitution Map used across all three versions:**

| Original | Replaced With |
|---|---|
| `i` | `!` |
| `a` | `@` |
| `S` | `$` |
| `o` | `0` |
| `&` | `8` |

**Input Validation:**
- Name and last name must contain only alphabetical characters
- Date must follow `DD.MM.YYYY` format
- Date must be a real historical date (1900 – today)
- Rejects future dates and invalid calendar dates (e.g., Feb 30)

**Output:**
- All three password variants displayed in a pop-up window
- Each variant has an individual **COPY** button for clipboard access

---

### 🩷 Page 2 — Random Password Generator
Generate cryptographically shuffled random passwords with full character-set control.

**Options:**
- **Length** — Adjustable via spinbox, range: `8` to `64` characters (minimum enforced at 8)
- **Character sets (checkboxes):**
  - `[ A-Z ]` — Uppercase letters (on by default)
  - `[ 0-9 ]` — Digits (on by default)
  - `[ !@# ]` — Special/punctuation characters (off by default)

**Generation Logic:**
1. Always includes at least one lowercase letter
2. Guarantees at least one character from each enabled character set
3. Fills remaining length from the full combined character pool
4. Final password is shuffled with `random.shuffle()` to eliminate positional bias

**Output:**
- Password displayed in a read-only entry field
- **COPY** button for instant clipboard access
- **CLEAR** button resets all settings to defaults

---

### 🟢 Page 3 — Password Strength Checker

A real-time password analysis engine inspired by NIST 2024 guidelines and the zxcvbn methodology. Analysis updates live as you type.

#### Scoring System

Passwords receive a score from **0 to 4**, mapped to these labels and colors:

| Score | Label | Color |
|---|---|---|
| 0 | Very Weak | 🔴 Red |
| 1 | Weak | 🟠 Orange |
| 2 | Fair | 🟡 Yellow |
| 3 | Strong | 🟢 Green |
| 4 | Very Strong | 💚 Dark Green |

#### Entropy Calculation

Entropy is calculated using Shannon's formula:

```
entropy = len(password) × log₂(character_pool_size)
```

Character pool sizes:
- Lowercase letters: **+26**
- Uppercase letters: **+26**
- Digits: **+10**
- Punctuation/Special: **+32**
- Unicode characters (ord > 127): **+1000**

A `penalty_factor` (ranging from `0.05` to `1.0`) is multiplied against raw entropy to produce the **adjusted entropy**, which determines the final score.

#### Score Thresholds (Adjusted Entropy in bits)

| Adjusted Entropy | Score |
|---|---|
| < 28 bits | 0 — Very Weak |
| 28–35 bits | 1 — Weak |
| 36–59 bits | 2 — Fair |
| 60–79 bits | 3 — Strong |
| ≥ 80 bits | 4 — Very Strong |

#### Crack Time Estimation

Crack time is estimated assuming **100 billion guesses/second** (RTX 4090 cluster benchmark):

```
avg_guesses = 2^(entropy_bits - 1)
seconds = avg_guesses / 1e11
```

Output ranges from `"Instantly"` to `"Effectively never"` across seconds, minutes, hours, days, months, years, and centuries.

#### 10 Analysis Checks

The analyzer runs the following checks and applies penalty multipliers:

| # | Check | Penalty |
|---|---|---|
| 1 | **Length** — flags passwords under 6, 8, or 12 characters | 0.2 – 0.8× |
| 2 | **Character variety** — flags single or dual character-type passwords | 0.4 – 0.7× |
| 3 | **Common passwords** — checks against a blocklist of 100 most-used passwords | 0.05× |
| 4 | **L33t speak decoding** — decodes substitutions (`@→a`, `0→o`, etc.) and re-checks against blocklist | 0.15× |
| 5 | **Keyboard walk patterns** — detects sequences like `qwerty`, `asdfgh`, `1q2w3e`, numpad walks | 0.2 – 0.6× |
| 6 | **Sequential characters** — detects alphabetic (`abcde`) and numeric (`12345`) runs | 0.3 – 0.7× |
| 7 | **Character repetition** — flags high ratios of repeated characters (e.g., `aaaa`, `1111`) | 0.2 – 0.7× |
| 8 | **Date/year patterns** — regex detection of years, full dates, and 6–8 digit date strings | 0.7× |
| 9 | **All same case** — flags all-lowercase or all-uppercase passwords under 16 characters | (label only) |
| 10 | **All digits** — flags PIN-style numeric-only passwords | 0.3× |

#### UI Elements
- **Live strength bar** — animated color-coded progress bar (500px wide)
- **Score label** — updates color to match the current strength level
- **Entropy display** — shows adjusted entropy in bits
- **Crack time estimate** — italic label below entropy
- **Analysis column** — up to 6 issues listed with ❌/⚠/✅ indicators
- **Suggestions column** — up to 6 actionable improvement tips
- **SHOW/HIDE** toggle — reveals or masks the password text
- **COPY** button — copies current input to clipboard

---

## 🛠 Tech Stack

| Component | Detail |
|---|---|
| Language | Python 3.x |
| GUI Framework | `tkinter` (stdlib) |
| Entropy Math | `math.log2` |
| Pattern Detection | `re` (regex) |
| Randomness | `random.choice`, `random.shuffle` |
| Date Validation | `datetime` |
| External Dependencies | **None** — 100% standard library |

---

## 🚀 Getting Started

### Prerequisites
- Python **3.7+**
- `tkinter` (included with most Python distributions)

> On some Linux systems, tkinter may need to be installed separately:
> ```bash
> sudo apt-get install python3-tk
> ```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/password-suite.git

# Navigate into the project folder
cd password-suite

# Run the application
python PasswordApp.py
```

No `pip install` required — all dependencies are part of Python's standard library.

---

## 📁 Project Structure

```
password-suite/
│
└── PasswordApp.py       # Single-file application (833 lines)
```

The entire application lives in a single file, organized into clearly commented sections:

```
PasswordApp.py
├── Neon color palette constants
├── Common passwords blocklist (100 entries)
├── Keyboard walk sequences
├── Leet-speak & sequential pattern maps
├── Part 1 — Personal data generator logic
├── Part 2 — Random password generator logic
├── Part 3 — Strength checker engine
├── Part 3 — Strength checker UI update logic
├── Neon border / grid background helpers
├── Root window & frame setup
├── Page 1 UI (Private Data Generator)
├── Page 2 UI (Random Generator)
├── Page 3 UI (Strength Checker)
└── Menu card layout & mainloop
```

---

## 🎨 Design & Theming

The UI uses a cyberpunk/neon aesthetic with a near-black background and three per-module neon accent colors:

| Color | Hex | Used For |
|---|---|---|
| **Cyan** | `#00dcff` | Page 1 — Private Data Generator |
| **Pink** | `#ff00a0` | Page 2 — Random Generator |
| **Green** | `#00ff8c` | Page 3 — Strength Checker |
| **Background** | `#0a0a12` | Main window |
| **Card** | `#0f0f1e` | Page backgrounds |
| **Widget** | `#14142a` | Entry fields, spinboxes |

**Visual effects implemented in pure Tkinter:**
- Multi-layer glowing neon borders (5 concentric rectangles with decreasing alpha)
- Subtle dot grid background canvas on every page
- Color-reactive animated strength bar

---

## 🔒 Security Notes

- **No data is stored or transmitted.** All inputs are processed in memory and discarded when the window is closed.
- The personal data generator is intended to help users create *memorable* passwords — it is not a substitute for a proper password manager.
- The random generator uses Python's `random` module, which is **not** cryptographically secure. For security-critical applications, consider using `secrets` from the standard library instead.
- The strength checker is an educational tool. Scores are heuristic-based and should be treated as guidance rather than a definitive security guarantee.
- The crack time estimate assumes a high-end offline attack scenario (100B guesses/sec). Online attack scenarios are significantly slower.

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas for improvements:

- [ ] Replace `random` with `secrets` for cryptographically secure random generation
- [ ] Add a password history log (session-only)
- [ ] Expand the common passwords blocklist (e.g., HaveIBeenPwned integration)
- [ ] Add a passphrase generator (Diceware-style)
- [ ] Export generated passwords to an encrypted local file
- [ ] Add window resizability / responsive layout
- [ ] Internationalization / multi-language support

To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Built with 💻 and ☕ — feel free to reach out or open an issue with feedback!
