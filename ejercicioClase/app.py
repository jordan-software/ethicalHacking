from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

vulnerabilities = list()

vulnerabilities.append({"id": 1, "title": "SQL Injection", "owasp_category": "A03", "severity": "High"})
vulnerabilities.append({"id": 2, "title": "Cross-Site Scripting", "owasp_category": "A03", "severity": "Medium"})
vulnerabilities.append({"id": 3, "title": "Broken Access Control", "owasp_category": "A01", "severity": "High"})

@app.route("/")
def index():
    return render_template("vulnerabilities.html", vulnerabilities=vulnerabilities)


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        title = request.form["title"]
        owasp_category = request.form["owasp_category"]
        severity = request.form["severity"]

        nuevo_id = len(vulnerabilities) + 1

        vulnerabilities.append({
            "id": nuevo_id,
            "title": title,
            "owasp_category": owasp_category,
            "severity": severity
        })

        return redirect(url_for("index"))

    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)