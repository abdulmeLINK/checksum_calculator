import argparse
import os
from checksum_algorithms import calculate_checksum_xor, calculate_checksum_mod, calculate_checksum_mod_scaled
from checksum_verification import verify_checksum

def validate_args(args):
    if not os.path.isfile(args.file_path):
        return 'Invalid file path.'
    if args.n_bits <= 0:
        return 'Invalid checksum length. Please enter a positive integer.'
    if args.algorithm not in ['xor', 'mod', 'mod_scaled']:
        return f'Invalid algorithm: {args.algorithm}'
    return None

def calculate_checksum(file_path, algorithm, n_bits):
    if algorithm == 'xor':
        return calculate_checksum_xor(file_path, n_bits)
    elif algorithm == 'mod':
        return calculate_checksum_mod(file_path, n_bits)
    elif algorithm == 'mod_scaled':
        return calculate_checksum_mod_scaled(file_path, n_bits)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path to the file')
    parser.add_argument('-a', '--algorithm',choices=['xor', 'mod', 'mod_scaled'], default="mod", help='Checksum algorithm')
    parser.add_argument('n_bits', type=int, nargs='?', default=16, help='Desired checksum length (in bits for xor and mod algorithms)')
    parser.add_argument('-v', '--verify', type=str, help='Checksum to verify against or path to the checksum file for verification')
    parser.add_argument('-f', '--file', action='store_true', help='Use -v as the file import method')
    parser.add_argument('-o', '--output',choices=['binary', 'string'], default="binary", help='Output format')
    parser.add_argument('-e', '--export', type=str, help='Path to export the calculated checksum')
    args = parser.parse_args()

    error_message = validate_args(args)
    if error_message:
        print(error_message)
        return

    checksum = calculate_checksum(args.file_path, args.algorithm, args.n_bits)
    if args.output == 'binary':
        checksum = bin(checksum)[2:].zfill(args.n_bits)

    if args.verify is not None:
        verify_checksum(args.file_path, args.verify, args.algorithm, args.n_bits, args.output, args.file)
    else:
        print(f'Checksum: {checksum}')

        if args.export is not None:
            with open(args.export, 'w') as file:
                file.write(str(checksum))

if __name__ == '__main__':
    main()
