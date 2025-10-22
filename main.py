from flask import Flask, render_template, request
import re
import requests
import hashlib

def check_password_strength(password):
    result=[]
    if not password:
        result.append(f"Field is empty!Enter the password")
        return False,result
    if len(password) <= 7 or len(password) >= 17:
        result.append("Password must between 8-16 characters.")
        return False,result
    if not re.search(r"[a-z]", password):
        result.append("Password must contain at least one lowercase letter.")
        return False,result
    if not re.search(r"[A-Z]", password):
        result.append("Password must include at least one uppercase letter.")
        return False,result
    if not re.search(r"\d", password):
        result.append("Password must include at least one digit.")
        return False,result
    if not re.search(r"[!@#$%^&*?]", password):
        result.append("Password must contain at least one special character.")
        return False,result
    if re.search(r"\s", password):
        result.append("Password must not contain spaces.")
        return False,result
    result.append("Password strength check passed.")
    return True,result


def check_pawned_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1password[:5]
    suffix = sha1password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error checking pawned passwords. Try again later.")
        return False,0

    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            print(f"Password has been pwned {count} times! Choose a different password.")
            return True, count

    print("Password not found in pwned database.")
    return False,0


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    all_result=[]
    if request.method == 'POST':
        password = request.form['password']
        valid, result = check_password_strength(password)
        all_result.extend(result)
        if valid:
            pwned,count=check_pawned_password(password)
            if pwned:
                all_result.append(f"Password has been pawned {count} times!")
            else:
                all_result.append("Congrats,you got a Guardian Key.")
        else:
            all_result.append("Password is weak.")
    return render_template('index.html', result=all_result)


if __name__ == "__main__":
    app.run(debug=True)