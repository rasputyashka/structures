### This repo is nothing more than playground, therefore there may be bugs. You can report them at issues page.

#### in order to install and use it (idk why would you need it, everything you need is in bultin, queue and collections module) run these commmands:
windows:
```cmd
py -m venv .venv
call .venv\Scripts\activate
pip install -e .[test]
```
unix-like systems:
```sh
path/to/python -m venv .venv
. .venv/bin/activate
pip install -e .[test]
```

Now you can test it by running `pytest` command.
