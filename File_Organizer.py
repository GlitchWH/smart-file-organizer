#                     IMPORTANT:
# Prints the folder it's about to organize (your Downloads folder by default)

# Asks "Continue? (y/n)" and stops immediately if the answer isn't y — nothing 
# gets moved without confirmation

# Goes through every item in the folder, one at a time
# Skips anything that's a folder, not a file, so subfolders are left alone
# Checks each file's extension (like .jpg or .pdf) against the categories list
# Sorts it into Images, Documents, Videos, Music, Archives, or Other if nothing matches
# Creates the destination folder if it doesn't exist yet

# Checks for a naming clash — if a file with the same name is already there, 
# it renames the incoming one instead of overwriting it, e.g. notes.pdf → notes (1).pdf

# Moves the file and prints a line like Moved holiday.jpg -> Images
# Prints a final count, e.g. Done! 5 file(s) moved.

# Pauses at the end with "Press Enter to close..." so the window stays
#  open and the student can actually read what happened, instead of it vanishing instantly




import os
import shutil

# 1. Which folder to clean up? (Change this if you want another folder)
folder = os.path.join(os.path.expanduser("~"), "Downloads")

# 2. Which file types go into which folder?
categories = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos":    [".mp4", ".mkv", ".avi"],
    "Music":     [".mp3", ".wav"],
    "Archives":  [".zip", ".rar", ".7z"],
}

print(f"This will organize files in:\n  {folder}\n")
answer = input("Continue? (y/n): ").strip().lower()

if answer != "y":
    print("Cancelled. No files were moved.")
else:
    moved_count = 0

    # 3. Look at every item in the folder
    for name in os.listdir(folder):
        old_path = os.path.join(folder, name)

        # Skip folders, we only want files
        if not os.path.isfile(old_path):
            continue

        # Get the extension, e.g. "photo.JPG" -> ".jpg"
        extension = os.path.splitext(name)[1].lower()

        # Find the matching category (default is "Other")
        target_folder = "Other"
        for category, extensions in categories.items():
            if extension in extensions:
                target_folder = category

        # Make the folder if it doesn't exist yet
        new_folder = os.path.join(folder, target_folder)
        os.makedirs(new_folder, exist_ok=True)

        # Avoid overwriting a file with the same name
        new_path = os.path.join(new_folder, name)
        if os.path.exists(new_path):
            base, ext = os.path.splitext(name)
            counter = 1
            while os.path.exists(new_path):
                new_path = os.path.join(new_folder, f"{base} ({counter}){ext}")
                counter += 1

        # Move the file
        shutil.move(old_path, new_path)
        print(f"Moved {name} -> {target_folder}")
        moved_count += 1

    print(f"\nDone! {moved_count} file(s) moved.")

# Keep the window open so the student can read the output
input("\nPress Enter to close...")