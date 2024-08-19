#!/usr/bin/env python3
import subprocess
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + "Success: Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: Command failed with error: {e}")

def main():
    choice = input(Fore.GREEN + "Enter 'e' to embed or 'x' to extract: ").strip().lower()

    if choice == 'e':
        # Embed data
        cover_file = input(Fore.YELLOW + "Enter the cover image file name: ")
        data_file = input(Fore.YELLOW + "Enter the data file name to hide: ")
        command = f'steghide embed -ef {data_file} -cf {cover_file}'
        run_command(command)

    elif choice == 'x':
        # Extract data
        stego_file = input(Fore.YELLOW + "Enter the image file name: ")
        command = f'steghide extract -sf {stego_file}'
        run_command(command)

    else:
        print(Fore.RED + "Invalid choice. Please run the script again and choose either 'e' or 'x'.")

if __name__ == "__main__":
    main()
