# Dek-D's Writer Font Injector

A simple python script that autometrically replace ```face``` attribute in ```font``` to the new one.

Made for personal use in [Dek-D's Writer](https://www.dek-d.com/home/writer/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Dek-D's Writer Font Injector.

First, download this repository. After you unizip, open console in the folder and issue this command.

```bash
pip install .
```

## Usage

Copy HTML code of your chapter from Dek-D's Writer and paste it into a file. **You must not format it.** Then, issue the command

```bash
ddfi -i [input] -o [output] -c [old_font] -t [new_font]
```

Please note that if the name contains space, it must be inside " (quotation mark).

Example :

```bash
ddfi -i chapter-2.html -o chapter-2-new.html -c "Cordia New" -o Prompt
```

## Author

**pannxe** - *original work*

## Lisence

GNU GENERAL PUBLIC LICENSE
