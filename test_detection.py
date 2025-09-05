import pandas as pd
from anomaly_detection import detect_anomalies

def test_anomaly_detection():
    """
    Test the anomaly detection logic with sample data.
    """
    print("🧪 Testing Anomaly Detection Logic")
    print("=" * 40)
    
    # Create test data
    test_data = {
        'Meter_ID': ['Test_1', 'Test_2', 'Test_3', 'Test_4', 'Test_5'],
        'Hour': [19, 21, 5, 18, 22],
        'Usage_KWh': [0.0, 0.0, 25.0, 0.0, 15.0],
        'Status': ['Normal', 'Normal', 'Normal', 'Normal', 'Normal']
    }
    
    df_test = pd.DataFrame(test_data)
    print("📊 Test Data:")
    print(df_test)
    
    # Apply detection
    df_detected = detect_anomalies(df_test)
    print("\n🔍 After Anomaly Detection:")
    print(df_detected)
    
    # Verify results
    print("\n✅ Expected Results:")
    print("   • Test_1 (Hour 19, Usage 0.0) → Should be 'Tampering'")
    print("   • Test_2 (Hour 21, Usage 0.0) → Should be 'Tampering'")
    print("   • Test_3 (Hour 5, Usage 25.0) → Should be 'Spike'")
    print("   • Test_4 (Hour 18, Usage 0.0) → Should be 'Tampering'")
    print("   • Test_5 (Hour 22, Usage 15.0) → Should be 'Normal'")
    
    # Check if detection worked correctly
    tampering_count = len(df_detected[df_detected['Status'] == 'Tampering'])
    spike_count = len(df_detected[df_detected['Status'] == 'Spike'])
    normal_count = len(df_detected[df_detected['Status'] == 'Normal'])
    
    print(f"\n📈 Detection Results:")
    print(f"   • Tampering detected: {tampering_count}")
    print(f"   • Spikes detected: {spike_count}")
    print(f"   • Normal readings: {normal_count}")
    
    # Verify specific cases
    test_1_status = df_detected[df_detected['Meter_ID'] == 'Test_1']['Status'].iloc[0]
    test_3_status = df_detected[df_detected['Meter_ID'] == 'Test_3']['Status'].iloc[0]
    test_5_status = df_detected[df_detected['Meter_ID'] == 'Test_5']['Status'].iloc[0]
    
    print(f"\n🔍 Verification:")
    print(f"   • Test_1 (Tampering): {'✅ PASS' if test_1_status == 'Tampering' else '❌ FAIL'}")
    print(f"   • Test_3 (Spike): {'✅ PASS' if test_3_status == 'Spike' else '❌ FAIL'}")
    print(f"   • Test_5 (Normal): {'✅ PASS' if test_5_status == 'Normal' else '❌ FAIL'}")
    
    if tampering_count == 3 and spike_count == 1 and normal_count == 1:
        print("\n🎉 All tests passed! Anomaly detection working correctly.")
    else:
        print("\n❌ Some tests failed. Please check the detection logic.")

if __name__ == "__main__":
    test_anomaly_detection()
