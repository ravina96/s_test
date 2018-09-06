from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def load_main():
    return render_template("index.html")

@app.route("/endometriosis")
def endometriosis():
	return render_template("endometriosis.html")

@app.route("/spirit")
def spirit():
	return render_template("spirit.html")

if(__name__=="__main__"):
    app.run()





