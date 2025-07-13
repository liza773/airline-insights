
def get_data(source, destination):
    # Simulate fake airline booking data
    data = [
        {'route': f'{source} → {destination}', 'price': 350, 'month': 'July', 'demand_score': 7},
        {'route': f'{source} → {destination}', 'price': 400, 'month': 'August', 'demand_score': 9},
        {'route': f'{source} → {destination}', 'price': 420, 'month': 'August', 'demand_score': 8},
        {'route': f'{source} → {destination}', 'price': 300, 'month': 'June', 'demand_score': 6},
    ]
    return data
