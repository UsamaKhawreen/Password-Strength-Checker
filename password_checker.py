import re


def check_password_strength(password):
    strength = 0
    remarks = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Include at least one digit.")

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character (@$!%*?&).")

    # Evaluate password strength
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]

    print(f"Password Strength: {strength_levels[strength]}")
    if remarks:
        print("Suggestions:")
        for remark in remarks:
            print(f"- {remark}")


# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
