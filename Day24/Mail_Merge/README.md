# Mail Merge (Day 24)

> **AI generated.** This README was written by AI (Claude) to show how the folders and paths in this project fit together.

Reads a list of names, puts each name into a letter template, and saves one letter per person.

## Folder structure

```
Mail_Merge/                              ← run main.py from this folder
├── main.py
├── Input/
│   ├── Names/
│   │   └── invited_names.txt            ← .\Input\Names\invited_names.txt
│   └── Letters/
│       └── starting_letter.txt          ← .\Input\Letters\starting_letter.txt
└── Output/
    └── ReadyToSend/                     ← .\Output\ReadyToSend\letter_for_<name>.txt
        ├── example.txt
        ├── letter_for_Aang.txt
        ├── letter_for_Appa.txt
        └── letter_for_Katara.txt
```

## Click to open each file

- [main.py](main.py): the program
- Input
    - [Names/invited_names.txt](Input/Names/invited_names.txt): one name per line
    - [Letters/starting_letter.txt](Input/Letters/starting_letter.txt): the template, with `[name]` where each name goes
- Output
    - [ReadyToSend/example.txt](Output/ReadyToSend/example.txt): what a finished letter should look like
    - [ReadyToSend/letter_for_Aang.txt](Output/ReadyToSend/letter_for_Aang.txt)
    - [ReadyToSend/letter_for_Appa.txt](Output/ReadyToSend/letter_for_Appa.txt)
    - [ReadyToSend/letter_for_Katara.txt](Output/ReadyToSend/letter_for_Katara.txt)

Running `main.py` makes a letter for all 8 names in the list. Only 3 of the finished letters are saved here.

## How the paths work

`.\` means **the folder you run the program from**. So `.\Input\Names\invited_names.txt` means: from `Mail_Merge`, go into `Input`, then `Names`.

Run it from inside this folder, or Python won't find the files and you'll get `FileNotFoundError`.
