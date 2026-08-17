import bcrypt

def hash_password(plain_password:str) -> str:
    salt = bcrypt.gensalt()

    hash_pass = bcrypt.hashpw(plain_password.encode("utf-8"),salt)

    return hash_pass.decode("utf-8")

def verify_password(plain_password: str , hashed_password:str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
        )


# print(f"{hash_password("hello")}")
# print(f"{verify_password("hello" , "$2b$12$xLSAmAzTWlBXit6a.IDhe.jJD1YSmcT2eaY09jSRG/ooLDiOnEFJm")}")


