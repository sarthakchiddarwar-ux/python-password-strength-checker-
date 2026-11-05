import re

def check_password_strength(password):
    # Test Case 3: Invalid Input Checks
    if not password:
        return "Password cannot be empty.", None
    if " " in password:
        return "Password must not contain spaces.", None

    score = 0
    suggestions = []

    # Rule 1: Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("use at least 8 characters")

    # Rule 2: Uppercase Check (Using Sets for variety as per concepts requested)
    if not set(password).isdisjoint(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        score += 1
    else:
        suggestions.append("add an uppercase letter")

    # Rule 3: Lowercase Check
    if not set(password).isdisjoint(set("abcdefghijklmnopqrstuvwxyz")):
        score += 1
    else:
        suggestions.append("add a lowercase letter")

    # Rule 4: Digit Check (Using re module as requested)
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("add a digit")

    # Rule 5: Special Character Check (@#$%&*!)
    special_chars = "@#$%&*!"
    if any(char in special_chars for char in password):
        score += 1
    else:
        suggestions.append("add a special character")

    # Determine Classification based on Score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # Format Output to match Test Case expectations
    output = f"Strength: {strength} ({score}/5)\n"
    if suggestions:
        # Join suggestions nicely with commas
        output += f"Suggestions: {', '.join(suggestions)}"
    else:
        output += "No suggestions. Your password is secure."

    return output, strength

def main():
    print("--- Password Strength Checker ---")
    user_password = input("Enter Password: ")
    result, _ = check_password_strength(user_password)
    print(result)

if __name__ == "__main__":
    main()
 