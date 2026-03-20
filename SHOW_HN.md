# Show HN: LocalhostKiller – See and kill what's running on localhost

I built LocalhostKiller because I was tired of "port 3000 is already in use" errors and having to remember `lsof -ti:3000 | xargs kill -9`.

**What it does:**
- Shows all processes running on localhost ports
- Kill by port: `lhk 3000`
- Interactive mode with menu selection
- Beautiful terminal UI

**Why I built it:**
Every developer has this problem. You start a dev server, forget to stop it, start another project, and boom - port conflict. Or you have 5 terminals open and can't remember which one has the server running.

LocalhostKiller solves this in one command.

**Tech:**
- Python 3.8+
- Rich (for the beautiful TUI)
- psutil (for process management)
- Cross-platform (Mac, Linux, Windows)

**Install:**
```bash
pip install localhostkiller
```

**Usage:**
```bash
lhk              # Interactive mode
lhk 3000         # Kill port 3000
lhk --list       # List all ports
```

GitHub: https://github.com/jawad/localhostkiller

Would love feedback! What features would make this more useful for you?
