#!/usr/bin/env python3
"""
Test script to verify the /api/summarize endpoint works correctly.
"""

import requests
import json

print("=" * 60)
print("Testing /api/summarize Endpoint")
print("=" * 60)
print()

# Test material
test_material = """
Photosynthesis is the process by which plants convert light energy 
into chemical energy. It occurs in the chloroplasts and involves 
two main stages: light-dependent reactions and the Calvin cycle. 
The overall equation is: 6CO2 + 6H2O + light → C6H12O6 + 6O2.

During the light-dependent reactions, chlorophyll absorbs light 
energy, which is used to split water molecules and produce ATP 
and NADPH. These energy carriers are then used in the Calvin cycle 
to fix carbon dioxide and produce glucose.
"""

print("Test Material:")
print("-" * 60)
print(test_material[:200] + "...")
print()

# Make API request
print("Sending request to http://localhost:5000/api/summarize...")
print()

try:
    response = requests.post(
        'http://localhost:5000/api/summarize',
        json={'material': test_material},
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    print()
    
    if response.status_code == 200:
        data = response.json()
        print("✓ Success! Response received:")
        print("-" * 60)
        print(json.dumps(data, indent=2))
        print()
        
        if 'summary' in data:
            summary = data['summary']
            if summary and summary != 'null':
                print("✓ Summary field is present and not null")
                print()
                print("Summary Content:")
                print("-" * 60)
                print(summary)
                print()
                print("=" * 60)
                print("✓ Test PASSED!")
                print("=" * 60)
            else:
                print("✗ Summary field is null or empty")
                print("This means the AI returned an empty response.")
                print()
                print("Possible causes:")
                print("  1. API key issue")
                print("  2. Groq API rate limit")
                print("  3. Material too short or unclear")
                print()
                print("Try:")
                print("  - Wait a few seconds and try again")
                print("  - Use longer, more structured material")
                print("  - Check API key in .env file")
        else:
            print("✗ Response missing 'summary' field")
            print("Response structure:", data)
    else:
        print(f"✗ Error: HTTP {response.status_code}")
        try:
            error_data = response.json()
            print("Error details:", json.dumps(error_data, indent=2))
        except:
            print("Error details:", response.text)
            
except requests.exceptions.ConnectionError:
    print("✗ Connection Error")
    print("Make sure Flask server is running:")
    print("  python app.py")
    print()
    
except requests.exceptions.Timeout:
    print("✗ Request Timeout")
    print("The AI service took too long to respond.")
    print("Try again with shorter material.")
    print()
    
except Exception as e:
    print(f"✗ Unexpected Error: {e}")
    print()
