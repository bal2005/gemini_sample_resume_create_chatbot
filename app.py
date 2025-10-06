
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database" for messages
messages = {
    "hr": [],
    "employee": []
}

@app.route("/")
def index():
    return redirect(url_for("hr"))

@app.route("/hr", methods=["GET", "POST"])
def hr():
    if request.method == "POST":
        message = request.form["message"]
        messages["hr"].append(("hr", message))
        messages["employee"].append(("hr", message))
    return render_template("hr.html", messages=messages["hr"])

@app.route("/employee", methods=["GET", "POST"])
def employee():
    if request.method == "POST":
        message = request.form["message"]
        messages["employee"].append(("employee", message))
        messages["hr"].append(("employee", message))
    return render_template("employee.html", messages=messages["employee"])

if __name__ == "__main__":
    app.run(debug=True)
