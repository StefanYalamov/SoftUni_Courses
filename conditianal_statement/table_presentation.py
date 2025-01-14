from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Top programming languages")

table.add_column("Rank", style="cyan", justify="right")
table.add_column("Language", style="magenta")
table.add_column("Rank", style="green", justify="right")

table.add_row("1", "Python", "10%")
table.add_row("2", "JAVA", "5%")
table.add_row("3", "C#", "3%")

console.print(table)
