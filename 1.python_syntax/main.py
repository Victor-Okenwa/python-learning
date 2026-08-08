model_name: str = "gemini"
max_tokens: int = 1000
is_temperature_high: bool= True

if max_tokens >= 1000 and not is_temperature_high:
    print(f"Configuring model {model_name} for structured tasks.")
else:
    print(f"Configuring model {model_name} for creative tasks..")

# String interpolation and concatenation
tokens = 500
message = "Token count: " + str(tokens)
print(message)
