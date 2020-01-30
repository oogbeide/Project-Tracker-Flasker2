"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student.
    Receives info from /student-search"""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html", 
                           first=first, 
                           last=last,
                           github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/student-add-form", methods=['GET'])
def show_student_add_form():

    return render_template("new_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    github = request.form.get('git_hub')
    
    hackbright.make_new_student(first_name, last_name, github)

    return render_template("successful_added.html", 
                           f_name=first_name,
                           l_name=last_name)


# @app.route("/student-info")
# def show_student_info():
#     first_name, last_name, github = hackbright.get_student_by_github()
#     return render_template("student_info.html")

# @app.route("/")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")