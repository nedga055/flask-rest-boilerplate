"""
Utility to generate application secrets
"""
import secrets

application_secret = secrets.token_hex(20)
jwt_secret = secrets.token_hex(20)

print("Application Secret: {}".format(application_secret))
print("JWT Secret: {}".format(jwt_secret))
