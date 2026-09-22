from flask import Flask,jsonify
app= Flask(__name__)

Movies=[
    {"id":1,"Name":"cocktail","category":"romantic"},
    {"id":2,"Name":"saiyara","category":"romantic"},
    {"id":3,"Name":"dhurandhar","category":"action"},
    {"id":4,"Name":"mirzapur","category":"action"},
    {"id":5,"Name":"shiddat","category":"romantic"},
    ]

@app.route("/Movies",methods=["GET"])
def get_all_movies():
    return jsonify(Movies)

@app.route("/Movies/<int:id>",methods=["GET"])
def get_by_id(id):
    for Movie in Movies:
        if Movie ["id"] == id:
            return jsonify(Movie)
        
    return jsonify({"msg":"movies are not found"}),404

@app.route("/Movies/Name/<string:Name>",methods=["GET"])
def get_by_name(Name):
    for Movie in Movies:
            if Movie ["Name"] == Name:
                return jsonify(Movie)
            
    return jsonify({"msg":"movies are not found"}),404

@app.route("/Movies/category/<string:category>",methods=["GET"])
def get_movie_category(category):
    r=[]
    for Movie in Movies:
        if Movie ["category"] == category:
            r.append(Movie)
            print(r)
    return jsonify(r)
        
    
    
    
if __name__=='__main__':
        app.run(debug=True)


    