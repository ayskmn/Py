r from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] =  "secretKey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def survey_start_home():
    """Select a survey"""
    return render_template("survey_start.html", survey=survey)



@app.route("/begin", methods=["POST"])
def start_survey():

    session[responses_key] = []
    return redirect("/questions/0")



@app.route("/answer", methods=["POST"])
def handle_question():
    choice = request.form['answer']
"""Handle and save response and redirect to the next question"""
    # add this response to the session
    responses = session[responses_key]
    responses.append(choice)
    session[responses_key] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    
    else:
        return redirect("/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def show_question(qid):
    responses = session.get(responses_key)

    if(responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")

    if(len(responses == !qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}") 

@app.route("/complete")
def complete():
    return render_template("completion.html")