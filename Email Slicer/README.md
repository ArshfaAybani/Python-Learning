# Python Email Slicer

A simple command-line Python program that extracts the **username** and **domain** from an email address using string slicing.

This project was created as part of my Python learning journey to practice string manipulation and user input.

---

## Features

- Accepts an email address from the user
- Extracts the username (before `@`)
- Extracts the domain (after `@`)
- Displays the extracted information in a clean format

---

## 🛠️ Technologies Used

- Python 3

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/ArshfaAybani/Python-Learning.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Python-Learning/Email_Slicer
   ```

3. Run the program:

   ```bash
   python emailSlicer.py
   ```

---

## Example

**Input**

```text
Enter your email: johndoe@gmail.com
```

**Output**

```text
Your username is johndoe and your domain is gmail.com
```

---

## Concepts Practiced

- Variables
- User Input (`input()`)
- String Indexing
- String Slicing
- The `.index()` Method
- Formatted Strings (f-strings)

---

## Purpose

This project was built to strengthen my understanding of Python string operations and how data can be extracted from user input using indexing and slicing.

---

## Future Improvements

- Validate email format before processing
- Handle invalid input without crashing
- Accept multiple email addresses
- Display additional information such as domain extension (`.com`, `.org`, `.edu`, etc.)
- Support emails containing multiple subdomains

---

⭐ If you found this project useful or are also learning Python, feel free to star the repository!
