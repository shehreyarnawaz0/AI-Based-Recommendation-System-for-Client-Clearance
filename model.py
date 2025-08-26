def recommend_solution(user_input, data):
    user_input = user_input.lower()

    # Rule-based matching
    if "restaurant" in user_input:
        return {"platform": "Mobile App", "features": "Menu, Online Ordering", "techstack": "Flutter + Firebase"}
    elif "salon" in user_input:
        return {"platform": "Web App", "features": "Booking System, Notifications", "techstack": "Django + React"}
    elif "retail" in user_input:
        return {"platform": "Web App", "features": "Inventory, Sales Reports", "techstack": "MERN Stack"}
    elif "logistics" in user_input:
        return {"platform": "Mobile + Web", "features": "Tracking, Reports", "techstack": "React Native + Node.js"}
    else:
        return {"platform": "Web App", "features": "Basic Management System", "techstack": "Python Flask + SQLite"}
