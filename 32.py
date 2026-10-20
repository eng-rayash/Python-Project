def add(a: int, b:int) -> int:
    return a + b

def find_user(users: list[dict], name: str) -> dict:
    for user in users:
        if user.get("name") == name:
            return user
    return {}