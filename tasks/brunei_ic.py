import random

def generate_brunei_ic(nationality):
    if nationality.lower() == "brunei":
        prefix = random.choice(["00", "01"])
    elif nationality.lower() == "pr":
        prefix = "03"
    else:
        prefix = "51"
    remaining_digits = random.randint(100000, 999999)
    return f"{prefix}-{remaining_digits}"

def hide_password(password):
    return 'x' * len(password)
