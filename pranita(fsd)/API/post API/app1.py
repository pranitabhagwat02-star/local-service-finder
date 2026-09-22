from flask import Flask,request,jsonify
app=Flask(__name__)
movies=[{"id":1,"Name":"cocktail","category":"romantic"},
    {"id":2,"Name":"saiyara","category":"romantic"},
    {"id":3,"Name":"dhurandhar","category":"action"},
    {"id":4,"Name":"mirzapur","category":"action"},
    {"id":5,"Name":"shiddat","category":"romantic"},
    
]
@app.route("/movie",methods=['GET'])
def get_all_movies():
    return jsonify(movies)

@app.route("/movie",methods=['POST'])
def movie():
    data=request.get_json()
    movies.append(data)
    
    return jsonify({
         "meg":"movie data added succesfully",
         "movie":data
                
    }
        
    )
app.run(debug=True)
    

    