# File Organizer

A command-line tool that automatically sorts files in a folder into subfolders by type.

## What it does

Point it at any folder and it will move files into organized subfolders:

- `images` — jpg, jpeg, png, gif
- `pdfs` — pdf
- `code` — py, js, html, css
- `audio` — mp3, wav
- `video` — mp4, mov
- `misc` — everything else

## Requirements

- Python 3.13+
- No external libraries needed

## Usage

```
python file_organizer.py
```

You will be prompted to enter the path of the folder you want to organize.

## Adding more file types

To support additional extensions, find the relevant category in the `organize()` function and add the extension to the list. For example to add `.txt` to misc, it's already handled automatically.
