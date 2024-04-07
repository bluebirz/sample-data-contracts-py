import os
from flask import Flask, request, Response
from jsonschema import validate, ValidationError
import yaml
from pathlib import Path

app = Flask(__name__)

# prepare contract list
CONTRACTS = dict()
for contract_file in Path("./src/contracts").glob("*.yml"):
    contract_name = contract_file.name.replace(".yml", "")
    with open(contract_file) as fptr:
        contract_content = yaml.safe_load(fptr)
    CONTRACTS[contract_name] = contract_content


def generic_validate(contract_key: str, payload: dict) -> Response:
    try:
        target_contract = (
            CONTRACTS.get(contract_key, {})
            .get("components", {})
            .get("schemas", {})
            .get(contract_key)
        )
        validate(instance=payload, schema=target_contract)
        return Response(status=200)
    except ValidationError as ve:
        return Response(ve.message, status=400)
    except Exception as e:
        print(e)
        return Response(status=400)


@app.route("/pets", methods=["POST"])
def post_pets():
    return generic_validate(contract_key="pets", payload=request.get_json())


@app.route("/people", methods=["POST"])
def post_people():
    return generic_validate(contract_key="people", payload=request.get_json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4001)))
