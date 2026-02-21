
```markdown
# Expense Tracker CLI 💰

A simple and efficient Command Line Interface (CLI) application built with Python to manage and track your daily expenses.

## ✨ Features
* **Rich Terminal UI:** Beautifully formatted tables and colored output using the `Rich` library.
* **Smart Summaries:** Calculate total expenses for all time or filter by a specific month.
* **Error Handling:** Robust management of missing files and invalid JSON data.
* **Developer Friendly:** Clean project structure with `.gitignore` and `requirements.txt`.
```
## 🚀 Installation

1. **Clone the repository:**


   ```bash
   git clone [https://github.com/jasurxayitmuradov/expense-tracker.git](https://github.com/jasurxayitmuradov/expense-tracker.git)
   cd expense-tracker


2. **Set up a virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# .venv\Scripts\activate     # On Windows

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



## 🛠 Usage

You can interact with the application using the following commands:

* **List all expenses:**
```bash
python3 main.py list

```


* **View total summary:**
```bash
python3 main.py summary

```


* **Filter summary by month (e.g., August):**
```bash
python3 main.py summary --month 8

```



## 📂 Project Structure

* `main.py`: The entry point of the application.
* `data.json`: Local storage for your expense data (auto-generated).
* `requirements.txt`: List of Python packages required for the project.
* `.gitignore`: Configured to exclude `.venv` and local data files.

## 📦 Built With

* [Rich](https://github.com/Textualize/rich) - For beautiful terminal formatting.
* [Python 3.12+](https://www.python.org/) - The core programming language.

---

**Author:** [Jasur Xayitmuradov](https://www.google.com/search?q=https://github.com/jasurxayitmuradov)

```

https://roadmap.sh/projects/expense-tracker

