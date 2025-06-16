from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep

# 1. Texto colorido y estilos
print("[bold magenta]Bienvenido a la demo de Rich![/bold magenta]")

# 2. Tabla de ejemplo

# crea la tabla por consola
console = Console()
tabla = Table(title="Tabla de Inventario")

# crea los espacios de las columnas
tabla.add_column("Producto", justify="left", style="cyan")
tabla.add_column("Cantidad", justify="center", style="green")
tabla.add_column("Precio", justify="right", style="yellow")

# crea las filas de la tabla
tabla.add_row("Tomate", "25", "$1.00")
tabla.add_row("Lechuga", "10", "$0.80")
tabla.add_row("Zanahoria", "18", "$0.50")

# muestra el resultado 
console.print(tabla)
print()

# 3 simula una barra de progreso
print("[bold blue]Simulando carga con barra de progreso:[/bold blue]")
for paso in track(range(10), description="Cargando..."):
    sleep(0.3)

# Texto colorido y estilos
print("\n[bold green]listo[/bold green]")

# la (/n) es para el salto de linea


