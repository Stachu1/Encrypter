import os, random as rnd
from sys import argv
from colorama import Fore, init
init()



def encrypt_file(input_file, output_file, table):
    with open(input_file, 'rb') as f:
        content = bytearray(f.read())

    encrypted_content = [table[byte] for byte in content]

    with open(output_file, 'wb') as f:
        f.write(bytearray(encrypted_content))


def decrypt_file(input_file, output_file, table):
    with open(input_file, 'rb') as f:
        encrypted_content = bytearray(f.read())

    reverse_table = {v: k for k, v in table.items()}
    decrypted_content = [reverse_table[byte] for byte in encrypted_content]

    with open(output_file, 'wb') as f:
        f.write(bytearray(decrypted_content))


def generate_table(seed):
    original_bytes = list(range(256))
    shuffled_bytes = original_bytes.copy()
    
    rnd.seed(seed)
    rnd.shuffle(shuffled_bytes)
    table = dict(zip(original_bytes, shuffled_bytes))
    return table


if __name__ == "__main__":
    if len(argv) < 4:
        print(f"{Fore.RED}ERROR: Not enough arguments!{Fore.RESET}\n")
        print(f"Usage: \n    python {argv[0]} <filename> <encrypt/decrypt> <seed>\n")
        
    else:
        file_name = argv[1]
        mode = argv[2]
        seed = int(argv[3])
        
        
        table = generate_table(seed)
        
        if mode == "encrypt" or mode == "enc":
            encrypt_file(file_name, f"{file_name}.encrypted", table)
            print(f"{Fore.GREEN}DONE!{Fore.RESET}")
            
        elif mode == "decrypt" or mode == "dec":
            decrypt_file(file_name, f"{file_name.split('.encrypted')[0]}", table)
            print(f"{Fore.GREEN}DONE!{Fore.RESET}")
            
        else:
            print(f"{Fore.RED}ERROR: invalid mode!{Fore.RESET}\n")
            print(f"Usage: \n    python {argv[0]} <filename> <encrypt/decrypt> <seed>\n")