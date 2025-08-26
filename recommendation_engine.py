import pandas as pd
from model import recommend_solution
from clarifier import clarify_input

# Load dataset
data = pd.read_csv("dataset/client_requirements.csv")

print("🤖 Welcome to the AI Client Recommendation System!")
print("Tell me about your business requirement:")

user_input = input("👉 ")

# Step 1: Check clarity
if len(user_input.split()) < 5:
    user_input = clarify_input(user_input)

# Step 2: Generate recommendation
recommendation = recommend_solution(user_input, data)

# Step 3: Display result
print("\n✅ Recommended Solution:")
print(f"Platform: {recommendation['platform']}")
print(f"Features: {recommendation['features']}")
print(f"Tech Stack: {recommendation['techstack']}")
