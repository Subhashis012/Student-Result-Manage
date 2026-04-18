# 🎓 Student Result Manager

A simple yet functional **command-line application** built with Python that helps manage student records and check their exam results. Data is automatically persisted between sessions using a local JSON file — no database required!

---

## 📋 Features

- ✅ **Add Students** — Store student names and their marks
- 📊 **View All Students** — Tabular display with Name, Marks, and Pass/Fail result
- 🔍 **Check Individual Result** — Instantly check if a specific student passed or failed
- 💾 **Auto-Save** — Data is automatically saved to a JSON file after every addition
- 🚪 **Save & Exit / Exit Without Saving** — Flexible exit options
- 🔁 **Persistent Data** — Student records survive across program restarts

---

## 🗂️ Project Structure

```
Student Result Manage/
│
├── student_result_manager.py   # Main application script
├── students_data.json          # Auto-generated data file (created on first run)
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your system
- No external libraries required — uses only Python built-ins (`json`, `os`)

### Running the App

```bash
python student_result_manager.py
```

---

## 🖥️ How to Use

When you run the program, you'll see this menu:

```
------- STUDENT MANAGER APP-------
1. Add Student
2. View All Students
3. Check Result
4. Save & Exit
5. Exit Without Saving
Enter Your Choice (1-5):
```

### Option 1 — Add Student
Enter the student's name and their marks (integer). Data is **auto-saved** immediately.

```
Enter Student Name: Subhashis
Enter marks: 85
Subhashis's marks added!
Data saved successfully!
```

### Option 2 — View All Students
Displays all stored students in a formatted table:

```
Name                 Marks      Result
----------------------------------------
Subhashis            85         PASS
Udit                 75         PASS
Rahul                25         FAIL
```

### Option 3 — Check Result
Enter a student's name to check their individual result:

```
Enter student name to check result: Udit
Result for Udit (Marks: 75): PASS
```

### Option 4 — Save & Exit
Saves all current data to `students_data.json` and exits the program.

### Option 5 — Exit Without Saving
Exits the program **without** saving any changes made in the current session.

---

## 📁 Data Storage

Student data is stored locally in `students_data.json` in the following format:

```json
{
    "Subhashis": 85,
    "Udit": 75,
    "Rahul": 25
}
```

This file is **auto-created** on the first run and **auto-loaded** every time the program starts.

---

## 🏆 Pass/Fail Criteria

| Marks       | Result |
|-------------|--------|
| 40 or above | ✅ PASS |
| Below 40    | ❌ FAIL |

---

## 🛠️ Tech Stack

| Technology | Usage                        |
|------------|------------------------------|
| Python 3   | Core programming language    |
| `json`     | Data serialization/storage   |
| `os`       | File existence checking      |

---

## 🤝 Contributing

Feel free to fork this repository, improve the code, and submit a pull request!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## 👤 Author

**Subhashis Dhara**  
🔗 [GitHub Profile](https://github.com/Subhashis012)

---

> 💡 *This project is great for beginners learning Python file I/O, dictionaries, and CLI application design.*
