from checksum_algorithms import calculate_checksum_xor, calculate_checksum_mod, calculate_checksum_mod_scaled

def verify_checksum(file_path, checksum, algorithm, n_bits, output_format, file_import):
    if file_import:
        with open(checksum, 'r') as file:
            checksum = file.read().strip()
            n_bits = len(checksum)

    if algorithm == 'xor':
        calculated_checksum = calculate_checksum_xor(file_path, n_bits)
    elif algorithm == 'mod':
        calculated_checksum = calculate_checksum_mod(file_path, n_bits)
    elif algorithm == 'mod_scaled':
        calculated_checksum = calculate_checksum_mod_scaled(file_path, n_bits)
    else:
        print(f'Invalid algorithm: {algorithm}')
        return

    if output_format == 'binary':
        calculated_checksum = bin(calculated_checksum)[2:].zfill(n_bits)

    if str(calculated_checksum) == checksum:
        print('Checksum verification successful.')
        return True
    
    print('Checksum verification failed.')
    return False
