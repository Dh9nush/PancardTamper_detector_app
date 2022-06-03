
from flask import Flask, render_template,request
from skimage.metrics import structural_similarity
from PIL import Image
import cv2

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def Check():
    if request.method=='GET':
        return render_template('home.html')
    
    if request.method=='POST':
        file_upload=request.files['file_upload']
        filename=file_upload.filename
        original1=Image.open('static/original.png')
        original1=original1.resize((250,160))
        original1=cv2.imread('static/original.png')
        original_gray=cv2.cvtColor(original1,cv2.COLOR_BGR2GRAY)
        
        tampered=Image.open(file_upload)
        tampered1=tampered.resize((250,160))
        tampered1=tampered1.save('static/tampered.png')
        tampered1=cv2.imread('static/tampered.png')
        tampered_gray=cv2.cvtColor(tampered1,cv2.COLOR_BGR2GRAY)
        

        
        (score,diff)=structural_similarity(original_gray,tampered_gray,full=True)
        value=(score*100).astype(int8)
        
        return render_template('home.html',value='SSIM value is ' + str(value)+'%'+'is Similar')
    



if __name__=='__main__':
    app.run(debug=True)
