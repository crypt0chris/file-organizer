![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

# 📁 File Organizer

A simple and efficient Python script that organizes files in a directory by their file extensions. Great for decluttering download folders, project directories, or any messy workspace.

## ⚙️ Features

- Automatically sorts files into subfolders by extension
- Handles files without extensions and hidden files
- Skips system or protected files
- Safe: avoids overwriting and moves files intelligently
- Lightweight, no dependencies outside the standard library

## 🚀 Usage

```bash
python3 organizer.py /path/to/your/folder
```

> **Note:** It's recommended to back up your files before organizing, especially when working with important or unsorted data.

If no path is provided, it will default to the current directory.

## 📂 Example

Before:

```
/Downloads
  ├── image.png
  ├── doc.pdf
  ├── notes.txt
  ├── archive.zip
```

After running the script:

```
/Downloads
  ├── png/
  │   └── image.png
  ├── pdf/
  │   └── doc.pdf
  ├── txt/
  │   └── notes.txt
  ├── zip/
  │   └── archive.zip
```

## 📄 License

MIT License
