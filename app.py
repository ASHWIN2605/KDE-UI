from flask import Flask, render_template, request, redirect, url_for, session

import conversion as co

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST'])
def hello():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return {'lat':lat,'long':lon}
    #return render_template("login-page.html")

@app.route('/hello',methods=['POST'])
def hela():
    
    req = request.form
    longi=req.get('longitude')
    lat=req.get('latitude')
    con_lat,con_long=co.reproject_wgs_to_itm(lat,longi)
    return render_template("lat-page.html",lat=con_lat,lon=con_long)


if __name__ == '__main__':
    app.run()
