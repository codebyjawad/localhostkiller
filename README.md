# LocalhostKiller 🔥

**Kill localhost processes with style.**

A beautiful CLI tool that shows what's running on your localhost ports and lets you kill processes instantly.

[![PyPI](https://img.shields.io/badge/pypi-v0.1.0-blue)](https://pypi.org/project/localhostkiller/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Why LocalhostKiller?

Ever had these problems?
- "Port 3000 is already in use" 😤
- Forgot what's running on localhost
- Tired of `lsof -ti:3000 | xargs kill -9`
- Need to see all your dev servers at once

**LocalhostKiller solves this.**

## Features

- 🎯 See all localhost ports instantly
- ⚡ Kill processes with one command
- 🎨 Beautiful terminal UI
- 🔄 Interactive mode with menu
- 💀 Kill all option
- 🚀 Fast and lightweight
- 💻 Cross-platform (Mac, Linux, Windows)

## Installation

```bash
pip install localhostkiller
```

Or install from source:
```bash
git clone https://github.com/jawad/localhostkiller
cd localhostkiller
pip install -e .
```

## Usage

### Interactive Mode
```bash
lhk
```
Select processes from a menu and kill them interactively.

### Kill by Port
```bash
lhk 3000
```
Instantly kill whatever is running on port 3000.

### List All Ports
```bash
lhk --list
```
See everything running on localhost.

### Help
```bash
lhk --help
```

## Examples

**Kill a specific port:**
```bash
$ lhk 8080
Checking port 8080...
Kill node on port 8080? [Y/n]: y
✓ Killed node (PID: 12345)
```

**Interactive mode:**
```bash
$ lhk

🔥 LocalhostKiller
┏━━━━┳━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ #  ┃ Port ┃ PID  ┃ Process ┃ Command          ┃
┡━━━━╇━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ 1  │ 3000 │ 1234 │ node    │ node server.js   │
│ 2  │ 8080 │ 5678 │ python3 │ python3 app.py   │
└────┴──────┴──────┴─────────┴──────────────────┘

Commands: [number] to kill | 'r' refresh | 'a' kill all | 'q' quit

→ 1
Kill node on port 3000? [Y/n]: y
✓ Killed node (PID: 1234)
```

## Pro Version (Coming Soon)

- 💾 Saved port configurations
- 🐳 Docker container support
- 👥 Team sharing
- 📊 Port usage analytics

**Price:** $19 one-time payment

## Development

```bash
git clone https://github.com/codebyjawad/localhostkiller
cd localhostkiller
pip install -e .
python3 lhk.py --list
```

## Tech Stack

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal UI
- [psutil](https://github.com/giampaolo/psutil) - Process management

## Contributing

PRs welcome! Please open an issue first to discuss changes.

## License

MIT © [Jawad](https://codebyjawad.com)

## Links

- 🌐 Website: [makeworking.com](https://makeworking.com)
- 🐙 GitHub: [github.com/jawad/localhostkiller](https://github.com/jawad/localhostkiller)
- 🐦 Twitter: [@jawad](https://twitter.com/jawad)
- 📦 PyPI: [pypi.org/project/localhostkiller](https://pypi.org/project/localhostkiller)

---

**Made with ❤️ by developers, for developers.**
 developers, for developers.**
iller)

---

**Made with ❤️ by developers, for developers.**
