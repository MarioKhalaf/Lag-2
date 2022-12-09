# Dungeon Run - Projektmetodik och agila metoder

## Roller

**Product Owner:** Robert Westin

**Scrum Master:** Timmy Elf

**Utvecklare:** Nina, Isabel, Mario, David, Daniel

## Verktyg

Bestämda program/plugin: Mermaid:

<https://mermaid-js.github.io/docs/mermaid-live-editor-beta/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbkFbQ2hyaXN0bWFzXSAtLT58R2V0IG1vbmV5fCBCKEdvIHNob3BwaW5nKVxuQiAtLT4gQ3tMZXQgbWUgdGhpbmt9XG5DIC0tPnxPbmV8IERbTGFwdG9wXVxuQyAtLT58VHdvfCBFW2lQaG9uZV1cbkMgLS0-fFRocmVlfCBGW2ZhOmZhLWNhciBDYXJdXG4gICIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9>

## Referenser

Robert Westins dokument:
https://studentportal.nackademin.se/course/view.php?id=4169

Trello:
https://trello.com/b/1Z7Z7Z7Z/dungeon-run

Github:
https://github.com/MarioKhalaf/Lag-2

Daily Standup:
https://nackademinyh-my.sharepoint.com/:x:/r/personal/timmy_elf_yh_nackademin_se/_layouts/15/Doc.aspx?sourcedoc=%7B9349B970-D5A1-41BC-B273-8FC0884CD10D%7D&file=Dungeon%20Run.xlsx&action=default&mobileredirect=true

## VScode extensions

Name: Mermaid Markdown Syntax Highlighting
Id: bpruitt-goddard.mermaid-markdown-syntax-highlighting
Description: Markdown syntax support for the Mermaid charting language
Version: 1.5.0
Publisher: Brian Pruitt-Goddard
VS Marketplace Link: <https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting>

Name: Markdown Preview Mermaid Support
Id: bierner.markdown-mermaid
Description: Adds Mermaid diagram and flowchart support to VS Code's builtin markdown preview
Version: 1.16.0
Publisher: Matt Bierner
VS Marketplace Link: <https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid>

## Installationsinstruktioner
1. Create a virtual environment
2. Install requirements

## Virtual environment (venv)

see <https://docs.python.org/3/library/venv.html>

Linux / OSX

```sh
python -m venv .venv  # could also be python3
source .venv/bin/activate
```

Windows - cmd.exe

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell

```PowerShell
# On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### Install requirements.txt

```bat
pip install -r requirements.txt
```

