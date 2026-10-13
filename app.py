from flask import Flask, make_response, jsonify, request

app = Flask(__name__)




@app.route("/", methods=["GET"])
def index():
    return make_response("<h1>Welcome to Flask</h1>", 200)


@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    return make_response(jsonify(businesses), 200)


# fetch by ID
@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["GET"])
def show_one_businesses(biz_id):
    data_to_return = [business for business in businesses
                      if business["id"] == biz_id]

    return make_response(jsonify(data_to_return[0]), 200)

# post method to add new business
@app.route("/api/v1.0/businesses", methods=["POST"])
def add_business():
    next_id = businesses[-1]["id"] + 1

    new_business = {
        "id": next_id,
        "name": request.form["name"],
        "town": request.form["town"],
        "rating": request.form["rating"],
        "reviews": []
    }

    businesses.append(new_business)

    return make_response(jsonify(new_business), 201)

# put method to modify existing record
@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["PUT"])
def edit_business(biz_id):
    for business in businesses:
        if business["id"] == biz_id:
            business["name"] = request.form["name"]
            business["town"] = request.form["town"]
            business["rating"] = request.form["rating"]
            break

    return make_response(jsonify(business), 200)

# delete method    
@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["DELETE"])
def delete_business(biz_id):
    for business in businesses:
        if business["id"] == biz_id:
            businesses.remove(business)
            

    return make_response(jsonify({"message": "Business removed successfully"}), 200)
            


if __name__ == "__main__":
    app.run(debug=True, port = 5001)
