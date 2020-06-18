def abbreviate(words):
    
    
    parts = [palabra[0] for palabra in words.replace("_", "").replace("-", " ").split()]
    return "".join(parts).upper()
