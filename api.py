from flask import Flask, request as req, jsonify
from openai import OpenAI
import logging
import os

app = Flask(__name__)


def query(payload, model_id, api_token):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_token,
    )

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
                "role": "user",
                "content": payload["input"],
            }
        ],
        extra_body={"reasoning": {"enabled": True}},
    )

    return response


@app.route("/chat", methods=["GET"])
def call_openrouter_chat_model():
    model_id = req.args.get("model_id")
    logging.debug(f"The model ID for the openrouter model is {model_id}")
    openrouter_token = req.args.get("openrouter_token")
    logging.debug(f"openrouter API Token: {openrouter_token}")
    questions = req.args.get("input")
    data = query(
        {"input": f"{questions}"},
        model_id,
        openrouter_token,
    )
    logging.debug(f"Model output: {data}")
    output = jsonify({"ack": data.choices[0].message.content})
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output


@app.route("/ping", methods=["GET"])
def ping():
    output = jsonify({"ack": "pong"})
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host="0.0.0.0", port=port)
