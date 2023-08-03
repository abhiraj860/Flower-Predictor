import model
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__,template_folder="templates")
@app.route('/')
def home1():
    return render_template('home.html') # Render home.html

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html') # Render home.html


@app.route('/classify',methods=['GET'])
def classify_type():
    try:
        sepal_len = request.args.get('slen') # Get parameters for sepal length
        sepal_wid = request.args.get('swid') # Get parameters for sepal width
        petal_len = request.args.get('plen') # Get parameters for petal length
        petal_wid = request.args.get('pwid') # Get parameters for petal width

        # Get the output from the classification model
        variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)
        # print("I am here", sepal_len, sepal_wid, petal_len, petal_wid)
        # Render the output in new HTML page
        return render_template('output.html', variety=variety)
    except:
        return 'Error Hello'
    
# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)