from dataclasses import dataclass
from pydantic import BaseModel, Field

class LLMRequest:
    def __init__(self, model: str, max_tokens: int = 1000) -> None:
        self.model: str = model
        self.max_tokens: int = max_tokens

        def get_summary(self) -> str:
            return f"{self.model_name} maxed at {self._max_tokens} tokens"

# Define data types with class

@dataclass
class Config:
    model: str
    temp: float = 0.9
config = Config("Grok", 0.8)
# print(config.model_name)

class LLMRequest2(BaseModel):
    model_name: str
    temp: float = Field(default = 0.7, ge = 0.0, le = 2.0)

llm = LLMRequest2(model_name="gpt", temp= 0.5)
print(llm)


# Exercise
class TokenCounter:
    def __init__(self, model_name: str, total_tokens: int = 0) -> None:
        self.model_name: str = model_name
        self._total_tokens: int = total_tokens

    def add_tokens(self, count: int) -> None:
        self._total_tokens += count

    def get_total(self) -> int:
        return self._total_tokens

counter = TokenCounter("gpt-4o")
counter.add_tokens(150)
print(counter.get_total())
