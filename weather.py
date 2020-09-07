from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Learn how to message')
root.geometry("1280x720")


# try:
api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode"
                               "=89129&distance=25&API_KEY=BB55AB9F-C3A9-4C6A-8A5A-F4F55C332CCB")
api = json.loads(api_request.content)
# except Exception as e:
#     api = "Error"

mylabel = Label(root, text=api)
mylabel.pack()
root.mainloop()