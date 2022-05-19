import pyqrcode
import png
myupi="8384050751286@paytm"
img=pyqrcode.create(myupi)
img.png("UPI.png",scale=8)