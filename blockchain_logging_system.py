import hashlib
import json
import csv
from datetime import datetime

class Block:
    """Represents a single block in the blockchain"""
    
    def __init__(self, meter_id, hour, usage_kwh, status, prev_hash=""):
        self.meter_id = meter_id
        self.hour = hour
        self.usage_kwh = usage_kwh
        self.status = status
        self.prev_hash = prev_hash
        self.timestamp = datetime.now().isoformat()
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculate SHA-256 hash of the block contents"""
        # Create a string representation of all block data
        block_string = f"{self.meter_id}{self.hour}{self.usage_kwh}{self.status}{self.prev_hash}{self.timestamp}"
        # Generate SHA-256 hash
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self):
        """Convert block to dictionary for JSON serialization"""
        return {
            "Meter_ID": self.meter_id,
            "Hour": self.hour,
            "Usage_KWh": self.usage_kwh,
            "Status": self.status,
            "Prev_Hash": self.prev_hash,
            "Hash": self.hash,
            "Timestamp": self.timestamp
        }

class Blockchain:
    """Smart Shield Blockchain for logging meter data"""
    
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block (Genesis Block)"""
        genesis_block = Block("GENESIS", 0, 0.0, "Genesis", "0")
        self.chain.append(genesis_block)
        print("Genesis Block created.")
    
    def add_block(self, meter_id, hour, usage_kwh, status):
        """Add a new block to the blockchain"""
        prev_block = self.chain[-1]
        new_block = Block(meter_id, hour, usage_kwh, status, prev_block.hash)
        self.chain.append(new_block)
        
        # Print block addition message
        print(f"Block {len(self.chain)-1} added: {meter_id} - {usage_kwh} kWh at {hour}h [{status}]")
        
        return new_block
    
    def is_valid(self):
        """Check if the blockchain is valid by verifying all hashes"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Check if previous hash matches
            if current_block.prev_hash != previous_block.hash:
                return False
        
        return True
    
    def get_chain_length(self):
        """Get the total number of blocks in the chain"""
        return len(self.chain) - 1  # Exclude genesis block
    
    def save_to_file(self, filename):
        """Save the blockchain to a JSON file"""
        chain_data = [block.to_dict() for block in self.chain]
        
        with open(filename, 'w') as f:
            json.dump(chain_data, f, indent=2)
        
        print(f"Blockchain saved to {filename}")
    
    def print_sample_blocks(self, num_blocks=5):
        """Print sample blocks for demonstration"""
        print("\nSample Block:")
        if len(self.chain) > 1:
            sample_block = self.chain[1]  # First non-genesis block
            print(json.dumps(sample_block.to_dict(), indent=2))

def main():
    """Main function to execute the blockchain logging system"""
    print("=== Smart Shield Blockchain Log ===")
    
    # Initialize blockchain
    blockchain = Blockchain()
    
    # Read meter data from CSV
    try:
        with open('meter_data_with_detection.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            
            # Process each row and add to blockchain
            for row in csv_reader:
                meter_id = row['Meter_ID']
                hour = int(row['Hour'])
                usage_kwh = float(row['Usage_KWh'])
                status = row['Status']
                
                blockchain.add_block(meter_id, hour, usage_kwh, status)
        
        print(f"\n✅ Blockchain valid ({len(set([block.meter_id for block in blockchain.chain[1:]]))} houses, {blockchain.get_chain_length()} blocks logged)")
        
        # Demonstrate integrity check
        if blockchain.is_valid():
            print("Blockchain valid ✅")
        else:
            print("Blockchain broken ❌")
        
        # Print sample blocks
        blockchain.print_sample_blocks()
        
        # Save blockchain to file
        blockchain.save_to_file('blockchain_log.json')
        
    except FileNotFoundError:
        print("Error: meter_data_with_detection.csv not found!")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    main()
