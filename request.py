import requests
url = "https://prod18.centralindia.logic.azure.com/workflows/d1dfef5cd2b54103b67a989eab024704/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=ZRSj02or46cAlXseGsDU4VGUd6KqqXqe_U4R_W9Dxhw"
with open('code.py', 'rb') as f:
    payload = f.read()
headers = {
  'Name': 'Nipun Gupta',
  'Email': 'nipun.gupta2017@vitstudent.ac.in',
  'College': 'VIT, Vellore',
  'StudentId': '17BCE0249',
  'FileName': 'code.py',
  'Content-Type': 'application/octet-stream'
}

response = requests.request("PUT", url, headers=headers, data = payload)

print(response.text.encode('utf8'))