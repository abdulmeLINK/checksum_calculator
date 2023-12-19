def calculate_checksum_xor(file_path, n_bits):
    with open(file_path, 'rb') as file:
        data = file.read()
        checksum = 0
        for byte in data:
            checksum ^= byte
        checksum &= (1 << n_bits) - 1
        return checksum

def calculate_checksum_mod(file_path, n_bits):
    with open(file_path, 'rb') as file:
        data = file.read()
        checksum = sum(data) % (1 << n_bits)
        return checksum

def calculate_checksum_mod_scaled(file_path, n_bits):
    with open(file_path, 'rb') as file:
        data = file.read()
        max_value = (1 << n_bits) - 1
        checksum = ((sum(data) % max_value) + max_value) % max_value
        return checksum
