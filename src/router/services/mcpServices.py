import json

def mcpJson(data:object)->bool:
    print("mcpJson {1}" , data)
    with open('../src/data.json',"w") as f:
        json.dump(data , f , indent=4)
        status = True
        return status