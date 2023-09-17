import lcu_driver
import requests

localhost = "http://localhost:5000/"

acceptator = requests.post((localhost + "accept/true"))
print(acceptator)