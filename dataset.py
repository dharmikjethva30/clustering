import requests
import tarfile

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/reuters21578-mld/reuters21578.tar.gz"
response = requests.get(url, stream=True)
with open("reuters21578.tar.gz", "wb") as tar_file:
    for data in response.iter_content(chunk_size=128):
        tar_file.write(data)

with tarfile.open("reuters21578.tar.gz", "r:gz") as tar:
    tar.extractall()
