prompt_tokens: int = 150
completion_tokens: int = 50
cost_per_thousand_tokens: float = 0.002

total_tokens: int = prompt_tokens + completion_tokens
total_cost: float = (total_tokens / 1000) * cost_per_thousand_tokens
is_over_budget: bool = total_cost > 0.01

if  is_over_budget or total_tokens == 0:
  print("Status: Warning needed")
else:
  print(f"Status: OK. Total cost: ${total_cost}")

  print(7/2)