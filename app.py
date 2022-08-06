import flask
import pandas as pd
import numpy as np
import utils 
from flask import Flask, Blueprint,render_template,request

tourismapp = Blueprint('tourismapp', __name__)

@tourismapp.route('/',methods=['GET','POST'])
def tourismRecommendationSystem():
    
        
    data = pd.read_excel("static/proj_data.xlsx")
    states = utils.getStates(data)
    labels = utils.getLabels(data)
    print(labels)
    weathers = utils.getWeathers(data)
    data = utils.createRecreation(data)
    recreations = utils.getRecreations(data)
    if request.method == "POST":
        user_state=request.form["state"]
        user_label=request.form["label"]
        user_recreation=request.form["recreation"]
        user_weather=request.form["weather"]
        user_budget=request.form["budget"]
        print(user_state)
        if(user_budget==1):
            data=data[data["Food Costs"]<=850]
        

        spots=utils.getSpots(data,user_state,user_label,user_recreation,user_weather,user_budget)
        return render_template("index.html",states=states,labels=labels,weathers=weathers,recreations=recreations,similar_spots = spots,visible="")
    return render_template("index.html",states=states,labels=labels,weathers=weathers,recreations=recreations,visible="invisible")
    

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(tourismapp, url_prefix='/')

    app.run(debug=True)