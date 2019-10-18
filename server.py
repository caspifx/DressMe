from flask import Flask, request, escape, render_template, send_from_directory
import classes
import program

app = Flask(__name__)
program.init()
#program.main()
@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('DressMe-Home.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # get type of item
        item_type = request.form['item_type']
        item_name = request.form['item_name']
        color = request.form['favcolor']
        if item_type == 'shirt':
            top = classes.Top(color=color, id=item_name, formal=False, neck=False, plain=True, sleeve=False)
            program.add_top(top)
            if item_name == 'create':
                program.create_relationship()
        if item_type == 'pants':
            pant = classes.Pants()
        if item_type == 'shoes':
            shoes = classes.Shoes()

    elif request.method == 'GET':
        print request
    return render_template('SignUp.html')

@app.route('/gen-outfit', methods=['GET', 'POST'])
def send_outfit():
    print "Recived"
    return program.main()




if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
