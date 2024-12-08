import os

# Returns the current working directory
print(os.getcwd())

# List files in the current directory
files = os.listdir('c:\\Users\\gakad\\PycharmProjects\\Python_Automation-Selenium_-_API-Automation-Project_Class_Practice')
print(f"Files in current directory: {files}")

# # Create a new directory
# os.mkdir('Test2')

# Check if a file exists
file_exist = os.path.exists("TestData.txt")
print(file_exist)


print(os.name) # posix == mac, nt - windows