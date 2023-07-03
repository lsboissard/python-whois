from flask import Flask, make_response, jsonify, request
import whois

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_domain():
    domain = request.args.get('domain')
    return make_response(
        jsonify(whois.whois(domain))
    )


if __name__ == '__main__':
    app.run()
