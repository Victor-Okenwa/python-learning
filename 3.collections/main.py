# LISTS


from typing import Any


models: list[str] = ["gpt-4o", "claude-3.5-sonnet"]

models.append("gpt-4o-mini")
print(models)

# TUPLES
models_tuple: tuple[str, ...] = ("gpt-4o", "claude-3.5-sonnet")
print(models_tuple)

# SETS
unique_tags: set[str] = {"llm", "rag", "llm"}
unique_tags.add("agent")

print(unique_tags)

has_rag = "rag" in unique_tags
print(has_rag)

# DICTIONARIES
payload: dict[str, float] = {
 "temperature": 0.5,
 "top_p": 0.9
}

print(payload)


# OVERVIEW

allowed_models: set[str] = {"gpt-4o", "claude-3.5-sonnet"}
default_params: dict[str, Any] = {
    "temperature": 0.2,
    "max_tokens": 500,
  }

is_allowed: bool = "gpt-4o" in allowed_models

print(f"Model allowed: {is_allowed}")
print(f"Max tokens: {default_params['max_tokens']}")

config = {"temp": 0.7}
print(config["max_tokens"])