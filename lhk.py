#!/usr/bin/env python3
"""LocalhostKiller - Kill localhost processes with style."""

import psutil
import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

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
                    'cmdline': ' '.join(proc.cmdline()[:3])  # First 3 args
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
        table.add_row(
            str(idx),
            str(proc['port']),
            str(proc['pid']),
            proc['name'],
            proc['cmdline'][:50] + "..." if len(proc['cmdline']) > 50 else proc['cmdline']
        )
    
    console.print(table)

def kill_process(pid):
    """Kill a process by PID."""
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        console.print(f"[green]✓ Killed process {pid} ({proc.name()})[/green]")
        return True
    except psutil.NoSuchProcess:
        console.print(f"[red]✗ Process {pid} not found[/red]")
        return False
    except psutil.AccessDenied:
        console.print(f"[red]✗ Access denied. Try with sudo?[/red]")
        return False
    except Exception as e:
        console.print(f"[red]✗ Failed: {e}[/red]")
        return False

def kill_by_port(port):
    """Kill process using a specific port."""
    processes = get_localhost_processes()
    for proc in processes:
        if proc['port'] == port:
            return kill_process(proc['pid'])
    console.print(f"[yellow]No process found on port {port}[/yellow]")
    return False

def interactive_mode():
    """Interactive mode to select and kill processes."""
    while True:
        console.clear()
        console.print("[bold cyan]LocalhostKiller[/bold cyan] - Interactive Mode\n")
        
        processes = get_localhost_processes()
        
        if not processes:
            console.print("[yellow]No localhost processes found.[/yellow]")
            return
        
        display_processes(processes)
        console.print("\n[dim]Commands: [number] to kill, 'r' to refresh, 'q' to quit[/dim]")
        
        choice = Prompt.ask("\nSelect", default="q")
        
        if choice.lower() == 'q':
            break
        elif choice.lower() == 'r':
            continue
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(processes):
                kill_process(processes[idx]['pid'])
                input("\nPress Enter to continue...")
            else:
                console.print("[red]Invalid selection[/red]")
                input("\nPress Enter to continue...")

def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    # No args = interactive mode
    if not args:
        interactive_mode()
        return
    
    # Single number = kill by port
    if len(args) == 1 and args[0].isdigit():
        port = int(args[0])
        console.print(f"[cyan]Killing process on port {port}...[/cyan]\n")
        kill_by_port(port)
        return
    
    # --list flag
    if '--list' in args or '-l' in args:
        console.print("[bold cyan]LocalhostKiller[/bold cyan] - Listing processes...\n")
        processes = get_localhost_processes()
        if processes:
            display_processes(processes)
        else:
            console.print("[yellow]No localhost processes found.[/yellow]")
        return
    
    # Help
    console.print("""
[bold cyan]LocalhostKiller[/bold cyan] - Kill localhost processes with style

Usage:
  lhk              Interactive mode
  lhk 3000         Kill process on port 3000
  lhk --list       List all localhost processes
  lhk --help       Show this help
    """)

if __name__ == "__main__":
    main()
