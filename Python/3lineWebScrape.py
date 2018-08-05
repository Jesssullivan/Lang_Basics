import requests
result = requests.get("https://github.com/Jesssullivan/Lang_Basics)
print("show results:github")
print(result.status_code)
print("show results:headers")
print(result.headers)


