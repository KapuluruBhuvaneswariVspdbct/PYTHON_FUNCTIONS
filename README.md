# 🧠 Python Functions Repository

This repository contains code examples and explanations related to **Python functions**, including standard definitions, anonymous (lambda) functions, variable-length arguments, and recursive logic.

## 📚 Topics Covered

### 1️⃣ Regular Functions
Basic function creation, return values, parameters, and calling conventions.

> 📁 Folder: `01_functions`  
> 📄 Example: `def greet(name): return f"Hello, {name}!"`

---

### 2️⃣ Lambda Functions
One-liner anonymous functions, used with `map()`, `filter()`, and `sorted()`.

> 📁 Folder: `02_lambda_functions`  
> 📄 Example: `square = lambda x: x**2`

---

### 3️⃣ *args and **kwargs
Variable-length positional and keyword arguments for flexible function signatures.

> 📁 Folder: `03_args_kwargs`  
> 📄 Example: 
```python
def demo(*args, **kwargs): 
    print(args)
    print(kwargs)
```

---

### 4️⃣ Recursion
Functions that call themselves for repetitive tasks like factorial, Fibonacci, etc.

> 📁 Folder: `04_recursion`  
> 📄 Example:
```python
def factorial(n): 
    return 1 if n==0 else n * factorial(n-1)
```

---

## 🚀 How to Use

1. Clone or download this repository.
2. Navigate into any folder using a terminal or file explorer.
3. Run the `example.py` in that folder with:

```bash
python example.py
```

---

## 🙌 Contributing

You’re welcome to contribute improvements or new function examples.

---

## 👩‍💻 Created by BHUVANESWARI KAPULURU
Learning one function at a time!
