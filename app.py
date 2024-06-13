from flask import Flask, render_template, request, jsonify
import model

app = Flask(__name__)

@app.route('/')
def index():
    images_with_tags = model.fetch_images()
    return render_template('index.html', images_with_tags=images_with_tags)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    chosen_tag = data['tag']
    reward = data['reward']
    model.update_model(chosen_tag, reward)
    return jsonify(success=True)

@app.route('/refresh', methods=['POST'])
def refresh():
    images_with_tags = model.fetch_images()
    images = [img for img, tag in images_with_tags]
    tags = [tag for img, tag in images_with_tags]
    return jsonify(images=images, tags=tags)

if __name__ == '__main__':
    app.run(debug=True)
