

class File_Handler:
    def __init__(self, file):
        with open('static/'+str(file), 'wb+') as destination:
            print("find file!")
            print(file)
            for chunk in file.chunks():
                destination.write(chunk)
