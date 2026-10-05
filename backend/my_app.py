from flask import Flask
app = Flask(__name__)
@app.route('/api/home')
def Bonjour():
    return 'Bonjour, les amis !'
    
if __name__ == '__main__':
    app.run(debug=True)
