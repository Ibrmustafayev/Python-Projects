import tkinter as tk
import string
import math
import re
from random import choice, shuffle
from datetime import datetime
from tkinter import messagebox

# ─── Neon Palette ────────────────────────────────────────────────────────────
BG_DARK   = "#0a0a12"   # near-black main background
BG_CARD   = "#0f0f1e"   # card / page background
BG_WIDGET = "#14142a"   # entry fields, spinbox
FG_MAIN   = "#dce8ff"   # primary text
FG_DIM    = "#5577aa"   # dimmed labels
FG_DIMMER = "#334466"   # crack time italic
BAR_EMPTY = "#0a0a18"   # empty bar track

# Per-page neon accents
CYAN      = "#00dcff"   # Page 1
PINK      = "#ff00a0"   # Page 2
GREEN     = "#00ff8c"   # Page 3

# Active/pressed shades
CYAN_ACT  = "#008faa"
PINK_ACT  = "#aa0066"
GREEN_ACT = "#00aa5e"

# Bar width constant (moved to top with other constants)
BAR_TOTAL_WIDTH = 500

# ─── Common passwords blocklist (top 100 most common) ────────────────────────
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "12345678", "12345", "1234567",
    "password1", "qwerty", "abc123", "111111", "1234567890", "123123",
    "000000", "1234", "iloveyou", "admin", "letmein", "welcome",
    "monkey", "dragon", "master", "sunshine", "princess", "shadow",
    "superman", "michael", "football", "baseball", "soccer", "batman",
    "starwars", "trustno1", "passw0rd", "p@ssword", "p@ssw0rd",
    "hello", "freedom", "whatever", "qazwsx", "zxcvbn", "qwertyuiop",
    "asdfghjkl", "zxcvbnm", "1q2w3e", "1q2w3e4r", "qwerty123",
    "qwerty1", "password123", "password12", "password2", "987654321",
    "654321", "55555", "666666", "777777", "888888", "696969",
    "123321", "159753", "pass", "login", "ninja", "killer", "access",
    "mustang", "maverick", "charlie", "donald", "hunter", "ranger",
    "harley", "jordan", "jennifer", "thomas", "jessica", "nicole",
    "daniel", "andrew", "joshua", "george", "michelle", "summer",
    "ashley", "hannah", "amanda", "abcdef", "abc",
    "root", "toor", "test", "guest", "user", "default", "changeme",
    "qwert", "asdf", "zxcv", "1111", "2222", "3333", "4444",
    "5555", "6666", "7777", "8888", "9999", "0000", "9876",
}

# Keyboard walk sequences (horizontal, diagonal, numpad)
KEYBOARD_WALKS = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "poiuytrewq", "lkjhgfdsa", "mnbvcxz",
    "qazwsxedcrfvtgbyhnujmikolp", "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol",
    "1234567890", "0987654321", "qweasdzxc", "qazxswedc",
    "147258369", "963852741", "123654789",
    "!@#$%^&*()", "qwerty", "asdfgh", "zxcvbn",
]

LEET_MAP = {
    "@": "a", "!": "i", "$": "s", "0": "o",
    "1": "i", "3": "e", "4": "a", "5": "s",
    "7": "t", "8": "b", "+": "t", "|": "i",
}

SEQUENTIAL_CHARS = [
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
    "0123456789", "9876543210",
]


# ─── Part 1 - Mechanisms ─────────────────────────────────────────────────────
def clear():
    name_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def months(month):
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return month_names.get(month, "Unknown")

def february(year):
    if year % 400 == 0:
        return 29
    elif year % 100 != 0 and year % 4 == 0:
        return 29
    else:
        return 28

def check_date(day, month, year):
    if not (1 <= month <= 12):
        return False
    if not (1900 <= year <= datetime.now().year):
        return False
    try:
        date_to_check = datetime(year, month, day)
    except ValueError:
        return False
    if date_to_check >= datetime.now():
        return False
    return True

def misspelling(original_password):
    exchange = {
        "i": "!", "a": "@", "S": "$",
        "o": "0", "&": "8"
    }
    password = ""
    for letter in original_password:
        if letter in exchange:
            password += exchange[letter]
        else:
            password += letter
    return password

def myversion1(name, lastname, day, month, year):
    originalpassword = "_" + str(year)[2:] + name + day + month + lastname
    password = ""
    for letter in originalpassword:
        if letter in "euiao":
            continue
        password += letter
    return misspelling(password)

def SentenceToAcronym(name, lastname, day, month, year):
    password1 = name[0] + lastname[0] + "b" + str(year) + "in" + months(int(month)) + day
    return misspelling(password1)

def SentenceToPhrase(name, lastname, month, year):
    password2 = name + lastname + "*" + str(year)[2:] + "*" + months(int(month))
    return misspelling(password2)

def copy_to_clipboard(pwd):
    root.clipboard_clear()
    root.clipboard_append(pwd)

def show_passwords(p1, p2, p3):
    win = tk.Toplevel(root)
    win.title("Generated Passwords")
    win.geometry("540x300")
    win.configure(bg=BG_CARD)
    win.resizable(False, False)

    tk.Label(win, text="//  GENERATED PASSWORDS", font=("Courier", 13, "bold"),
             bg=BG_CARD, fg=CYAN).pack(pady=15)

    for label, pwd in [("VER.1", p1), ("VER.2", p2), ("VER.3", p3)]:
        row = tk.Frame(win, bg=BG_CARD)
        row.pack(pady=6)

        tk.Label(row, text=f"{label}:", font=("Courier", 11), bg=BG_CARD,
                 fg=FG_DIM, width=7, anchor="w").pack(side="left")

        entry = tk.Entry(row, font=("Courier", 11), width=28, bg=BG_WIDGET, fg=CYAN,
                         readonlybackground=BG_WIDGET, relief="flat",
                         highlightthickness=1, highlightbackground=CYAN,
                         insertbackground=CYAN)
        entry.insert(0, pwd)
        entry.config(state="readonly")
        entry.pack(side="left", padx=5, ipady=3)

        tk.Button(row, text="COPY", font=("Courier", 9, "bold"), width=6,
                  command=lambda p=pwd: copy_to_clipboard(p),
                  bg=BG_WIDGET, fg=CYAN, activebackground=BG_DARK,
                  relief="flat", highlightthickness=1, highlightbackground=CYAN).pack(side="left", padx=3)

    tk.Button(win, text="[ CLOSE ]", font=("Courier", 11, "bold"), width=12, command=win.destroy,
              bg=BG_WIDGET, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN,
              relief="flat", highlightthickness=1, highlightbackground=FG_DIM).pack(pady=18)

def get_information():
    try:
        name = name_entry.get().strip()
        lastname = lname_entry.get().strip()
        date_text = date_entry.get().strip()

        if not name or not lastname or not date_text:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        name = name.capitalize()
        lastname = lastname.capitalize()

        parts = date_text.split(".")
        if len(parts) != 3:
            messagebox.showerror("Error", "Enter date in DD.MM.YYYY format.")
            return

        day, month, year = parts

        if not name.isalpha() or not lastname.isalpha():
            messagebox.showerror("Error", "Name and last name must contain only letters.")
            return

        if not check_date(int(day), int(month), int(year)):
            messagebox.showerror("Error", "Enter a valid date of birth.")
            return

        show_passwords(
            myversion1(name, lastname, day, month, year),
            SentenceToAcronym(name, lastname, day, month, year),
            SentenceToPhrase(name, lastname, month, year)
        )

    except ValueError:
        messagebox.showerror("Error", "Date must contain only numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def show_frame(frame):
    frame.tkraise()


# ─── Part 2 - Mechanisms ─────────────────────────────────────────────────────
def clear_random():
    length_spinbox.delete(0, tk.END)
    length_spinbox.insert(0, "8")
    uppercase_var.set(True)
    digit_var.set(True)
    special_var.set(False)
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.config(state="readonly")

def generate_random_password():
    try:
        length = int(length_spinbox.get().strip())
        if length < 8:
            messagebox.showerror("Error", "The length of the password must be at least 8 characters!")
            return
    except ValueError:
        messagebox.showerror("Error", "The input must be a digit!")
        return

    include_uppercase = uppercase_var.get()
    include_digit     = digit_var.get()
    include_special   = special_var.get()

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    digits    = string.digits           if include_digit     else ""
    special   = string.punctuation      if include_special   else ""

    all_characters = lowercase + uppercase + digits + special

    password = []
    password.append(choice(lowercase))
    if include_uppercase:
        password.append(choice(uppercase))
    if include_digit:
        password.append(choice(digits))
    if include_special:
        password.append(choice(special))

    for _ in range(length - len(password)):
        password.append(choice(all_characters))

    shuffle(password)
    result = "".join(password)

    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)
    result_entry.config(state="readonly")


# ─── Part 3 - Password Strength Checker Engine ───────────────────────────────

def decode_leet(password):
    """Convert l33t speak back to normal letters."""
    decoded = ""
    for ch in password.lower():
        decoded += LEET_MAP.get(ch, ch)
    return decoded

def check_keyboard_walk(password):
    """Return the longest keyboard walk length found."""
    pwd_lower = password.lower()
    for walk in KEYBOARD_WALKS:
        for length in range(min(len(pwd_lower), len(walk)), 3, -1):
            for i in range(len(walk) - length + 1):
                if walk[i:i+length] in pwd_lower:
                    return length
    return 0

def check_sequential(password):
    """Return length of longest sequential pattern."""
    pwd_lower = password.lower()
    for seq in SEQUENTIAL_CHARS:
        for length in range(min(len(pwd_lower), len(seq)), 3, -1):
            for i in range(len(seq) - length + 1):
                if seq[i:i+length] in pwd_lower:
                    return length
    return 0

def check_repeats(password):
    """Return ratio of repeated characters (0-1)."""
    if not password:
        return 0
    char_count = {}
    for ch in password.lower():
        char_count[ch] = char_count.get(ch, 0) + 1
    max_repeat = max(char_count.values())
    return max_repeat / len(password)

def check_date_pattern(password):
    """Detect date patterns in password."""
    patterns = [
        r'\b(19|20)\d{2}\b',
        r'\b\d{1,2}[.\-/]\d{1,2}[.\-/]\d{2,4}\b',
        r'\b\d{8}\b',
        r'\b\d{6}\b',
    ]
    for pat in patterns:
        if re.search(pat, password):
            return True
    return False

def calculate_entropy(password):
    """Calculate raw Shannon entropy based on character pool."""
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += 32
    if any(ord(c) > 127 for c in password): pool += 1000
    if pool == 0:
        return 0
    return len(password) * math.log2(pool)

def estimate_crack_time(entropy_bits):
    """Estimate crack time assuming 100 billion guesses/second (RTX 4090 cluster)."""
    guesses_per_second = 1e11
    avg_guesses = 2 ** (entropy_bits - 1)
    seconds = avg_guesses / guesses_per_second

    if seconds < 1:
        return "Instantly"
    elif seconds < 60:
        return f"{int(seconds)} second(s)"
    elif seconds < 3600:
        return f"{int(seconds/60)} minute(s)"
    elif seconds < 86400:
        return f"{int(seconds/3600)} hour(s)"
    elif seconds < 2592000:
        return f"{int(seconds/86400)} day(s)"
    elif seconds < 31536000:
        return f"{int(seconds/2592000)} month(s)"
    elif seconds < 3153600000:
        return f"{int(seconds/31536000)} year(s)"
    elif seconds < 3.154e12:
        return f"{int(seconds/3153600000)} century/centuries"
    else:
        return "Effectively never"

def analyze_password(password):
    """
    Full analysis engine based on NIST 2024 + zxcvbn methodology.
    Returns: (score 0-4, entropy_bits, issues[], suggestions[], crack_time)
    """
    if not password:
        return 0, 0, [], [], "N/A"

    issues = []
    suggestions = []
    penalty_factor = 1.0

    # ── 1. Length check ──────────────────────────────────────────────────────
    L = len(password)
    if L < 6:
        issues.append("❌ Too short (under 6 characters)")
        suggestions.append("Use at least 12 characters")
        penalty_factor *= 0.2
    elif L < 8:
        issues.append("⚠ Short password (6–7 characters)")
        suggestions.append("Aim for at least 12 characters")
        penalty_factor *= 0.5
    elif L < 12:
        issues.append("⚠ Could be longer (8–11 characters)")
        suggestions.append("12+ characters is recommended by NIST")
        penalty_factor *= 0.8
    elif L < 15:
        pass
    else:
        pass

    # ── 2. Character variety ──────────────────────────────────────────────────
    has_lower   = any(c.islower() for c in password)
    has_upper   = any(c.isupper() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = sum([has_lower, has_upper, has_digit, has_special])
    if variety == 1:
        issues.append("❌ Only one character type used")
        suggestions.append("Mix uppercase, lowercase, digits, and symbols")
        penalty_factor *= 0.4
    elif variety == 2:
        issues.append("⚠ Only two character types used")
        suggestions.append("Add symbols or digits to increase variety")
        penalty_factor *= 0.7
    elif variety == 3:
        pass

    # ── 3. Common password check ──────────────────────────────────────────────
    if password.lower() in COMMON_PASSWORDS:
        issues.append("❌ This is one of the most common passwords!")
        suggestions.append("Avoid passwords that appear in known breach lists")
        penalty_factor *= 0.05

    # ── 4. L33t speak → re-check against common passwords ────────────────────
    decoded = decode_leet(password)
    if decoded != password.lower() and decoded in COMMON_PASSWORDS:
        issues.append("❌ Password is a l33t-speak variation of a common word")
        suggestions.append("L33t substitutions (@ for a, 0 for o) are well-known to attackers")
        penalty_factor *= 0.15

    # ── 5. Keyboard walk check ────────────────────────────────────────────────
    walk_len = check_keyboard_walk(password)
    if walk_len >= 6:
        issues.append(f"❌ Long keyboard walk pattern detected ({walk_len} chars)")
        suggestions.append("Avoid sequences like 'qwerty', 'asdfgh', '1q2w3e'")
        penalty_factor *= 0.2
    elif walk_len >= 4:
        issues.append(f"⚠ Keyboard walk pattern detected ({walk_len} chars)")
        suggestions.append("Avoid keyboard patterns like 'qwer' or 'asdf'")
        penalty_factor *= 0.6

    # ── 6. Sequential characters ──────────────────────────────────────────────
    seq_len = check_sequential(password)
    if seq_len >= 5:
        issues.append(f"❌ Sequential characters detected ({seq_len} chars, e.g. 'abcde' or '12345')")
        suggestions.append("Avoid alphabetical or numerical sequences")
        penalty_factor *= 0.3
    elif seq_len >= 4:
        issues.append(f"⚠ Short sequential pattern detected ({seq_len} chars)")
        penalty_factor *= 0.7

    # ── 7. Repeated characters ────────────────────────────────────────────────
    repeat_ratio = check_repeats(password)
    if repeat_ratio >= 0.6:
        issues.append(f"❌ Many repeated characters ({int(repeat_ratio*100)}% of the password)")
        suggestions.append("Avoid repeating the same characters (e.g., 'aaaa', '1111')")
        penalty_factor *= 0.2
    elif repeat_ratio >= 0.4:
        issues.append(f"⚠ Some repeated characters detected")
        penalty_factor *= 0.7

    # ── 8. Date pattern ───────────────────────────────────────────────────────
    if check_date_pattern(password):
        issues.append("⚠ Date or year pattern detected (e.g. 1990, 12.05.1990)")
        suggestions.append("Avoid including birth years or dates — attackers try these first")
        penalty_factor *= 0.7

    # ── 9. All same case ──────────────────────────────────────────────────────
    if password.islower() and L < 16:
        issues.append("⚠ All lowercase letters")
        suggestions.append("Add uppercase letters, digits or symbols")
    elif password.isupper() and L < 16:
        issues.append("⚠ All uppercase letters")
        suggestions.append("Mix in lowercase, digits, or symbols")

    # ── 10. All digits ────────────────────────────────────────────────────────
    if password.isdigit():
        issues.append("❌ Password is all digits (PIN-style)")
        suggestions.append("Add letters and symbols to dramatically increase strength")
        penalty_factor *= 0.3

    # ── Calculate final entropy ───────────────────────────────────────────────
    raw_entropy = calculate_entropy(password)
    adjusted_entropy = raw_entropy * penalty_factor

    # ── Map entropy to score 0-4 ──────────────────────────────────────────────
    if adjusted_entropy < 28:
        score = 0
    elif adjusted_entropy < 36:
        score = 1
    elif adjusted_entropy < 60:
        score = 2
    elif adjusted_entropy < 80:
        score = 3
    else:
        score = 4

    # ── Positive notes ────────────────────────────────────────────────────────
    if not issues:
        issues.append("✅ No common weaknesses detected!")

    if L >= 16 and variety >= 3:
        suggestions.insert(0, "✅ Great length and variety — very strong!")
    elif L >= 12 and variety >= 3:
        suggestions.insert(0, "✅ Good length and variety!")

    crack_time = estimate_crack_time(adjusted_entropy)
    return score, round(adjusted_entropy, 1), issues, suggestions, crack_time


# ─── Part 3 - UI: Password Strength Checker ──────────────────────────────────

STRENGTH_COLORS  = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"]
STRENGTH_LABELS  = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
STRENGTH_BAR_PCT = [0.15, 0.30, 0.55, 0.78, 1.00]

def update_strength_display(*args):
    password = checker_entry.get()

    if not password:
        bar_canvas.coords(bar_fill, 0, 0, 0, 20)
        bar_canvas.itemconfig(bar_fill, fill="#dddddd")
        strength_label_var.set("")
        entropy_label_var.set("")
        crack_label_var.set("")
        for lbl in issue_labels:
            lbl.config(text="")
        for lbl in suggestion_labels:
            lbl.config(text="")
        return

    score, entropy, issues, suggestions, crack_time = analyze_password(password)

    # ── Animated strength bar ──────────────────────────────────────────────
    bar_width = int(BAR_TOTAL_WIDTH * STRENGTH_BAR_PCT[score])
    bar_canvas.coords(bar_fill, 0, 0, bar_width, 20)
    bar_canvas.itemconfig(bar_fill, fill=STRENGTH_COLORS[score])

    # ── Labels ─────────────────────────────────────────────────────────────
    strength_label_var.set(f"{STRENGTH_LABELS[score]}")
    strength_score_label.config(fg=STRENGTH_COLORS[score])
    entropy_label_var.set(f"Entropy: {entropy} bits")
    crack_label_var.set(f"Estimated crack time: {crack_time}")

    # ── Issues list — FIX: cap at label count to avoid index errors ────────
    for i, lbl in enumerate(issue_labels):
        if i < len(issues):
            lbl.config(text=issues[i])
        else:
            lbl.config(text="")

    # ── Suggestions list — FIX: cap at label count ─────────────────────────
    for i, lbl in enumerate(suggestion_labels):
        if i < len(suggestions):
            lbl.config(text=suggestions[i])
        else:
            lbl.config(text="")

def toggle_password_visibility():
    if checker_entry.cget("show") == "*":
        checker_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        checker_entry.config(show="*")
        show_btn.config(text="Show")


# ─── Neon helper: draw glowing border on a Frame via Canvas overlay ──────────
def neon_border(parent, color, thickness=2):
    """Draws a glowing neon border inside a frame using a Canvas."""
    c = tk.Canvas(parent, bg=parent.cget("bg"), bd=0, highlightthickness=0)
    c.place(relwidth=1, relheight=1)
    def _redraw(event=None):
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 4 or h < 4:
            return
        layers = [(4, 0.12), (3, 0.22), (2, 0.40), (1, 0.70), (0, 1.0)]
        r, g, b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
        for offset, alpha in layers:
            shade = f"#{int(r*alpha):02x}{int(g*alpha):02x}{int(b*alpha):02x}"
            c.create_rectangle(offset, offset, w-offset, h-offset,
                               outline=shade, width=1)
    c.bind("<Configure>", _redraw)
    parent.after(50, _redraw)
    return c

# ─── Root ────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Password Suite")
root.geometry("900x620")
root.configure(bg=BG_DARK)
root.resizable(False, False)

# ─── Grid background helper ───────────────────────────────────────────────────
def draw_grid(canvas, color="#14142a", step=40):
    """Fill a canvas with a subtle dot/line grid."""
    def _draw(event=None):
        canvas.delete("grid")
        w, h = canvas.winfo_width(), canvas.winfo_height()
        for x in range(0, w, step):
            canvas.create_line(x, 0, x, h, fill=color, tags="grid")
        for y in range(0, h, step):
            canvas.create_line(0, y, w, y, fill=color, tags="grid")
    canvas.bind("<Configure>", _draw)
    canvas.after(50, _draw)

# ─── Main container (the 3-card menu) ────────────────────────────────────────
menu_frame = tk.Frame(root, bg=BG_DARK)
menu_frame.place(relwidth=1, relheight=1)
menu_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")
menu_frame.grid_rowconfigure(0, weight=1)

menu_grid = tk.Canvas(menu_frame, bg=BG_DARK, bd=0, highlightthickness=0)
menu_grid.place(relwidth=1, relheight=1)
draw_grid(menu_grid)

# ─── Page frames ─────────────────────────────────────────────────────────────
page1 = tk.Frame(root, bg=BG_CARD)
page2 = tk.Frame(root, bg=BG_CARD)
page3 = tk.Frame(root, bg=BG_CARD)

for page in (page1, page2, page3):
    page.place(relwidth=1, relheight=1)
    pg = tk.Canvas(page, bg=BG_CARD, bd=0, highlightthickness=0)
    pg.place(relwidth=1, relheight=1)
    draw_grid(pg, color="#111122")

# ─── Page 1 content ──────────────────────────────────────────────────────────
tk.Label(page1, text="PASSWORD GENERATOR  //  PRIVATE DATA", font=("Courier", 16, "bold"), bg=BG_CARD, fg=CYAN).pack(pady=35)

tk.Label(page1, text="// NAME", bg=BG_CARD, fg=FG_DIM, font=("Courier", 10)).pack(pady=(10,2))
name_entry = tk.Entry(page1, font=("Courier", 12), width=44, bg=BG_WIDGET, fg=CYAN,
                      insertbackground=CYAN, relief="flat",
                      highlightthickness=1, highlightcolor=CYAN, highlightbackground=CYAN)
name_entry.pack(ipady=5)

tk.Label(page1, text="// LAST NAME", bg=BG_CARD, fg=FG_DIM, font=("Courier", 10)).pack(pady=(12,2))
lname_entry = tk.Entry(page1, font=("Courier", 12), width=44, bg=BG_WIDGET, fg=CYAN,
                       insertbackground=CYAN, relief="flat",
                       highlightthickness=1, highlightcolor=CYAN, highlightbackground=CYAN)
lname_entry.pack(ipady=5)

tk.Label(page1, text="// DATE OF BIRTH  [ DD.MM.YYYY ]", bg=BG_CARD, fg=FG_DIM, font=("Courier", 10)).pack(pady=(12,2))
date_entry = tk.Entry(page1, font=("Courier", 12), width=44, bg=BG_WIDGET, fg=CYAN,
                      insertbackground=CYAN, relief="flat",
                      highlightthickness=1, highlightcolor=CYAN, highlightbackground=CYAN)
date_entry.pack(ipady=5)

btn_row1 = tk.Frame(page1, bg=BG_CARD)
btn_row1.pack(pady=22)
tk.Button(btn_row1, text="[ GENERATE ]", font=("Courier", 12, "bold"), width=14,
          command=get_information,
          bg=BG_WIDGET, fg=CYAN, activebackground=BG_DARK, activeforeground=CYAN,
          relief="flat", highlightthickness=1, highlightbackground=CYAN).pack(side="left", padx=10)
tk.Button(btn_row1, text="[ CLEAR ]", font=("Courier", 12, "bold"), width=10,
          command=clear,
          bg=BG_WIDGET, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN,
          relief="flat", highlightthickness=1, highlightbackground=FG_DIM).pack(side="left", padx=10)

tk.Button(page1, text="← BACK", font=("Courier", 11), command=lambda: show_frame(menu_frame),
          bg=BG_CARD, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN, relief="flat").pack(pady=15)

# ─── Page 2 content ──────────────────────────────────────────────────────────
tk.Label(page2, text="PASSWORD GENERATOR  //  RANDOM", font=("Courier", 16, "bold"), bg=BG_CARD, fg=PINK).pack(pady=25)
tk.Label(page2, text="// LENGTH", bg=BG_CARD, fg=FG_DIM, font=("Courier", 10)).pack(pady=(8,2))

length_spinbox = tk.Spinbox(page2, from_=8, to=64, width=8, font=("Courier", 14), justify="center",
                             bg=BG_WIDGET, fg=PINK, buttonbackground=BG_WIDGET,
                             highlightthickness=1, highlightcolor=PINK, highlightbackground=PINK,
                             insertbackground=PINK, relief="flat")
length_spinbox.delete(0, tk.END)
length_spinbox.insert(0, "8")
length_spinbox.pack(ipady=4)

uppercase_var = tk.BooleanVar(value=True)
digit_var     = tk.BooleanVar(value=True)
special_var   = tk.BooleanVar()

checkbox_frame = tk.Frame(page2, bg=BG_CARD)
checkbox_frame.pack(pady=12)

for var, label in [(uppercase_var, "[ A-Z ]  Include Uppercase Letters"),
                   (digit_var,     "[ 0-9 ]  Include Digits"),
                   (special_var,   "[ !@# ]  Include Special Characters")]:
    tk.Checkbutton(checkbox_frame, text=label, variable=var,
                   bg=BG_CARD, fg=FG_MAIN, selectcolor=BG_WIDGET,
                   activebackground=BG_CARD, activeforeground=PINK,
                   font=("Courier", 11)).pack(anchor="w", pady=4)

button_row = tk.Frame(page2, bg=BG_CARD)
button_row.pack(pady=12)
tk.Button(button_row, text="[ GENERATE ]", font=("Courier", 12, "bold"), width=14,
          command=generate_random_password,
          bg=BG_WIDGET, fg=PINK, activebackground=BG_DARK, activeforeground=PINK,
          relief="flat", highlightthickness=1, highlightbackground=PINK).pack(side="left", padx=10)
tk.Button(button_row, text="[ CLEAR ]", font=("Courier", 12, "bold"), width=10,
          command=clear_random,
          bg=BG_WIDGET, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN,
          relief="flat", highlightthickness=1, highlightbackground=FG_DIM).pack(side="left", padx=10)

result_frame = tk.Frame(page2, bg=BG_CARD)
result_frame.pack(pady=8)
result_entry = tk.Entry(result_frame, font=("Courier", 13), width=32, state="readonly",
                        bg=BG_WIDGET, fg=GREEN, readonlybackground=BG_WIDGET,
                        highlightthickness=1, highlightcolor=GREEN, highlightbackground=GREEN,
                        relief="flat")
result_entry.pack(side="left", padx=5, ipady=5)
tk.Button(result_frame, text="COPY", font=("Courier", 10, "bold"), width=6,
          command=lambda: copy_to_clipboard(result_entry.get()),
          bg=BG_WIDGET, fg=GREEN, activebackground=BG_DARK, activeforeground=GREEN,
          relief="flat", highlightthickness=1, highlightbackground=GREEN).pack(side="left", padx=3)

tk.Button(page2, text="← BACK", font=("Courier", 11), command=lambda: show_frame(menu_frame),
          bg=BG_CARD, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN, relief="flat").pack(pady=15)

# ─── Page 3 content: Strength Checker ────────────────────────────────────────
tk.Label(page3, text="PASSWORD STRENGTH CHECKER", font=("Courier", 16, "bold"), bg=BG_CARD, fg=GREEN).pack(pady=16)

entry_frame = tk.Frame(page3, bg=BG_CARD)
entry_frame.pack(pady=6)

checker_var = tk.StringVar()
checker_var.trace_add("write", update_strength_display)
checker_entry = tk.Entry(entry_frame, textvariable=checker_var, font=("Courier", 13),
                         width=34, show="*", relief="flat", bd=0,
                         bg=BG_WIDGET, fg=GREEN, insertbackground=GREEN,
                         highlightthickness=1, highlightcolor=GREEN, highlightbackground=GREEN)
checker_entry.pack(side="left", padx=5, ipady=5)

show_btn = tk.Button(entry_frame, text="SHOW", font=("Courier", 10, "bold"), width=6,
                     command=toggle_password_visibility,
                     bg=BG_WIDGET, fg=GREEN, activebackground=BG_DARK, activeforeground=GREEN,
                     relief="flat", highlightthickness=1, highlightbackground=GREEN)
show_btn.pack(side="left", padx=4)

copy_btn = tk.Button(entry_frame, text="COPY", font=("Courier", 10, "bold"), width=6,
                     command=lambda: copy_to_clipboard(checker_entry.get()),
                     bg=BG_WIDGET, fg=GREEN, activebackground=BG_DARK, activeforeground=GREEN,
                     relief="flat", highlightthickness=1, highlightbackground=GREEN)
copy_btn.pack(side="left", padx=2)

# ── Strength bar ──────────────────────────────────────────────────────────────
bar_outer = tk.Frame(page3, bg=BAR_EMPTY, width=BAR_TOTAL_WIDTH, height=16, bd=0, relief="flat",
                     highlightthickness=1, highlightbackground="#1a1a33")
bar_outer.pack(pady=8)
bar_outer.pack_propagate(False)

bar_canvas = tk.Canvas(bar_outer, width=BAR_TOTAL_WIDTH, height=16,
                       bg=BAR_EMPTY, bd=0, highlightthickness=0)
bar_canvas.pack()
bar_fill = bar_canvas.create_rectangle(0, 0, 0, 16, fill=BAR_EMPTY, outline="")

# ── Score label ───────────────────────────────────────────────────────────────
strength_label_var = tk.StringVar(value="")
strength_score_label = tk.Label(page3, textvariable=strength_label_var,
                                font=("Courier", 15, "bold"), bg=BG_CARD, fg=GREEN)
strength_score_label.pack()

# ── Entropy + Crack time ──────────────────────────────────────────────────────
entropy_label_var = tk.StringVar(value="")
tk.Label(page3, textvariable=entropy_label_var,
         font=("Courier", 10), bg=BG_CARD, fg=FG_DIM).pack()

crack_label_var = tk.StringVar(value="")
tk.Label(page3, textvariable=crack_label_var,
         font=("Courier", 10, "italic"), bg=BG_CARD, fg=FG_DIMMER).pack(pady=2)

# Divider
sep = tk.Canvas(page3, height=1, bg=BG_CARD, bd=0, highlightthickness=0)
sep.pack(fill="x", padx=60, pady=4)
sep.create_line(0, 0, 900, 0, fill="#1a2a3a")

# ── Issues + Suggestions columns ─────────────────────────────────────────────
columns_frame = tk.Frame(page3, bg=BG_CARD)
columns_frame.pack(pady=6, padx=20, fill="x")

issues_col = tk.Frame(columns_frame, bg=BG_CARD)
issues_col.pack(side="left", anchor="n", padx=20, fill="x", expand=True)
tk.Label(issues_col, text="//  ANALYSIS", font=("Courier", 11, "bold"),
         bg=BG_CARD, fg="#ff4466").pack(anchor="w")

issue_labels = []
for _ in range(6):
    lbl = tk.Label(issues_col, text="", font=("Courier", 9), bg=BG_CARD,
                   fg="#ff6688", wraplength=300, justify="left", anchor="w")
    lbl.pack(anchor="w", pady=1)
    issue_labels.append(lbl)

sug_col = tk.Frame(columns_frame, bg=BG_CARD)
sug_col.pack(side="left", anchor="n", padx=20, fill="x", expand=True)
tk.Label(sug_col, text="//  SUGGESTIONS", font=("Courier", 11, "bold"),
         bg=BG_CARD, fg=GREEN).pack(anchor="w")

suggestion_labels = []
for _ in range(6):
    lbl = tk.Label(sug_col, text="", font=("Courier", 9), bg=BG_CARD,
                   fg="#00cc70", wraplength=300, justify="left", anchor="w")
    lbl.pack(anchor="w", pady=1)
    suggestion_labels.append(lbl)

tk.Button(page3, text="← BACK", font=("Courier", 11), command=lambda: show_frame(menu_frame),
          bg=BG_CARD, fg=FG_DIM, activebackground=BG_DARK, activeforeground=FG_MAIN, relief="flat").pack(pady=8)

# ─── Menu cards ──────────────────────────────────────────────────────────────
frame1 = tk.Frame(menu_frame, bg=BG_CARD)
frame1.grid(row=0, column=0, sticky="nsew", padx=12, pady=15)
neon_border(frame1, CYAN)

frame2 = tk.Frame(menu_frame, bg=BG_CARD)
frame2.grid(row=0, column=1, sticky="nsew", padx=4, pady=15)
neon_border(frame2, PINK)

frame3 = tk.Frame(menu_frame, bg=BG_CARD)
frame3.grid(row=0, column=2, sticky="nsew", padx=12, pady=15)
neon_border(frame3, GREEN)

tk.Label(frame1, text="Password Generator\n(Based on Private Data)", bg=BG_CARD, fg=CYAN,  font=("Courier", 13, "bold")).pack(pady=110)
tk.Label(frame2, text="Password Generator\n(Random)",                bg=BG_CARD, fg=PINK,  font=("Courier", 13, "bold")).pack(pady=110)
tk.Label(frame3, text="Password Strength\nChecker",                  bg=BG_CARD, fg=GREEN, font=("Courier", 13, "bold")).pack(pady=110)

tk.Button(frame1, text="[ ENTER ]", font=("Courier", 13, "bold"), width=12, height=2,
          command=lambda: show_frame(page1),
          bg=BG_WIDGET, fg=CYAN, activebackground=BG_DARK, activeforeground=CYAN, relief="flat", bd=0,
          highlightthickness=1, highlightbackground=CYAN).pack(side="bottom", pady=90)

tk.Button(frame2, text="[ ENTER ]", font=("Courier", 13, "bold"), width=12, height=2,
          command=lambda: show_frame(page2),
          bg=BG_WIDGET, fg=PINK, activebackground=BG_DARK, activeforeground=PINK, relief="flat", bd=0,
          highlightthickness=1, highlightbackground=PINK).pack(side="bottom", pady=90)

tk.Button(frame3, text="[ ENTER ]", font=("Courier", 13, "bold"), width=12, height=2,
          command=lambda: show_frame(page3),
          bg=BG_WIDGET, fg=GREEN, activebackground=BG_DARK, activeforeground=GREEN, relief="flat", bd=0,
          highlightthickness=1, highlightbackground=GREEN).pack(side="bottom", pady=90)

show_frame(menu_frame)
root.mainloop()
