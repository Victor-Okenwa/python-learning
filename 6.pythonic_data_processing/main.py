# Converting items in a list to uppercase
items = ['python', 'java', 'c++', 'javascript', 'ruby']
uppercase_items = [item.upper() for item in items]

print(uppercase_items)

# Filtering and performing an operation on a list
tokens = [120, 4500, 80, 2300]
large_prompts = [t/1000 for t in tokens if t > 1000]
print(large_prompts)

#  Operation on dictionaries
model_scores = {"gpt-4o": 0.95, "claude": 0.88, "legacy_model": 0.40}
# Filter out models with low scores and format the keys
high_performers = {
    key: score
    for key, score in model_scores.items()
    if score >= 0.88
}
print(high_performers)

# Python Top level functions : all and any
scores = [0.85, 0.92, 0.78]
has_top_score = any(s > 0.9 for s in scores)
all_passed = all(s > 0.9 for s in scores)

print(has_top_score, all_passed)

#  Exercise 
prompt_tokens: list[int] = [250, 1200, 850, 3000, 400]
heavy_prompt_costs: list[int | None] = [token * 0.000002 for token in prompt_tokens if token > 500]
print(heavy_prompt_costs)