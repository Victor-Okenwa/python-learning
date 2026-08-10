# Normal Python functions
from typing import Any, Union


def format_prompt(system_prompt: str, user_query: str, max_tokens: int):
    return f"[System: {system_prompt}] User: {user_query} (Max: {max_tokens})"

result1 = format_prompt("You are a helpful assistant", "What is the capital of France?", 100)
# calling the function with the arguments as keys for readability
result2 = format_prompt(system_prompt="You are a helpful assistant", user_query="What is the capital of France?", max_tokens=100)

print(result1, result2)

# Multiple return values
def calculate_metrics(total_tokens: int, cost_per_token: float)-> tuple[float, bool]:
    total_cost = total_tokens * cost_per_token
    is_expensive = total_cost > 1.00
    return total_cost, is_expensive

cost, is_expensive = calculate_metrics(100, 0.01)
print(cost, is_expensive)



# Exercise
from typing import Optional

def configure_api_call(
    model_name: str,
    temperature: float = 0.7,
    stop_sequence: Optional[str] = None,
) -> str:
    stop_msg = f" Stop: {stop_sequence}" if stop_sequence else ""
    return f"Calling {model_name} at temp {temperature}.{stop_msg}"

print(configure_api_call("gpt-4o", temperature=0.5, stop_sequence="Stop"))

def update_params(params: dict = {}) -> dict:
    params["count"] = params.get("count", 0) + 1
    return params

print(update_params())
print(update_params())