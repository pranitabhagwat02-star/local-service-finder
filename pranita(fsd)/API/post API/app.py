from flask import Flask,request,jsonify
app = Flask(__name__)

students=[{"ID":101,"Name":"pranita bhagwat","r_no":1,"course":"BSC(IT)"},
          {"ID":102,"Name":"siya sharma","r_no":2,"course":"BSC(IT)"},
          {"ID":103,"Name":"pranita raoo","r_no":3,"course":"BSC(IT)"},
          {"ID":104,"Name":"nita patil","r_no":4,"course":"BSC(IT)"},
          {"ID":105,"Name":"janu singh","r_no":5,"course":"BSC(IT)"},
        
]

@app.route('/student',methods=['GET'])
def get_all_students():
    return jsonify(students)

@app.route('/student',methods=['POST'])
def student():
    data = request.get_json() 
    students.append(data)
    return jsonify(
        {
            "meg":"student data added succesfully","student":data
        }
        
    )
app.run(debug=True)