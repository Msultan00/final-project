from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        # Get the expression from the form
        expression = request.form.get("expression")
        try:
            # Evaluate the expression
            result = eval(expression)
            return render_template("calculator.html", result=result, expression=expression)
        except Exception as e:
            # Handle invalid expressions
            error_message = "Invalid expression: " + str(e)
            return render_template("calculator.html", error_message=error_message)
    else:
        return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)
