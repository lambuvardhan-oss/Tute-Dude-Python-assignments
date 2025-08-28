#Task1 Read a file and handle errors
def read_file_alternative(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.read()
            print(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not found.")

read_file_alternative('sample.txt')


#Task2 Write and append to a data file.
def write_and_append_file():
    # Step 1: Take user input and write to the file
    user_text = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_text + '\n')
    print("Data successfully written to output.txt.\n")
    
    # Step 2: Take additional input and append to the file
    additional_text = input("Enter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write(additional_text + '\n')
    print("Data successfully appended.\n")
    
    # Step 3: Read and display the final content of the file
    print("Final content of output.txt:")
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content, end='')
