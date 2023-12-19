# Checksum Calculator

This repository contains a Python script for calculating and verifying checksums of files. It supports three checksum algorithms: XOR, MOD, and scaled MOD.

## Installation

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/checksum_calculator.git
    ```
2. Navigate to the project directory.
    ```bash
    cd checksum_calculator
    ```
3. Install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the script from the command line with the following syntax:

```bash
python main.py <file_path> <n_bits> -a <algorithm> -v <checksum> -f -o <output_format> -e <export_path>
```

Here's what each argument does:

- `file_path`: Path to the file you want to calculate the checksum for.
- `n_bits`: Desired checksum length (in bits for XOR and MOD algorithms).
- `-a` or `--algorithm`: Checksum algorithm to use. Choices are 'xor', 'mod', and 'mod_scaled'. Default is 'mod'.
- `-v` or `--verify`: Checksum to verify against or path to the checksum file for verification.
- `-f` or `--file`: Use `-v` as the file import method.
- `-o` or `--output`: Output format. Choices are 'binary', 'hex', and 'string'. Default is 'binary'.
- `-e` or `--export`: Path to export the calculated checksum.

## Contributing

We welcome contributions to this project. Please feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
