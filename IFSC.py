import requests #importing required module

IFSC_Code =input("Enter ifsc code")
URL = "https://ifsc.razorpay.com/"
#Enter Dersired IFSC Code

ifscinfo = requests.get(URL+IFSC_Code).json()
#Using get() method to retrieve information from razorpay server.

print(ifscinfo)
#printing the Output i.e.,Branch Location,Bank details,Address of the Branch,whether UPI or IMPS is there or not
