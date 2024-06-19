import json
param_string = input(">>>")
data_dict = {item.split('=')【0】: item.split('=')【1】 for item in param_string.split('&')}
data_string = json.dumps(data_dict, indent=4)
print(data_string)
with open("output.txt", mode="w") as f:
    f.write(data_string)