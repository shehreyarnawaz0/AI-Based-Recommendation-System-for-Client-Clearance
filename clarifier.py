def clarify_input(user_input):
    print("🤔 Your requirement seems unclear. Let me ask a few questions.")
    
    business_type = input("What type of business do you run? (e.g., Restaurant, Salon, Retail) 👉 ")
    scope = input("Do you need a small, medium, or large-scale system? 👉 ")
    preferred_platform = input("Do you prefer Mobile, Web, or Desktop? 👉 ")

    clarified = f"{user_input} | Business: {business_type} | Scope: {scope} | Preference: {preferred_platform}"
    return clarified

