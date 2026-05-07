from flask import Flask, jsonify

import requests

from config import (
    SUPABASE_URL,
    SUPABASE_HEADERS
)

app = Flask(__name__)


# ---------------- GET BA ----------------

@app.route("/get_ba")

def get_ba():

    url = f"{SUPABASE_URL}/rest/v1/ba"

    response = requests.get(
        url,
        headers=SUPABASE_HEADERS
    )

    data = response.json()

    return jsonify(data)


# ---------------- GET OA ----------------

@app.route("/get_oa/<int:ba_id>")

def get_oa(ba_id):

    url = (
        f"{SUPABASE_URL}/rest/v1/oa"
        f"?ba_id=eq.{ba_id}"
    )

    response = requests.get(
        url,
        headers=SUPABASE_HEADERS
    )

    data = response.json()

    return jsonify(data)


# ---------------- GET SDCA ----------------

@app.route("/get_sdca/<int:oa_id>")

def get_sdca(oa_id):

    url = (
        f"{SUPABASE_URL}/rest/v1/sdca"
        f"?oa_id=eq.{oa_id}"
    )

    response = requests.get(
        url,
        headers=SUPABASE_HEADERS
    )

    data = response.json()

    return jsonify(data)


# ---------------- HOME ----------------

@app.route("/")

def home():

    return jsonify({
        "message": "BTS API Running"
    })


# ---------------- START SERVER ----------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )