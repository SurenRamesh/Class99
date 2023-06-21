import os, shutil

# source = input("Choose a source folder: ")
# destination = input("Choose the destination: ")
# source = source + "/"
# destination = destination + "/"
# storage = os.listdir(source)
#----------------------COPY THE FILES---------------------------------------
# for I in storage:
#     shutil.copy((source + I), destination)

#----------------------MOVE THE FILES---------------------------------------
# for I in storage:
#     shutil.move((source + I), destination)

#----------------------ORGANIZE THE FILES---------------------------------------
Organisation = input("Enter the folder name that needs to be sorted: ")
storage = os.listdir(Organisation)
for D in storage:
    name , ext =os.path.splitext(D)
    ext = ext[1:] # .txt, .js , .png , .py
    if ext == "":
        continue
    if os.path.exists(Organisation + "/" + ext):
        shutil.move((Organisation + "/" + ext), (Organisation + "/" + ext + "/" + D))
    else:
        os.makedirs(Organisation + "/" + ext)
        shutil.move((Organisation + "/" + ext), (Organisation + "/" + ext + "/" + D))
        