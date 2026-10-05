# smart-file-organizer
Smart File Organizer scans a target folder (Downloads by default) and automatically routes each file into a category folder — Images, Documents, Videos, Music, Archives, or Other — based on its file extension. It uses only Python's built-in os and shutil modules, requires no external dependencies, and asks for confirmation before making any changes.

This project was built as a hands-on exercise in using Python to interact with the operating system's file system — reading directory contents, inspecting file extensions, creating folders dynamically, and safely moving files without overwriting existing data.

It was also packaged into a standalone .exe using PyInstaller, so it can be run by someone with no Python installed at all.

## Features
* Safe by default — asks for confirmation before moving any files
* Automatic categorization — sorts files into folders based on extension (Images, Documents, Videos, Music, Archives, Other)
* Folder-safe — skips existing subfolders, only processes loose files
* No overwrites — if a filename already exists in the destination, the incoming file is automatically renamed (e.g. notes.pdf → notes (1).pdf)
* Clear feedback — prints each file as it's moved, plus a final summary count
* Beginner-readable code — every step is commented, written for someone new to Python
* No dependencies — uses only Python's standard library

## How It Works
The script prints the folder it's about to organize and asks the user to confirm with y or n.
It scans every item in the target folder using os.listdir().
Folders are skipped — only files are processed.
Each file's extension is checked against a categories dictionary to determine where it belongs; anything unmatched goes to Other.
The destination folder is created automatically if it doesn't already exist, using os.makedirs().
If a file with the same name already exists at the destination, the script renames the incoming file instead of overwriting it.
The file is moved using shutil.move(), and a confirmation line is printed for each one.
A final count of moved files is shown, and the program pauses so the output can be read before the window closes.

## For Non-Technical Users (No Python Needed)
Download the file. Click on simple_organizer.exe in this repository, then click the Download button.
Double-click the file to run it.
A black window will pop up — this is normal, it's just the program running.
It will show you the folder it's about to organize and ask:

   Continue? (y/n):
   click y and get your things done
   
## A Few Things to Know
The program only organizes your Downloads folder — it won't touch anything else on your computer.
It never overwrites a file. If two files have the same name, the new one is renamed automatically (e.g. notes (1).pdf).
If Windows shows a blue "Windows protected your PC" warning the first time you open it, click More info, then Run anyway. This happens because the app isn't registered with Microsoft — it's safe, since you can see the full source code in this repository.
No installation needed — just double-click and go.

## Getting started
Python 3.x (no external libraries needed)
Clone the repository:
   git clone https://github.com/GlitchWH/smart-file-organizer.git
Navigate into the project folder:
   cd smart-file-organizer
Run the script:
   python simple_organizer.py

## demonstration
<img width="472" height="252" alt="image" src="https://github.com/user-attachments/assets/97dc06e3-e46f-4d11-bc6b-7f14482a9f18" />
<img width="725" height="296" alt="image" src="https://github.com/user-attachments/assets/1535a11a-2466-4da0-8f2a-ab4811c24a29" />

## Future Improvements
Add an undo feature using a log of moved files
Add a dry-run mode to preview changes without moving anything
Support command-line arguments for choosing the target folder
Sort files into date-based subfolders (e.g. Images/2026-10)
Add a .gitignore to exclude dist/, build/, and .spec files from the repo

## License

This project is licensed under the MIT License — see the LICENSE file for details.

## Author

Waqas Hussain
Feel free to connect or check out more of my projects on GitHub.
