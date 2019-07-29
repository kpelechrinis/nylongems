from flask import Flask, render_template, Response, request, redirect, url_for
import os
import base64
import fnmatch
import random
import datetime
import sys

TEMPLATE_DIR = os.path.abspath('/home/nylongems/mysite/templates')
STATIC_DIR = os.path.abspath('/home/nylongems/mysite/static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/",methods=['GET', 'POST'])
def index():
    now = datetime.datetime.now()
    fout = now.strftime("%Y-%m-%d!%H:%M")+"!"+str(random.randint(0, sys.maxsize))
    images = [f for f in fnmatch.filter(os.listdir('/home/nylongems/mysite/static/img/'), '*.png')]
    comp = random.sample(images,2)
    im1 = open("/home/nylongems/mysite/static/img/"+str(comp[0]),"rb")
    im1_str = base64.b64encode(im1.read()).decode('ascii')
    im2 = open("/home/nylongems/mysite/static/img/"+str(comp[1]),"rb")
    im2_str = base64.b64encode(im2.read()).decode('ascii')
    competitors = fout+"::"+str(comp[0])+"-"+str(comp[1])
    fresults = open("/home/nylongems/mysite/results.txt","a")
    fresults.write(competitors+"\n")
    fresults.close()
    return render_template('index.html', image1 = im1_str, image2 = im2_str, v1=fout+"!A",v2=fout+"!B")

@app.route("/forwardA/", methods=['POST'])
def forwardA():
    fresults = open("/home/nylongems/mysite/results.txt","a")
    fresults.write(str(request.form['net'])+"\n")
    fresults.close()
    now = datetime.datetime.now()
    fout = now.strftime("%Y-%m-%d!%H:%M")+"!"+str(random.randint(0, sys.maxsize))
    images = [f for f in fnmatch.filter(os.listdir('/home/nylongems/mysite/static/img/'), '*.png')]
    comp = random.sample(images,2)
    im1 = open("/home/nylongems/mysite/static/img/"+str(comp[0]),"rb")
    im1_str = base64.b64encode(im1.read()).decode('ascii')
    im2 = open("/home/nylongems/mysite/static/img/"+str(comp[1]),"rb")
    im2_str = base64.b64encode(im2.read()).decode('ascii')
    competitors = fout+"::"+str(comp[0])+"-"+str(comp[1])
    fresults = open("/home/nylongems/mysite/results.txt","a")
    fresults.write(competitors+"\n")
    fresults.close()
    return render_template('index.html', image1 = im1_str, image2 = im2_str,v1=fout+"!A",v2=fout+"!B");

if __name__ == '__main__':
	app.run(threaded=True,debug = True)
