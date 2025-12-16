import re

# REGISTER VALIDATOR
def validate_register(data):
    required_fields = ["username", "password", "email", "nama"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"{field} wajib diisi"

    if len(data["username"]) < 3:
        return False, "Username minimal 3 karakter"

    if len(data["password"]) < 6:
        return False, "Password minimal 6 karakter"

    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, data["email"]):
        return False, "Format email tidak valid"

    return True, None

# LOGIN VALIDATOR
def validate_login(data):
    if "username" not in data or not str(data["username"]).strip():
        return False, "Username wajib diisi"

    if "password" not in data or not str(data["password"]).strip():
        return False, "Password wajib diisi"

    return True, None


# UPDATE USER VALIDATOR
def validate_update_user(data):
    if not data:
        return False, "Data tidak boleh kosong"

    if "email" in data:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, data["email"]):
            return False, "Format email tidak valid"

    if "username" in data and len(data["username"]) < 3:
        return False, "Username minimal 3 karakter"

    return True, None
