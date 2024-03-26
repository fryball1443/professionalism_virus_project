def consume_memory(): 
  for i in range(9999):
    try:
        large_list = [0] * int(1e8)  # Create a list with 100 million elements
        consume_memory()  # Call the function recursively
    except MemoryError:
        print("break")
        break

if __name__ == "__main__":
    consume_memory()