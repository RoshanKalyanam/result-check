"""
Flask application for the Result-Check website.
Provides a web interface and REST API to look up student exam results.
"""

from flask import Flask, render_template, request, jsonify
from results import calculate_result, STUDENT_RESULTS

app = Flask(__name__)


@app.route("/")
def index():
    """Render the homepage with the search form."""
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    """Handle form submission and display the result page."""
    roll_number = request.form.get("roll_number", "").strip().upper()
    result_data = calculate_result(roll_number)
    if result_data is None:
        return render_template("index.html", error=f"No record found for {roll_number}")
    return render_template("result.html", result=result_data)


@app.route("/api/result/<roll_number>")
def api_result(roll_number):
    """REST API endpoint that returns result as JSON."""
    result_data = calculate_result(roll_number.strip().upper())
    if result_data is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(result_data)


@app.route("/health")
def health():
    """Health-check endpoint for container orchestration."""
    return jsonify({"status": "healthy", "students_loaded": len(STUDENT_RESULTS)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

