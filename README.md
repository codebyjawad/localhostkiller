# LocalhostKiller 🔥

Kill localhost processes with style. A beautiful CLI tool for developers.

![Demo](demo.gif)

## Features

- 🎯 See all localhost ports in use
- ⚡ Kill processes instantly
- 🎨 Beautiful terminal UI
- 🔄 Interactive mode
- 🚀 Fast and lightweight
- 💻 Cross-platform (Mac, Linux, Windows)

## Installation

```bash
pip install localhostkiller
```

## Usage

**Interactive mode:**
```bash
lhk
```

**Kill by port:**
```bash
lhk 3000
```

**List all ports:**
```bash
lhk --list
```

## Why LocalhostKiller?

Ever had port conflicts? Forgotten what's running on port 3000? Tired of `lsof -ti:3000 | xargs kill -9`?

LocalhostKiller makes it simple.

## Development

```bash
git clone https://github.com/jawad/localhostkiller
cd localhostkiller
pip install -e .
```

## License

MIT © Jawad

## Links

- Website: https://makeworking.com
- Twitter: @jawad
- GitHub: @jawad
