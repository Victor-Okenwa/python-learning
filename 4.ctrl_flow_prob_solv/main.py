
# CONDITIONAL
score: float = 3.8

if score >= 4.5:
    print("Grade: A")
elif score >= 3.5:
    print("Grade: B")
elif score >= 2.5:
    print("Grade: C")
else:
    print("Grade: F")

# LOOPS
models: list[str] = ["gpt-4o", "claude-3.5-sonnet", "gemini-2.5-flash"]
scores: list[float] = [4.5, 3.5, 2.5, 1.5, 0.5]
# simple loop
for model in models:
    print(model)

# loop with index
for i in range(len(models)):
    print(f"Model {i}: {models[i]}")

# loop with enumerate i.e index and item
for index, model in enumerate(models):
    print(f"Model {index}: {model}")

print("-"*10)

# looping through two lists simutenouely using zip
for model, score in zip(models, scores):
    print(f"Model: {model}, Score: {score}")

# EXERCISES

prompt_list: list[str] = ["Summary text", "Extract entities", "Classify sentiment"]
for index, prompt_text in enumerate(prompt_list):
    prompt_number: int = index + 1
    
    if prompt_text == "Extract entities":
        print(f"Skipping prompt {prompt_number}")
        continue
    print(f"Running prompt {prompt_number}: {prompt_text}")

for item in [1, 2, 3]:
    if item == 5:
        break
else:
    print("Loop finished normally")