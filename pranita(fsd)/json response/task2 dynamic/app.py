from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():

    student={

    "Name":"Pranita Bhagwat",
    "Age":21,
    "Roll_no":13,
    "Course":"BSC(IT)",
    "Year":"TY"

    }

    student1={

    "Name":"prita arora",
    "Age":21,
    "Roll_no":12,
    "Course":"BSC(IT)",
    "Year":"TY"

}

    return render_template("index.html",student=student,student1=student1)
app.run(debug=True)