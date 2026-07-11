import time

def classify_waste_item(material_density, structural_rigidity):
    """
    Simulated AI classification model for the Smart-Sort Bin Insert.
    Categorizes waste items using real-time structural data inputs.
    """
    # Threshold variables based on cost-benefit and structural analysis
    if material_density > 0.8 and structural_rigidity > 50:
        return "Recyclable (Metal/Dense Plastic)"
    elif 0.3 <= material_density <= 0.8:
        return "Organic/Biodegradable"
    else:
        return "General Waste / Non-Recyclable"

def run_segregation_simulation():
    print("Initializing Smart-Sort AI Segregation System Analytics...")
    time.sleep(1)
    
    # Mock sensor data stream: (density, rigidity)
    simulated_sensor_data = [
        (0.92, 65),  # Example: Aluminum can
        (0.45, 12),  # Example: Food waste
        (0.15, 5)    # Example: Styrofoam
    ]
    
    for idx, data in enumerate(simulated_sensor_data):
        density, rigidity = data
        category = classify_waste_item(density, rigidity)
        print(f"Item {idx+1}: Density={density}, Rigidity={rigidity} -> Categorized as: {category}")

if __name__ == "__main__":
    run_segregation_simulation()
