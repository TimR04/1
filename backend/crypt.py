import bcrypt  # Neu hinzugefügt für Passwort-Hashing

def hash_password(password):
    """Hash das Passwort."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(plain_password, hashed_password):
    """Überprüft, ob das Passwort korrekt ist."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


