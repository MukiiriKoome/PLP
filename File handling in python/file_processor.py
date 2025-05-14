def process_file(input_path, output_path):
    """
    Reads a file, modifies its content (e.g., uppercase), and writes to a new file.
    Handles file errors gracefully.
    """
    try:
        # Read input file
        with open(input_path, 'r') as file:
            content = file.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write to output file
        with open(output_path, 'w') as file:
            file.write(modified_content)
        print(f"Success! Modified file saved to {output_path}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to read/write files.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    # Get user input
    input_file = input("Enter the input filename (e.g., input.txt): ").strip()
    output_file = input("Enter the output filename (e.g., output.txt): ").strip()
    
    # Process file
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
