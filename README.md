Great question 🚀 — Python 2.7 (released in 2010, EOL in 2020) and Python 3.12 (released in 2023) are worlds apart. Here’s a **solid list of 10 key differences** you can confidently bring up in interviews or discussions:

---

## 🔟 Solid Differences Between Python 2.7 and Python 3.12

### 1. **Print Statement vs Print Function**

* **Python 2.7**: `print "Hello"` (statement)
* **Python 3.12**: `print("Hello")` (function, supports advanced features like `sep`, `end`)

---

### 2. **Integer Division**

* **Python 2.7**: `/` does floor division if both operands are integers

  ```python
  print(5 / 2)   # 2
  ```
* **Python 3.12**: `/` always gives float, `//` is floor division

  ```python
  print(5 / 2)   # 2.5
  ```

---

### 3. **Unicode Handling**

* **Python 2.7**: Strings are ASCII by default; Unicode needs `u"hello"`
* **Python 3.12**: Strings are Unicode by default

---

### 4. **Input Function**

* **Python 2.7**: `input()` evaluates input as code; `raw_input()` for plain text
* **Python 3.12**: Only `input()`, always returns a string

---

### 5. **Range / xrange**

* **Python 2.7**: `range()` returns a list, `xrange()` returns a generator-like object
* **Python 3.12**: `range()` returns a lazy, memory-efficient sequence (like `xrange`)

---

### 6. **Exceptions Syntax**

* **Python 2.7**:

  ```python
  except ValueError, e:
      print e
  ```
* **Python 3.12**:

  ```python
  except ValueError as e:
      print(e)
  ```

---

### 7. **Iterators in Built-ins**

* **Python 2.7**:

  * `dict.keys()`, `dict.values()` return lists
* **Python 3.12**:

  * `dict.keys()`, `dict.values()` return *views* (dynamic, memory efficient)

---

### 8. **Libraries & Ecosystem**

* **Python 2.7**: No new features after 2020, ecosystem frozen.
* **Python 3.12**: Active development, modern libraries (asyncio, type hints, dataclasses, pattern matching, etc.)

---

### 9. **Advanced Language Features**

* **Python 2.7**: No support for f-strings, type hints, async/await, data classes, pattern matching.
* **Python 3.12**:

  * f-strings: `f"Hello {name}"`
  * type hints: `def add(x: int, y: int) -> int:`
  * `async`/`await` for concurrency
  * `match` statements (structural pattern matching, introduced in 3.10)

---

### 10. **Performance and Internals**

* **Python 2.7**: Uses legacy CPython interpreter; slower, no modern optimizations.
* **Python 3.12**:

  * Faster CPython with performance improvements (PEP 659 adaptive interpreter, zero-cost exceptions).
  * Better memory management, optimized garbage collector.

---

✅ **Summary:**
Python 2.7 is **legacy**, with outdated syntax and limitations. Python 3.12 is **modern, faster, safer, and feature-rich**. Migrating is a must for compatibility, performance, and long-term support.

---

👉 Do you want me to also make you a **table version (Python 2.7 vs 3.12 side-by-side)** so it’s easier to recall quickly in interviews?


Great question 🙌 — Python has a set of **reserved words (keywords)** that you **cannot use as variable names, function names, or identifiers** because they have special meaning in the language.

You can always check the current list in your version of Python with:

```python
import keyword
print(keyword.kwlist)
```

---

## 🔹 Reserved Words in Python 3.12

(There are **36 keywords** as of Python 3.12)

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

---

## 🔹 Explanation

* **Boolean / Null**: `True`, `False`, `None`
* **Control Flow**: `if`, `else`, `elif`, `for`, `while`, `break`, `continue`, `return`, `yield`, `try`, `except`, `finally`, `raise`, `assert`
* **Functions & Classes**: `def`, `class`, `lambda`
* **Imports & Modules**: `import`, `from`, `as`
* **Scope & Variables**: `global`, `nonlocal`, `del`
* **Async**: `async`, `await`
* **Operators (logical)**: `and`, `or`, `not`, `is`, `in`
* **Context**: `with`, `pass`

---

✅ Reserved words are case-sensitive (`True` is a keyword, but `true` is not).
✅ The set of keywords can slightly differ across Python versions (older versions had `print`, `exec`, etc. as keywords).

---

Do you want me to also make you a **cheat sheet table (keyword + short meaning)** so it’s easier to memorize for interviews?

Yes 😃 Python has a few fun libraries for **text-based drawings / ASCII art**, similar to `cowsay` in Unix.

Here are some popular ones:

---

### 🐮 1. [`cowsay`](https://pypi.org/project/cowsay/) (Python port of classic cowsay)

* Brings the classic \*nix `cowsay` tool to Python.
* Supports different “characters” (cow, dragon, tux, etc.).

```python
import cowsay

cowsay.cow("Hello, world!")
cowsay.tux("I am Linux penguin!")
```

---

### ✏️ 2. [`art`](https://pypi.org/project/art/)

* ASCII art text generator.
* Can draw **decorative text** and predefined art objects.

```python
from art import *
print(text2art("HELLO"))
print(art("happy"))
```

---

### 🎨 3. [`pyfiglet`](https://pypi.org/project/pyfiglet/)

* Python port of `FIGlet` → generates fancy text banners.

```python
import pyfiglet

print(pyfiglet.figlet_format("Python"))
```

---

### 🖼️ 4. [`asciimatics`](https://pypi.org/project/asciimatics/)

* More advanced: animations, full-screen text UIs, and ASCII art.
* Useful for making retro-style terminal apps.

---

### 🐍 5. [`termgraph`](https://pypi.org/project/termgraph/)

* Not art, but lets you **draw graphs and charts** in text.
* Great for visualizing numbers in CLI.

---

👉 So for something like **cowsay specifically**, you can use the Python `cowsay` package. For **big ASCII text**, use `pyfiglet` or `art`. For **animations**, use `asciimatics`.

---

Would you like me to show you a **combined demo script** that prints:

1. A `cowsay` cow 🐮
2. A `pyfiglet` banner
3. An `art` drawing

all in one terminal run?

Great question 👍 This is a **common issue** in Python projects when your tests can’t find code inside a `src/` folder.

There are a few ways to add `src` to the `PYTHONPATH` when running pytest:

---

### ✅ 1. Recommended: use `pytest` with `PYTHONPATH`

Run pytest with the environment variable set:

```bash
PYTHONPATH=src pytest
```

This tells Python to include `src/` when resolving imports.

---

### ✅ 2. Add `src/` to `sys.path` in `conftest.py`

Inside your `tests/conftest.py` (runs before tests):

```python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
```

This ensures all tests can import from `src/`.

---

### ✅ 3. Use `pytest.ini` or `pyproject.toml`

If you don’t want to mess with environment variables, configure pytest:

**pytest.ini**

```ini
[pytest]
pythonpath = src
```

or in **pyproject.toml**

```toml
[tool.pytest.ini_options]
pythonpath = [
    "src"
]
```

---

### ✅ 4. Install your package in editable mode

If your `src/` contains a package (with `setup.py` or `pyproject.toml`):

```bash
pip install -e .
pytest
```

This way imports just work, no need to hack paths.

---

🔑 **Best Practice:**
If this is a proper Python package → go with **editable install (`pip install -e .`)**.
If it’s just a project with loose scripts → add `pythonpath = src` in `pytest.ini`.

---

👉 Do you want me to show you a **sample folder structure** (`src/`, `tests/`, config) and how to set it up for pytest?

Got it 👍 Let’s go step by step with **`set`** and **`frozenset`** in Python.

---

## 🔹 `set`

* **Mutable collection** of **unique elements**.
* Supports operations like **add**, **remove**, **union**, **intersection**, etc.
* Not hashable (can’t be used as a dictionary key or inside another set).

### Example:

```python
# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" ignored
print(fruits)   # {'apple', 'banana', 'cherry'}

# Add and remove
fruits.add("orange")
fruits.remove("banana")
print(fruits)   # {'apple', 'cherry', 'orange'}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # union → {1, 2, 3, 4, 5}
print(a & b)  # intersection → {3}
print(a - b)  # difference → {1, 2}
```

---

## 🔹 `frozenset`

* **Immutable version** of `set`.
* Once created, elements cannot be added or removed.
* **Hashable** → can be used as dictionary keys or stored in other sets.
* Still supports set operations like union, intersection, difference.

### Example:

```python
# Creating frozenset
fs = frozenset([1, 2, 3, 2, 1])
print(fs)   # frozenset({1, 2, 3})

# Immutable → cannot do fs.add() or fs.remove()
# fs.add(4)  # ❌ AttributeError

# But you can still do set operations
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})
```

---

## 🔑 Differences between `set` and `frozenset`

| Feature    | `set`                              | `frozenset`                         |
| ---------- | ---------------------------------- | ----------------------------------- |
| Mutability | Mutable (can add/remove)           | Immutable (cannot change)           |
| Hashable   | ❌ No                               | ✅ Yes (can be dict key)             |
| Use Case   | For collections you need to modify | For fixed collections, safe as keys |
| Syntax     | `{1, 2, 3}`                        | `frozenset([1, 2, 3])`              |

---

✅ **When to use which?**

* Use **`set`** when you need a dynamic collection (adding/removing).
* Use **`frozenset`** when you need an **unchangeable, hashable collection**, e.g., as a key in a dictionary.

---

Would you like me to also show you a **real-world example** where `frozenset` is required but `set` would fail?

