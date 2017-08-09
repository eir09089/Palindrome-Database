
#!flask/bin/python
import os
from os import abort
from flask import Flask,jsonify,request, render_template
import model

app = Flask(__name__)
palindromes = model.Palindrome()



# check if the expression is palindrome
def isPalindrome(phrase):
    clear_input = "".join(e for e in phrase.lower() if e.isalnum())
    return clear_input == clear_input[::-1]


# create the outputs in json format
def create_output(posts):
    palindrome_posts = []
    for p in posts:
        temp_post = {
            "palindrome":p.phrase,
            "time":p.time
        }
        palindrome_posts.append(temp_post)
    return palindrome_posts

# post and get requests
@app.route('/palindromes/api/v1.0/palindrome',methods = ['POST'])
def get_input():
    if not request or not "palindrome" in request.json:
        abort(400)
    pal_aux = request.json["palindrome"]
    anser = isPalindrome(pal_aux)
    if anser:
        palindromes.add(pal_aux)
    return 'True' if anser else 'False' ,201


@app.route('/palindromes/api/v1.0/get_palindromes',methods = ['GET'])
def get_palindromes():
    return jsonify({'Palindromes':palindromes.getPhrases()})

# error handling

@app.errorhandler(404)
def not_found_error(error):
    return  jsonify({'message':'Invalid URL, try /palindromes/api/v1.0/palindrome or /palindromes/api/v1.0/get_palindromes '}) , 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(400)
def custom400(error):
    return jsonify({'message':'no palindrome field in request'})



if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))

