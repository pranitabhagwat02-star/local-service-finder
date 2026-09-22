from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to result portal"

@app.route('/result',methods=['GET','POST'])
def result():

    if request.method =="POST":

       name= request.form.get("name")  
       roll_no= request.form.get("roll_no")
       fsd= int(request.form.get("fsd")) 
       wad= int(request.form.get("wad"))
       cloud=int(request.form.get("cloud"))
       java= int(request.form.get("java"))

       total_marks =  fsd+wad+cloud+java
       percentage =(total_marks / 4 ) * 100

       if percentage >= 90:
           grade = "o"
       elif percentage >= 80:  
           grade = "A"
       elif percentage >= 70:  
           grade = "B"
       elif percentage >= 32:  
           grade = "C"
       else:
           grade = "f" 

       return f"""
              <h1>Student Result Details</h1>

              <p>Student Name :{name}</p>
              <p>Roll no :{roll_no}</p>
              <p>full stack development :{fsd}</p>
              <p>web development :{wad}</p>
              <p>cloud :{cloud}</p>
              <p>java :{java}</p>

              <p>Total of Marks :{total_marks}/400</p>
              <p>Percentage : {percentage}%/p> 
              <p>grade : {grade}</p>
            """

    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)