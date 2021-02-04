from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    print(myzip.namelist())
    myzip.printdir()
