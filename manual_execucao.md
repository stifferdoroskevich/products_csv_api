## How to run project locally
```
FIRST
docker pull mongo:4.4.6

docker run -d --name mongo_local -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=eiprice -e MONGO_INITDB_ROOT_PASSWORD=contratado mongo:4.4.6

docker start mongo_local


SECOND
git clone https://github.com/stifferdoroskevich/products_csv_api.git
cd products_csv_api
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py init_db
python3 server.py
```


## Verification of Data:
* URL: 127.0.0.1:5000/stores
* Should return 84 rows 