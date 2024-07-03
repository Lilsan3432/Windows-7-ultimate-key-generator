import random
import string

def generate_random_code():
    characters = string.ascii_uppercase + string.digits
    code_sections = []
    for _ in range(5):
        section = ''.join(random.choices(characters, k=5))
        code_sections.append(section)
    return '-'.join(code_sections)

def generate_multiple_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = generate_random_code()
        codes.append(code)
    return codes

if __name__ == "__main__":
    num_codes = 100
    random_codes = generate_multiple_codes(num_codes)
    for code in random_codes:
        print(code)
    
    input("Press Enter to exit...")
