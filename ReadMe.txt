## Open CMD With Sudo Power # First Time virtualenv will not run
set-executionpolicy remotesigned # Run this command


Step 1:- pip install virtualenv # To install virtualenv
Step 2:- virtualenv OpenCvEnv # Create virtualenv
Or 
Step 3:- virtualenv --system-site-packages OpenCvEnv # Create OpenCvEnv with all system packages
Step 4:- .\OpenCvEnv\Scripts\activate # Activate virtualenv

## OpenCvEnv\Scripts\python.exe # Set this virtualenv in your ide

deactivate # for deactivate virtualenv




pip install opencv-python
pip install mediapipe



pip freeze > requirements.txt # To make requirements.txt file
pip install -r .\requirements.txt # To install all liberry from requirements.txt file

deactivate # for deactivate virtualenv

