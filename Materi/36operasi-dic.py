# OPERASI DICTIONARY

data_dict = {
    "Er":"Erika",
    "Ell":"Ellinor",
    "rarr":"rariru",
}

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary: {lendict}")

# mengecek key exist atau tidak
key = "rarr"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["Er"])
print(data_dict.get("Er"))
print(data_dict.get("kis","key tidak ditemukan"))

# mengupdate data
data_dict["Ell"] = "Ester" 
print(data_dict)
data_dict["rarr"] = "rarirureroy"
print(data_dict)

data_dict.update({"Er":"Erika af"})
print(data_dict)
data_dict.update({"new":"new dictionary"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["new"]
print(data_dict)

