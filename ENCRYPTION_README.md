# Smart Shield Prototype - Encryption Module

## Overview
This module demonstrates AES encryption using the cryptography library for the Smart Shield prototype. It showcases how meter data can be securely encrypted and decrypted using industry-standard encryption methods.

## Features
- **Random Data Selection**: Picks a random meter reading from the CSV dataset
- **AES Encryption**: Uses Fernet (AES-128 in CBC mode) for secure encryption
- **Data Recovery**: Demonstrates successful decryption to prove data integrity
- **Beginner-Friendly Output**: Clear, formatted output suitable for demonstration

## Requirements
- Python 3.7+
- pandas >= 1.3.0
- cryptography >= 3.4.0

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the encryption demo:
```bash
python encryption_module.py
```

## How It Works

### 1. Data Loading
- Loads meter data from `meter_data_with_detection.csv`
- Uses pandas for efficient CSV processing

### 2. Random Selection
- Selects a random row from the dataset
- Formats the reading as: "House_X - Y.Y kWh at Zh"
- Example: "House_5 - 7.4 kWh at 14h"

### 3. Encryption Process
- Generates a secure encryption key using Fernet
- Encrypts the formatted text string
- Produces encrypted binary data

### 4. Decryption & Verification
- Decrypts the encrypted data using the same key
- Verifies that the original text is perfectly recovered
- Demonstrates the integrity of the encryption system

## Output Format
The module provides clear, structured output including:
- Original meter reading details
- Encryption and decryption status
- Encrypted data (in base64 format)
- Decrypted data (for verification)
- Encryption key (for reference)

## Security Features
- **AES-128 Encryption**: Industry-standard symmetric encryption
- **Secure Key Generation**: Cryptographically secure random keys
- **Data Integrity**: Verifies successful decryption
- **No Hardcoded Keys**: Generates new keys for each run

## Example Output
```
Smart Shield Prototype - Encryption Demo
==================================================
Loading meter data from CSV...
Loaded 480 meter readings successfully!

Randomly selected reading:
  Meter: House_6
  Hour: 19
  Usage: 8.7 kWh
  Status: Normal

Generating encryption key...
Encrypting the reading...
Decrypting to verify...

ENCRYPTION RESULTS:
==================================================
Original Text:     'House_6 - 8.7 kWh at 19h'
Encrypted Text:    b'gAAAAABouLhFrerJGmDcCXOS6vNVcYhiFCp69RHh7CFPKoBKrIjuLwmwen_YJoYNxrbCZm8uBmE5RN37MJIHPHqf7TPMBZ7vipfGRa-3EGakwWaLtcRoNfI='

Decrypted Text:    'House_6 - 8.7 kWh at 19h'

SUCCESS: Encryption and decryption completed successfully!
  The original data was perfectly recovered.

Encryption Key (Base64): Yi50l20Ompk3clEuIbdm1hLp75NurBsqJR2dhO7bX-w=
  This key is used to encrypt and decrypt the data.
```

## Use Cases
- **Smart Grid Security**: Protecting meter data in transit
- **Data Privacy**: Ensuring sensitive usage information remains confidential
- **Audit Trails**: Maintaining encrypted logs of system activities
- **Compliance**: Meeting security requirements for critical infrastructure

## Technical Details
- **Algorithm**: AES-128 in CBC mode with PKCS7 padding
- **Key Management**: Fernet handles key generation and rotation
- **Encoding**: UTF-8 for text, Base64 for binary data
- **Performance**: Optimized for real-time encryption/decryption

## Future Enhancements
- Key persistence and management
- Multiple encryption algorithms
- Performance benchmarking
- Integration with other Smart Shield modules
