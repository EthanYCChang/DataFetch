import urllib.request as request
src = "https://pda.5284.gov.taipei/MQS/route.jsp?rid=10873"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")
print(data)
