import os

def delete_files():
	os.chdir(os.getcwd()+"\pics")
	teams = os.listdir(os.getcwd())
	for element in teams: #for each folder in the pics folder
		current_dir = os.getcwd()+"\\"+element
		files = os.listdir(current_dir)
		for f in files: #for each file in teams folder
			os.remove(current_dir+"\\\\"+f) #delete file




if __name__ == "__main__":
	delete_files()