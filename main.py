"""A simple API to track writing."""

from flask import Flask, request
from entry_functions import load_all_entries, is_valid_entry, save_new_entry

api = Flask(__name__)


@api.get("/")
def index():
    return {"message": "Welcome to the Writing App API"}


@api.route("/entry", methods=["GET", "POST"])
def get_or_create_entries():

    if request.method == "GET":
        entries = load_all_entries()
        args = request.args

        if "author" in args:
            author = args["author"]
            filtered_entries = []
            for entry in entries:
                if entry["author"].lower() == author.lower():
                    filtered_entries.append(entry)
            entries = filtered_entries

        return entries

    else:
        new_entry = request.json
        if is_valid_entry(new_entry):
            created_entry = save_new_entry(new_entry)
            return created_entry, 201
        else:
            return {"error": True, "message": "Invalid entry"}, 400


if __name__ == "__main__":

    api.run(port=8080, debug=True)
