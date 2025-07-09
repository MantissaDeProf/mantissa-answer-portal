from flask import Flask, render_template, request

app = Flask(__name__)

answers = {
    "1a": "Health surveillance involves ongoing health checks for employees exposed to workplace risks...",
    "1b": "Effective systems include reporting structure, documentation, root cause analysis...",
    "2a": "Risk identification involves recognizing hazards through observation, records, consultation...",
    "2b": "It quantifies the likelihood and impact of risks...",
    "2c": "Chronic lung disease from inhaling silica dust; common in mining...",
    "2d": "Lung scarring from asbestos exposure...",
    "3a": "Infections acquired at work, such as TB or hepatitis...",
    "3b": "Evaluates fitness for duty post-illness...",
    "3c": "Includes tracking, interviews, digital tools...",
    "4a": "Concerns include confidentiality, discrimination, legal rights...",
    "4b": "Head: stabilize, control bleeding. Eye: rinse, avoid rubbing..."
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected = None
    answer = None
    if request.method == "POST":
        selected = request.form.get("question")
        answer = answers.get(selected, "Answer not found.")
    return render_template("index.html", selected=selected, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
