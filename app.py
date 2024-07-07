from flask import*
from pickle import*
import os

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def home():
	if request.method == "POST":
		fn = "cc.pkl"
		if os.path.exists(fn):
			f = open(fn,"rb")
			model = load(f)
			f.close()
		home = float(request.form["distance_from_home"])
		last_transaction = float(request.form["distance_from_last_transaction"])		
		purchase_price= float(request.form["ratio_to_median_purchase_price"])
		repeat = float(request.form["repeat_retailer"])
		chip = float(request.form["used_chip"])
		pin_number = float(request.form["used_pin_number"])
		online_order = float(request.form["online_order"])
		d = [[home, last_transaction, purchase_price,repeat,chip,pin_number,online_order]]
		res = model.predict(d)
		if res == 0:
			msg = "Normal Transaction"
		else :
			msg = "Fraud Transaction"


		return render_template("home.html",msg = msg)
	else:
		return render_template("home.html")		
	
			
if __name__ == "__main__":
    app.run(debug=True, use_reloader = True)
