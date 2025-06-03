
# 📧 Email Variation Generator

## 📝 Description

The **Email Variation Generator** is a desktop application with a graphical interface that allows you to generate all possible variations of a Gmail email address by adding dots (`.`) to the local part of the email. Gmail ignores dots in the local part, so all variations will arrive in the same inbox.

### Example:

- **Original email:** `prueba@gmail.com`  
- **Variations generated:**
  ```
  p.rueba@gmail.com
  pr.ueba@gmail.com
  pru.eba@gmail.com
  ...
  ```

These variations are useful for testing, multiple registrations, or avoiding restrictions on forms that require unique emails.

---

## 💻 Features

- Graphical user interface (GUI) using **Tkinter**
- Automatic generation of all combinations with dots
- Display of results in a scrollable text area
- Button to copy all variations to the clipboard
- Email format validation

---

## 🛠 Requirements

This script requires **Python 3** and the installation of the `pyperclip` module.

Installing dependencies:

```bash
pip install pyperclip
```

---

## 📂 Project Structure

- `email_variation_generator.py` – Main application script

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Install the dependency with pip:
   ```bash
   pip install pyperclip
   ```
3. Save the code in a file called `email_variation_generator.py`.
4. Run the script with:
   ```bash
   python3 email_variation_generator.py
   ```

---

## 🧠 How It Works

1. **Input:** The user enters a valid email address (e.g., `ejemplo@gmail.com`).
2. **Validation:** The system verifies that the email address contains an `@` symbol.
3. **Generation of Variations:**
   - All possible combinations of positions for inserting dots in the local part (before the `@` symbol) are generated.
   - A period is inserted in each combination of positions without repetition.
4. **Output:** The variations are displayed in a text area.
5. **Copy:** A button allows all generated variations to be copied to the clipboard.

---

## 🔒 Notes

- This system **is only valid for Gmail accounts**, as only Gmail ignores dots in the local part of the email address.
- It should not be used for malicious activities or to evade verification systems without authorization.

---

## 📄 License

This project can be used freely for educational and personal purposes. If you wish to integrate it into commercial software, we recommend reviewing Gmail's email usage policies.

---