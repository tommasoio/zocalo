import json

def export_results(results):

    with open("data/exports/results.json", "w") as f:
        json.dump(results, f, indent=4)
