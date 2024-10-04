import random
from datetime import datetime, timedelta

# Function to generate random birthday between 15-30 years old
def generate_random_birthday(min_age=15, max_age=30):
    today = datetime.today()
    min_birth_year = today.year - max_age
    max_birth_year = today.year - min_age
    start_date = datetime(min_birth_year, 1, 1)
    end_date = datetime(max_birth_year, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d")

# Function to calculate age from birthday
def calculate_age(birthday):
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Function to get ANSI escape codes for background colors
def get_background_color_code(color):
    colors = {
        "Red": "41",
        "Green": "42",
        "Blue": "44",
        "Yellow": "43",
        "Purple": "45",
        "Orange": "48;5;208",
        "Pink": "48;5;213",
        "Brown": "48;5;94",
        "Gray": "48;5;235",
        "Black": "40"
    }
    return colors.get(color, "40")  # Default to black if color not found

# Function to generate random identity profile
def generate_identity_profile():
    first_names = ["Aarav", "Maya", "Ishan", "Nisha", "Ravi", "Ananya", "Sanjay", "Tara", "Arjun", "Meera"]
    last_names = ["Perera", "Rajapaksa", "Fernando", "Kumar", "Silva", "Jayasinghe", "De Silva", "Gunaratne", "Mendis", "Dissanayake"]
    addresses = [
        "No. 12, Park Road, Colombo 05",
        "No. 24, Main Street, Kandy",
        "No. 36, Beach Road, Negombo",
        "No. 48, Hill Street, Nuwara Eliya",
        "No. 60, Station Road, Jaffna",
        "No. 72, Market Lane, Galle",
        "No. 84, Temple Road, Anuradhapura",
        "No. 96, Harbour Street, Trincomalee"
    ]
    colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Black"]

    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    birthday = generate_random_birthday()
    age = calculate_age(birthday)
    address = random.choice(addresses)
    favorite_color = random.choice(colors)
    phone_number = f"+94 {random.randint(10000000, 99999999)}"
    email = f"{full_name.replace(' ', '.').lower()}@example.com"

    profile = {
        "Full Name": full_name,
        "Birthday": birthday,
        "Age": age,
        "Address": address,
        "Favorite Color": favorite_color,
        "Phone Number": phone_number,
        "Email": email
    }

    return profile

# Function to print the identity profile
def print_profile(profile):
    header = "\033[1;34mTool Name: Identity Profile Generator\033[0m"
    creator = "\033[1;33mTool Creator: Specter CH\033[0m"
    
    print(header)
    print(creator)
    print("\nIdentity Profile:")
    for key, value in profile.items():
        if key == "Favorite Color":
            bg_color = get_background_color_code(value)
            print(f"\033[1;37;{bg_color}m{key}: {value}\033[0m")
        else:
            print(f"{key}: {value}")

# Function to display tool startup header
def display_startup_header():
    print("\033[1;32m====================================\033[0m")
    print("\033[1;35m     WELCOME TO IDENTITY GENERATOR     \033[0m")
    print("\033[1;32m====================================\033[0m")
    print("\n\033[1;36mTool Name: Identity Profile Generator v1.0\033[0m")
    print("\033[1;33mCreated by: Specter CH\033[0m")
    print("\033[1;32m====================================\033[0m\n")

if __name__ == "__main__":
    # Display the tool startup header
    display_startup_header()

    while True:
        profile = generate_identity_profile()
        print_profile(profile)
        input("\nPress Enter to generate another profile...")