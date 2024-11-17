def create_beautiful_maze(filename="laberinto.txt"):
    """
    Creates a beautiful maze and saves it to a file.
    The maze includes a start point (A), a goal point (B),
    walls (█), and paths ( ).
    """
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
create_beautiful_maze()
