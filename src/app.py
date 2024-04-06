import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/people", methods=["POST"])
def post_people():
    print(request.get_json())
    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4001)))
