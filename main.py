from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('rental_listing.pkl','rb'))

app =Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('rentallisting.html')

@app.route('/predict',methods=['POST'])
def predict():
    longitude= request.form.get('longitude')
    latitude= request.form.get('latitude')
    bathroom= request.form.get('bathroom')
    bedroom= request.form.get('bedroom')
    price= request.form.get('price')
    year= request.form.get('year')
    months= request.form.get('months')
    week_date= request.form.get('week_date')
    res1=np.array([[float(longitude),float(latitude),float(bathroom),float(bedroom),float(price),float(year),float(months),float(week_date)]])

    res= model.predict(res1)
    if res[0]== 0 :
        res = "Low"
    elif res[0] == 1:
        res="Medium"
    else:
        res="High"

    return render_template("index.html",res=res)

if __name__=="__main__":
    app.run(debug=True)


