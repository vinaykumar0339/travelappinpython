'''from werkzeug.security import generate_password_hash

def generate_hashed_password(plain_password):
    # Generate a hashed password
    hashed_password = generate_password_hash(plain_password, method='pbkdf2:sha256')
    return hashed_password

def main():
    # Example usage
    plain_password = input("Enter the password you want to hash: ")
    hashed_password = generate_hashed_password(plain_password)
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()'''

'''from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit_form():
    name=request.form['name']
    email=request.form['email']
    return f"Received Name:{name}, Email:{email} "
if __name__=='__main__':
    app.run(debug=True)'''


