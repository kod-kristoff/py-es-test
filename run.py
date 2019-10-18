import json
import os

import urllib3


ES_HOST = os.environ["ELASTICSEARCH_HOST"]
ES_PORT = os.environ["ELASTICSEARCH_PORT"]


def main():
    http = urllib3.PoolManager()
    r = http.request("GET", f"http://{ES_HOST}:{ES_PORT}")
    assert r.status == 200
    data = json.loads(r.data.decode("utf-8"))
    print(f"data = {data}")

if __name__ == "__main__":
    main()
