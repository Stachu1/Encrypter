import os, random as rnd, time
from sys import argv
from colorama import Fore, init
init()



def encrypt_file(input_file, output_file, table, chunk_size=int(1e6)) -> None:
    file_size = os.stat(input_file).st_size
    if file_size > 5e9:
        chunk_size = 50e6
    elif file_size < 1e6:
        chunk_size = int(1e6)
    else:
        chunk_size = int(file_size/100)
        
    chunks_count = int(file_size / chunk_size)
    with open(input_file, 'rb') as in_f:
        with open(output_file, 'wb') as out_f:
            time_start = time.time()
            chunk_index = 0
            content = bytearray(in_f.read(chunk_size))
            
            while content:
                print_progress_bar(chunk_index, chunks_count, time_start)
                encrypted_content = [table[byte] for byte in content]
                out_f.write(bytearray(encrypted_content))
                chunk_index += 1
                
                content = bytearray(in_f.read(chunk_size))


def print_progress_bar(progress, total, time_start, size=100) -> None:
    percent = 1 if progress >= total else progress / total
    bar = "█" * int(percent * size) + "-" * (100 - int(percent * size))
    time_total = time.time() - time_start
    if time_total >= 60:
        time_total = f"{int(time_total // 60)}m {(time_total % 60):.2f}s"
    else:
        time_total = f"{time_total:.2f}s"

    if percent == 0:
        time_left = "--"
    else:
        time_left = (time.time() - time_start) / percent - (time.time() - time_start)
        if time_left >= 60:
            time_left = f"{int(time_left // 60)}m {(time_left % 60):.2f}s"
        else:
            time_left = f"{time_left:.2f}s"
    print(f"{bar} {percent*100:.2f}%   t: {time_total}   eta: " + time_left, end="     \r")
    if progress == total: 
        print(f"{Fore.GREEN}{bar} {percent*100:.2f}%   t: {time_total}   eta: --      {Fore.RESET}", end="\n")


def generate_table(seed) -> dict:
    original_bytes = list(range(256))
    shuffled_bytes = original_bytes.copy()
    
    rnd.seed(seed)
    rnd.shuffle(shuffled_bytes)
    table = dict(zip(original_bytes, shuffled_bytes))
    return table


if __name__ == "__main__":
    if len(argv) < 4:
        print(f"{Fore.RED}ERROR: Not enough arguments!{Fore.RESET}\n")
        print(f"Usage: \n    python {argv[0]} <filename> <encrypt/decrypt> <key>\n")
        
    else:
        file_name = argv[1]
        mode = argv[2]
        seed = int(argv[3])
        
        
        table = generate_table(seed)
        reverse_table = {v: k for k, v in table.items()}
        
        if mode == "encrypt" or mode == "enc":
            print(f"\n{Fore.YELLOW}Encrypting:{Fore.RESET}")
            encrypt_file(file_name, f"{file_name}.encrypted", table)
            print(f"\n{Fore.GREEN}DONE!{Fore.RESET}")
            
        elif mode == "decrypt" or mode == "dec":
            print(f"\n{Fore.MAGENTA}Decrypting:{Fore.RESET}")
            encrypt_file(file_name, f"[DECRYPTED]{file_name.split('.encrypted')[0]}", reverse_table)
            print(f"\n{Fore.GREEN}DONE!{Fore.RESET}")
            
        else:
            print(f"{Fore.RED}ERROR: invalid mode!{Fore.RESET}\n")
            print(f"Usage: \n    python {argv[0]} <filename> <encrypt/decrypt> <key>\n")