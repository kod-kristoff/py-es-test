import json
import os

import urllib3


PORT = os.environ.get("ES_PORT", 9200)


def main():
    http = urllib3.PoolManager()
    r = http.request("GET", f"elasticsearch:{PORT}")
    assert r.status == 200
    data = json.loads(r.data.decode("utf-8"))
    print(f"data = {data}")

if __name__ == "__main__":
    main()
