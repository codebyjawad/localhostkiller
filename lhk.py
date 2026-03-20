#!/usr/bin/env python3
"""LocalhostKiller - Kill localhost processes with style."""

import psutil
import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()
VERSION = "0.1.0"

def get_localhost_processes():
    """Get all processes using localhost ports."""
    processes = []
    seen_ports = set()
    
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.ip in ('127.0.0.1', '::1', 'localhost') and conn.laddr.port not in seen_ports:
            try:
                proc = psutil.Process(conn.pid)
                processes.append({
                    'port': conn.laddr.port,
                    'pid': conn.pid,
                    'name': proc.name(),
                    'status': conn.status,
                    'cmdline': ' '.join(proc.cmdline()[:3])
                })
                seen_ports.add(conn.laddr.port)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    
    return sorted(processes, key=lambda x: x['port'])

def display_processes(processes):
    """Display processes in a beautiful table."""
    table = Table(title="🔥 LocalhostKiller", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Port", style="cyan", width=8)
    table.add_column("PID", style="yellow", width=8)
    table.add_column("Process", style="green")
    table.add_column("Command", style="dim", no_wrap=False)
    
    for idx, proc in enumerate(processes, 1):
        cmd = proc['cmdline'][:50] + "..." if len(proc['cmdline']) > 50 else proc['cmdline']
        table.add_row(
            str(idx),
            str(proc['port']),
            str(proc['pid']),
            proc['name'],
            cmd
        )
    
    console.print(table)

def kill_process(pid, name=""):
    """Kill a process by PID."""
    try:
        proc = psutil.Process(pid)
        proc_name = name or proc.name()
        proc.terminate()
        console.print(f"[green]✓ Killed {proc_name} (PID: {pid})[/green]")
        return True
    except psutil.NoSuchProcess:
        console.print(f"[red]✗ Process {pid} not found[/red]")
        return False
    except psutil.AccessDenied:
        console.print(f"[red]✗ Access denied. Try: sudo lhk {pid}[/red]")
        return False
    except Exception as e:
        console.print(f"[red]✗ Failed: {e}[/red]")
        return False

def kill_by_port(port):
    """Kill process using a specific port."""
    processes = get_localhost_processes()
    for proc in processes:
        if proc['port'] == port:
            if Confirm.ask(f"Kill {proc['name']} on port {port}?", default=True):
                return kill_process(proc['pid'], proc['name'])
            return False
    console.print(f"[yellow]No process found on port {port}[/yellow]")
    return False

def interactive_mode():
    """Interactive mode to select and kill processes."""
    while True:
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]LocalhostKiller[/bold cyan] v" + VERSION,
            subtitle="Interactive Mode"
        ))
        console.print()
        
        processes = get_localhost_processes()
        
        if not processes:
            console.print("[yellow]No localhost processes found.[/yellow]")
            console.print("\n[dim]Press Enter to exit...[/dim]")
            input()
            return
        
        display_processes(processes)
        console.print("\n[dim]Commands: [number] to kill | 'r' refresh | 'a' kill all | 'q' quit[/dim]")
        
        choice = Prompt.ask("\n→", default="q")
        
        if choice.lower() == 'q':
            break
        elif choice.lower() == 'r':
            continue
        elif choice.lower() == 'a':
            if Confirm.ask(f"Kill all {len(processes)} processes?", default=False):
                killed = 0
                for proc in processes:
                    if kill_process(proc['pid'], proc['name']):
                        killed += 1
                console.print(f"\n[green]Killed {killed}/{len(processes)} processes[/green]")
                input("\nPress Enter to continue...")
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(processes):
                proc = processes[idx]
                if Confirm.ask(f"Kill {proc['name']} on port {proc['port']}?", default=True):
                    kill_process(proc['pid'], proc['name'])
                input("\nPress Enter to continue...")
            else:
                console.print("[red]Invalid selection[/red]")
                input("\nPress Enter to continue...")

def show_help():
    """Show help message."""
    console.print(Panel.fit("""
[bold cyan]LocalhostKiller[/bold cyan] v""" + VERSION + """ - Kill localhost processes with style

[bold]Usage:[/bold]
  lhk              Interactive mode
  lhk 3000         Kill process on port 3000
  lhk --list       List all localhost processes
  lhk --version    Show version
  lhk --help       Show this help

[bold]Examples:[/bold]
  lhk              # Start interactive mode
  lhk 8080         # Kill whatever is on port 8080
  lhk --list       # Just show what's running

[bold]Links:[/bold]
  GitHub: github.com/jawad/localhostkiller
  Website: makeworking.com
    """, title="Help"))

def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    # Version
    if '--version' in args or '-v' in args:
        console.print(f"[cyan]LocalhostKiller[/cyan] v{VERSION}")
        return
    
    # Help
    if '--help' in args or '-h' in args:
        show_help()
        return
    
    # No args = interactive mode
    if not args:
        interactive_mode()
        return
    
    # Single number = kill by port
    if len(args) == 1 and args[0].isdigit():
        port = int(args[0])
        console.print(f"[cyan]Checking port {port}...[/cyan]\n")
        kill_by_port(port)
        return
    
    # --list flag
    if '--list' in args or '-l' in args:
        console.print(Panel.fit("[bold cyan]LocalhostKiller[/bold cyan] v" + VERSION))
        console.print()
        processes = get_localhost_processes()
        if processes:
            display_processes(processes)
            console.print(f"\n[dim]Found {len(processes)} localhost processes[/dim]")
        else:
            console.print("[yellow]No localhost processes found.[/yellow]")
        return
    
    # Unknown command
    console.print("[red]Unknown command. Use --help for usage.[/red]")

if __name__ == "__main__":
    main()
