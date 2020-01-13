# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api, request
import wordninja

app = Flask(__name__)
api = Api(app)
blacklist = [
'php',
'javascript',
'microsoft',
'windows',
'mssql',
'healthy',
'gym',
'running',
'authorization',
'accept',
'loves',
'hate',
'number',
'token',
'nails',
'the',
'a',
'smaller',
'bigger',
'huge',
'tiny']
def check(word):
        if word.lower() in blacklist:
            return {'word': word, 'isBlacklisted': True }
        else:
            return {'word': word, 'isBlacklisted': False }

class HelloWorld(Resource):
    def get(self):
        input = request.args.get('input', default = '*', type = str)
        output = wordninja.split(input)
        results = []
        for word in output:
            results.append(check(word))
        return results

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')