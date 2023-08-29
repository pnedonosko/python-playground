from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello it's the server root :)"

@app.route("/datasets/<filename>", methods=["GET"])
def get_dataset(filename):
    # TODO read from datasets folder more safely (use send_from_directory)
    return send_file(
        "../datasets/" + filename,
        as_attachment=True,
        download_name=filename,
        mimetype="text/plain")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found</p>", 404

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9180, debug=True)