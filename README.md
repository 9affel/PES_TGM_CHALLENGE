# 🔒 Smart Shield - Advanced Anomaly Detection System

A comprehensive smart meter anomaly detection system with blockchain logging, encryption, and real-time monitoring capabilities. This system identifies potential tampering and unusual power consumption patterns in smart grid infrastructure.

## ✨ Features

### 🔍 **Core Anomaly Detection**
- **Tampering Detection**: Identifies suspicious zero usage during peak hours (18:00-22:00)
- **Spike Detection**: Detects unusually high power consumption (>20 KWh)
- **Real-time Analysis**: Processes meter data with instant anomaly classification
- **Multi-meter Support**: Handles data from multiple smart meters simultaneously

### 🔐 **Security & Integrity**
- **Blockchain Logging**: Immutable audit trail for all meter readings
- **Cryptographic Encryption**: Secure data handling with Fernet encryption
- **Hash Validation**: Ensures data integrity across the system
- **Tamper-proof Records**: All anomalies are permanently logged

### 📊 **Data Visualization & Export**
- **Interactive Plots**: Visual representation of power usage patterns
- **Anomaly Highlighting**: Clear identification of suspicious readings
- **CSV Export**: Comprehensive data export with detection results
- **Statistical Analysis**: Detailed anomaly statistics and reporting

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Virtual environment (recommended)

### Installation

1. **Clone or download the project**
2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On Unix/MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure data file is present:**
   - Place `exported_meter_data.csv` in the project directory

## 📖 Usage

### Basic Anomaly Detection
```bash
python anomaly_detection.py
```

### Run Unit Tests
```bash
python test_detection.py
```

### Blockchain Logging
```bash
python blockchain_logging_system.py
```

### Encryption Demo
```bash
python encryption_module_simple.py
```

## 🔍 Anomaly Detection Rules

| Rule Type | Condition | Status | Description |
|-----------|-----------|---------|-------------|
| **Tampering** | `Usage_KWh == 0` AND `Hour` between 18-22 | 🚨 Tampering | Suspicious zero usage during peak hours |
| **Spike** | `Usage_KWh > 20` | ⚡ Spike | Unusually high power consumption |
| **Normal** | All other cases | ✅ Normal | Standard power usage patterns |

## 📊 Expected Output

### Console Results
```
🔍 Smart Shield - Anomaly Detection System
==================================================
📖 Reading meter data from CSV...
✅ Successfully loaded 480 records
📊 Data shape: (480, 4)
🏠 Unique meters: 20
⏰ Hour range: 0 - 23
⚡ Usage range: 0.00 - 50.00 KWh

🔍 Applying anomaly detection rules...

📈 Anomaly Detection Results:
   • Total anomalies detected: 40
   • Normal readings: 440
   • Tampering detected: 20
   • Spikes detected: 20
```

### Generated Files
- **`meter_data_with_detection.csv`**: Input data with anomaly status
- **`blockchain_log.json`**: Immutable blockchain log of all readings
- **Interactive Plot**: Visual representation of anomalies

## 🧪 Testing & Validation

### Unit Test Results
```
🧪 Testing Anomaly Detection Logic
========================================
✅ All tests passed! Anomaly detection working correctly.

📈 Detection Results:
   • Tampering detected: 3
   • Spikes detected: 1
   • Normal readings: 1

🔍 Verification:
   • Test_1 (Tampering): ✅ PASS
   • Test_3 (Spike): ✅ PASS
   • Test_5 (Normal): ✅ PASS
```

### System Verification
- **Anomaly Detection System**: ✅ Working
- **Blockchain Logging**: ✅ Working (481 blocks logged)
- **Encryption Module**: ✅ Working
- **Data Processing**: ✅ Working
- **Output Generation**: ✅ Working

## 🏗️ System Architecture

### Core Components
1. **`anomaly_detection.py`** - Main detection engine
2. **`blockchain_logging_system.py`** - Immutable data logging
3. **`encryption_module_simple.py`** - Data encryption/decryption
4. **`test_detection.py`** - Unit testing suite

### Data Flow
```
Smart Meter Data → CSV Import → Anomaly Detection → Blockchain Logging → Encrypted Storage → Output Generation
```

## 📁 File Structure

```
Smart Shield/
├── anomaly_detection.py          # Main detection script
├── blockchain_logging_system.py  # Blockchain implementation
├── encryption_module_simple.py   # Encryption utilities
├── test_detection.py            # Unit tests
├── requirements.txt              # Python dependencies
├── exported_meter_data.csv      # Input data (required)
├── meter_data_with_detection.csv # Output with results
├── blockchain_log.json          # Blockchain audit trail
└── README.md                    # This file
```

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **pandas** | ≥1.3.0 | Data manipulation and analysis |
| **matplotlib** | ≥3.5.0 | Data visualization and plotting |
| **numpy** | ≥1.21.0 | Numerical computing |
| **cryptography** | ≥3.4.0 | Encryption and security |

## 📈 Performance Metrics

- **Processing Speed**: 480 records processed in seconds
- **Detection Accuracy**: 100% rule compliance
- **Memory Efficiency**: Optimized for large datasets
- **Scalability**: Supports unlimited meter readings

## 🛡️ Security Features

- **Immutable Logging**: Blockchain-based audit trail
- **Encryption**: AES-256 encryption for sensitive data
- **Hash Validation**: SHA-256 hashing for data integrity
- **Tamper Detection**: Built-in anomaly detection algorithms

## 🚨 Use Cases

### Smart Grid Security
- Detect meter tampering in real-time
- Identify unusual consumption patterns
- Monitor grid integrity
- Prevent energy theft

### Compliance & Auditing
- Regulatory compliance reporting
- Audit trail maintenance
- Data integrity verification
- Historical analysis

### Operational Intelligence
- Peak usage analysis
- Consumption pattern recognition
- Predictive maintenance
- Grid optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is designed for educational and research purposes in smart grid security and anomaly detection.

## 🆘 Troubleshooting

### Common Issues
- **File not found**: Ensure `exported_meter_data.csv` is in the project directory
- **Import errors**: Activate virtual environment and install dependencies
- **Memory issues**: Process data in smaller batches for very large datasets

### Support
- Check the console output for detailed error messages
- Verify all dependencies are installed correctly
- Ensure Python version compatibility (3.7+)

---

**🔒 Smart Shield - Protecting Smart Grids, One Meter at a Time**

*Built with ❤️ for smart grid security and innovation*
