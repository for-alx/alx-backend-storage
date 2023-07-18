#!/usr/bin/env python3
"""
returns all students sorted by average score:
"""
from pymongo import MongoClient


if __name__ == "__main__":
    connection = MongoClient("mongodb://127.0.0.1:27017")
    nginx = connection.logs.nginx
    logs = nginx.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    stats = nginx.count_documents({"path": "/status"})
    print(f"{stats} status check")
    print("IPs:")
    ip_add = nginx.aggregate(
        [
            {"$group": {"_id": "$ip", "sum": {"$sum": 1}}},
            {"$sort": {"sum": -1}},
            {"$limit": 10},
        ]
    )
    for ip in ip_add:
        sum = ip["sum"]
        ip = ip["_id"]
        print(f"\t{ip}: {sum}")
