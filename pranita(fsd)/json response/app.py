from flask import Flask ,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    student1={
        "name":"pranita bhagwat",
        "age":20,
        "rno":101,
        "course":"BSC.(IT)",
        "year": 2026,
        "marks":8.55,
    },
    student2={
        "name":"sonu kale ",
        "age":20,
        "rno":102,
        "course":"BSC.(IT)",
        "year": 2026,
        "marks":8.00,
    },
    student3={
        "name":"manu bhor",
        "age":20,
        "rno":103,
        "course":"BSC.(IT)",
        "year": 2026,
        "marks":8.20,
    },
    student4={
        "name":"riya patil",
        "age":21,
        "rno":104,
        "course":"BSC.(IT)",
        "year": 2026,
        "marks":8.26,
    },
    student5={
        "name":"diksha aher",
        "age":21,
        "rno":105,
        "course":"BSC.(IT)",
        "year": 2026,
        "marks":8.00,
    }
 
    return jsonify(student1,student2,student3,student4,student5)
if __name__ == "__main__":
    app.run(debug=True)
