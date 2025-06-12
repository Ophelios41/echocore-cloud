import json

def get_blocked_strategies():
    try:
        with open("data/strategy_registry.json", "r") as f:
            return json.load(f).get("blocked", [])
    except:
        return []

def make_decision(data):
    strategy = data.get("strategy")
    sim_passed = data.get("sim_passed", False)

    if not sim_passed:
        return {"action": "deny", "note": "Simulation failed."}

    if strategy in get_blocked_strategies():
        return {"action": "deny", "note": "Strategy blocked."}

    return {"action": "allow", "note": "Passed all checks."}