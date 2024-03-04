filename = input("File name: ").lower()

sufix = filename.split(".")[1]

if sufix == "gif":
    print("image/gif")
elif sufix == "jpg":
    print("image/jpeg")
elif sufix == "jpeg":
    print("image/jpeg")
elif sufix == "png":
    print("image/png")
elif sufix == "pdf":
    print("application/pdf")
elif sufix == "txt":
    print("application/txt")
elif sufix == "zip":
    print("application/zip")
else:
    print("application/octet-stream")





