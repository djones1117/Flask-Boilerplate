## Setup

1. Clone the Repo!

2. Move the make_virtual_env.py file to the desktop folder

3. Create and Activate a python virtual env by going into the desktop folder using ```cd Desktop``` once in the desktop folder run ```python3 make_virtual_env.py```

4. Select your python version and the name of the virtualenv. Copy and paste the final command that you see printed in your terminal. The virtualenv will now be activated. CD back into your projects root folder.

5. (If you have multiple branches do this. If not you can ignore this step.) 
If you're gonna be working with multiple branches - run ```git checkout main```
then pull down the changes by running ```git pull origin main``` once you've pulled down the latest changes run ```git checkout -b branchName``` to create a new branch off of main. branchName can be replaced with the name of your choice. 

6. Run ```pip install -r requirements.txt``` on the command line

7. Run ```python3 main.py``` to start the app!

8. Once you are ready to push the changes you've made run ```pip freeze > requirements.txt```

9. (if you are working with mutliple branches only) Open a pull request and merge the changes into the main branch. Deactivate your virtual env. Start back at step 3. 

10. Happy Hacking!!!