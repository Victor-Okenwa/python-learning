from pathlib import Path
import pandas as pd

current_dir = Path(__file__).parent
file_path = current_dir / "customers_ai_training.csv"

df = pd.read_csv(file_path)
print(df)