#!/usr/bin/env python3

def validate_user(username, minlen):
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
    
