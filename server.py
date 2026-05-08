from flask import Flask, jsonify

import requests

from config import (
    SUPABASE_URL,
    SUPABASE_HEADERS
)

app = Flask(__name__)


# =========================================================
# GET BTS DATA BY SDCA
# =========================================================

@app.route("/get_bts/<sdca>")
def get_bts_by_sdca(sdca):

    try:

        url = (
            f"{SUPABASE_URL}"
            f"/rest/v1/bts_data"
            f"?sdca=eq.{sdca}"
        )

        response = requests.get(
            url,
            headers=SUPABASE_HEADERS
        )

        data = response.json()

        return jsonify(data)

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        })





# =========================================================
# GET COMPLETE MASTER DATA
# =========================================================

@app.route("/get_master_data")
def get_master_data():

    try:

        url = (
            f"{SUPABASE_URL}"
            f"/rest/v1/master_data"
        )

        response = requests.get(
            url,
            headers=SUPABASE_HEADERS
        )

        data = response.json()

        return jsonify(data)

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        })



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