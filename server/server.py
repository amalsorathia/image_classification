from flask import Flask, request, jsonify
# import python_utils
import util

app = Flask(__name__)

#using saved model in artifacts directory we will classify image
@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run(port=9874)


