from flask import Flask ,jsonify

app = Flask(__name__)

students=[{"name":"pranita bahgwat","age":20,"ID":101,"course":"BSC.(IT)","year": 2026,"marks":8.55,},
         {"name":"siya sharma","age":20,"ID":102,"course":"BSC.(IT)","year": 2026,"marks":8.00,},
         {"name":"ravi sharma","age":20,"ID":103,"course":"BSC.(IT)","year": 2026,"marks":8.20,},
         {"name":"sharu mane","age":21,"ID":104,"course":"BSC.(IT)","year": 2026,"marks":8.26,},
         {"name":"neha varpe","age":21,"ID":105,"course":"BSC.(IT)","year": 2026,"marks":8.00,}]


@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)

@app.route('/students/<int:ID>', methods=['GET'])
def get_student(ID):
    
    for student in students:
        if student["ID"] == ID:
            return jsonify(student)

    return jsonify({"msg":'students not found'}),404
if __name__ == "__main__":
    app.run(debug=True)
    






