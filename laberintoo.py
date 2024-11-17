## Hacer laberinto en Archivo .txt

def laberinto(filename="laberinto.txt"):
    maze = [
        "█████████████████████████",
        "█A     █         █     █",
        "█ ████ █ ███████ █ ███ █",
        "█ █    █     █   █   █ █",
        "█ █ ████████ █ █████ █ █",
        "█ █ █      █ █       █ █",
        "█ █ █ ███████████ ██████",
        "█   █   █       █      █",
        "██████ █████ █████ ███ █",
        "█      █     █     █   █",
        "█ ████████████████ ███ █",
        "█ █                █   █",
        "█ █ █████ ███████████ █",
        "█ █   █   █          █ █",
        "█ █████ █████ ██████ █ █",
        "█       █      █     █ █",
        "█████ ██████████ ███ █ █",
        "█     █          █   █ █",
        "█ █████ █████████████ █B",
        "████████████████████████",
    ]
    
    # Save the maze to the file using utf-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(maze))
    print(f"Maze saved to {filename}")

# Create and save the maze
laberinto()
