import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def detect_anomalies(df):
    """
    Apply anomaly detection rules to the DataFrame.
    
    Rules:
    - If Usage_KWh == 0 and Hour between 18 and 22 → Status = "Tampering"
    - If Usage_KWh > 20 → Status = "Spike"
    - Else → Status = "Normal"
    """
    # Create a copy to avoid modifying the original
    df_detected = df.copy()
    
    # Apply anomaly detection rules
    # Rule 1: Tampering detection (Usage_KWh == 0 and Hour between 18-22)
    tampering_mask = (df_detected['Usage_KWh'] == 0) & (df_detected['Hour'].between(18, 22))
    df_detected.loc[tampering_mask, 'Status'] = 'Tampering'
    
    # Rule 2: Spike detection (Usage_KWh > 20)
    spike_mask = df_detected['Usage_KWh'] > 20
    df_detected.loc[spike_mask, 'Status'] = 'Spike'
    
    # Rule 3: Normal (everything else)
    normal_mask = ~(tampering_mask | spike_mask)
    df_detected.loc[normal_mask, 'Status'] = 'Normal'
    
    return df_detected

def plot_sample_house(df, meter_id='House_1'):
    """
    Plot usage vs hour for a sample house, marking anomalies in red.
    """
    # Filter data for the specified house
    house_data = df[df['Meter_ID'] == meter_id].copy()
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    
    # Plot normal readings in blue
    normal_data = house_data[house_data['Status'] == 'Normal']
    plt.scatter(normal_data['Hour'], normal_data['Usage_KWh'], 
                color='blue', alpha=0.7, label='Normal', s=50)
    
    # Plot tampering in red
    tampering_data = house_data[house_data['Status'] == 'Tampering']
    if not tampering_data.empty:
        plt.scatter(tampering_data['Hour'], tampering_data['Usage_KWh'], 
                    color='red', alpha=0.8, label='Tampering', s=100, marker='x')
    
    # Plot spikes in red
    spike_data = house_data[house_data['Status'] == 'Spike']
    if not spike_data.empty:
        plt.scatter(spike_data['Hour'], spike_data['Usage_KWh'], 
                    color='red', alpha=0.8, label='Spike', s=100, marker='^')
    
    # Customize the plot
    plt.xlabel('Hour of Day')
    plt.ylabel('Usage (KWh)')
    plt.title(f'Power Usage vs Hour for {meter_id} - Anomaly Detection')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(range(0, 24))
    
    # Add horizontal line at y=20 to show spike threshold
    plt.axhline(y=20, color='orange', linestyle='--', alpha=0.7, label='Spike Threshold (20 KWh)')
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the anomaly detection system.
    """
    print("🔍 Smart Shield - Anomaly Detection System")
    print("=" * 50)
    
    try:
        # Step 1: Read the CSV file
        print("📖 Reading meter data from CSV...")
        df = pd.read_csv("exported_meter_data.csv")
        print(f"✅ Successfully loaded {len(df)} records")
        
        # Display basic info about the data
        print(f"📊 Data shape: {df.shape}")
        print(f"🏠 Unique meters: {df['Meter_ID'].nunique()}")
        print(f"⏰ Hour range: {df['Hour'].min()} - {df['Hour'].max()}")
        print(f"⚡ Usage range: {df['Usage_KWh'].min():.2f} - {df['Usage_KWh'].max():.2f} KWh")
        
        # Step 2: Apply anomaly detection rules
        print("\n🔍 Applying anomaly detection rules...")
        df_detected = detect_anomalies(df)
        
        # Step 3: Count anomalies
        anomaly_counts = df_detected['Status'].value_counts()
        total_anomalies = len(df_detected[df_detected['Status'] != 'Normal'])
        
        print(f"\n📈 Anomaly Detection Results:")
        print(f"   • Total anomalies detected: {total_anomalies}")
        print(f"   • Normal readings: {anomaly_counts.get('Normal', 0)}")
        print(f"   • Tampering detected: {anomaly_counts.get('Tampering', 0)}")
        print(f"   • Spikes detected: {anomaly_counts.get('Spike', 0)}")
        
        # Step 4: Display list of anomalies
        print(f"\n🚨 List of Anomalies:")
        anomalies = df_detected[df_detected['Status'] != 'Normal']
        if not anomalies.empty:
            print(anomalies[['Meter_ID', 'Hour', 'Status', 'Usage_KWh']].to_string(index=False))
        else:
            print("   No anomalies detected!")
        
        # Step 5: Save results to new CSV
        print(f"\n💾 Saving results to 'meter_data_with_detection.csv'...")
        df_detected.to_csv("meter_data_with_detection.csv", index=False)
        print("✅ Results saved successfully!")
        
        # Step 6: Bonus - Plot usage vs hour for sample house
        print(f"\n📊 Generating visualization for House_1...")
        plot_sample_house(df_detected, 'House_1')
        
        print("\n🎉 Anomaly detection completed successfully!")
        
    except FileNotFoundError:
        print("❌ Error: 'exported_meter_data.csv' file not found!")
        print("   Please make sure the file is in the current directory.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
