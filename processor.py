
from collections import Counter
import statistics

def extract_insights(data):
    routes = [f"{d['origin']} → {d['destination']}" for d in data]
    prices = [d['price'] for d in data]
    demand_scores = [d['demand_score'] for d in data]

    most_common_routes = Counter(routes).most_common(3)
    average_price = round(statistics.mean(prices), 2)
    peak_demand = max(demand_scores)

    return {
        'most_common_routes': most_common_routes,
        'average_price': average_price,
        'peak_demand': peak_demand
    }
