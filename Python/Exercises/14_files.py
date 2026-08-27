txt_data = "Hello World"

file_path = "C:/Users/DELL/Desktop/RoadMap/Python/Exercises/file.txt"

# "w" - create & write "r" - read "a" - append "x - create & write if not exist"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Text File {file_path} was created.")

with open(file_path, "r") as file:
    file_data = file.read()
    print(f"File contains : {file_data}")
