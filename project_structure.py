# pip install cookiecutter
# cookiecutter -c v1 https://github.com/jesussantana/cookiecutter-data-science
# or create folders recursively

import os

src = ['preparation' ,'procesing', 'modeling']
test = ['test']
model = ['model']
data = ['raw', 'processed']
notebook = ['eda', 'poc', 'modeling', 'evaluation']

main_dir = [src, test, model, data, notebook]
root_dir = 'Master'
main_dir_names = ['src', 'test', 'model', 'data','notebook']

def main():
# Create directory
	for i in range(0, len(main_dir)):
	    for j in range(0,len(main_dir[i])):
		    dirName = str(root_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])
		    
		    try:
		        # Create target Directory
		        os.makedirs(dirName)
		        print("Directory " , dirName ,  " Created ") 
		    except FileExistsError:
		        print("Directory " , dirName ,  " already exists")        
		    
		    # Create target Directory if don't exist
		    if not os.path.exists(dirName):
		        os.makedirs(dirName)
		        print("Directory " , dirName ,  " Created ")
		    else:    
		        print("Directory " , dirName ,  " already exists")  
         
if __name__ == '__main__':
    main()