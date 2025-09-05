"""
Smart Shield Prototype - Encryption Module (Simple Version)
This module demonstrates AES encryption using the cryptography library.
"""

import pandas as pd
import random
from cryptography.fernet import Fernet


def demo_encryption():
    """
    Demonstrates AES encryption by:
    1. Loading meter data from CSV
    2. Picking a random reading
    3. Encrypting and decrypting the data
    4. Displaying results in a beginner-friendly format
    """
    
    print("Smart Shield Prototype - Encryption Demo")
    print("=" * 50)
    
    try:
        # Step 1: Load the CSV data using pandas
        print("Loading meter data from CSV...")
        df = pd.read_csv('meter_data_with_detection.csv')
        print("Loaded {} meter readings successfully!".format(len(df)))
        
        # Step 2: Pick a random row from the data
        random_row = df.sample(n=1).iloc[0]
        meter_id = random_row['Meter_ID']
        hour = int(random_row['Hour'])
        usage = random_row['Usage_KWh']
        status = random_row['Status']
        
        # Format the reading as requested: "House_5 - 7.4 kWh at 14h"
        original_text = "{} - {:.1f} kWh at {}h".format(meter_id, usage, hour)
        
        print("\nRandomly selected reading:")
        print("  Meter: {}".format(meter_id))
        print("  Hour: {}".format(hour))
        print("  Usage: {:.1f} kWh".format(usage))
        print("  Status: {}".format(status))
        
        # Step 3: Generate encryption key and create Fernet cipher
        print("\nGenerating encryption key...")
        key = Fernet.generate_key()
        cipher = Fernet(key)
        
        # Step 4: Encrypt the original text
        print("Encrypting the reading...")
        encrypted_data = cipher.encrypt(original_text.encode())
        
        # Step 5: Decrypt the encrypted data to prove recovery
        print("Decrypting to verify...")
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_text = decrypted_data.decode()
        
        # Step 6: Display results in a clear, beginner-friendly format
        print("\nENCRYPTION RESULTS:")
        print("=" * 50)
        print("Original Text:     '{}'".format(original_text))
        print("Encrypted Text:    {}".format(encrypted_data))
        print("Decrypted Text:    '{}'".format(decrypted_text))
        
        # Verify the decryption was successful
        if original_text == decrypted_text:
            print("\nSUCCESS: Encryption and decryption completed successfully!")
            print("  The original data was perfectly recovered.")
        else:
            print("\nERROR: Decryption failed - data mismatch detected!")
            
        print("\nEncryption Key (Base64): {}".format(key.decode()))
        print("  This key is used to encrypt and decrypt the data.")
        
    except FileNotFoundError:
        print("ERROR: Could not find 'meter_data_with_detection.csv' file!")
        print("  Please ensure the CSV file is in the same directory.")
    except Exception as e:
        print("ERROR: An unexpected error occurred: {}".format(str(e)))
        print("  Please check your data and try again.")


if __name__ == "__main__":
    # Run the encryption demo when the script is executed directly
    demo_encryption()
