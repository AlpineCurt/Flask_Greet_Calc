from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_route():
    print('begin add route')
    a = int(request.args['a'])
    b = int(request.args['b'])
    print(a, b)
    return str(operations.add(a, b))

@app.route('/sub')
def sub_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.sub(a, b))

@app.route('/mult')
def mult_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.mult(a, b))

@app.route('/div')
def div_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.div(a, b))

@app.route('/math/<op>')
def all_in_one(op):
    a = int(request.args['a'])
    b = int(request.args['b'])
    ops = {
        'add': operations.add(a, b),
        'sub': operations.sub(a, b),
        'mult': operations.mult(a, b),
        'div': operations.div(a, b)
    }
    return str(ops[op])