# BloodDonationSystem 

BloodDonationSystem is a project intended to bridge the gap between the patients who are in dire need of blood and people willing to donate the blood. The patients can request for blood donation from anyone in the system and willing person can donate blood.
***

The system is developed using **Django Framework**.
The system implements `sqlite`. However, when it will be used in large scale, the system will use `postgress`
The system is hosted in `Google Cloud Platform`

Based on the procedure of installing and running **django** applications as it is in the [Documentation](https://docs.djangoproject.com/en/3.0/) here are the procedure do run the application in your device.

1. Clone the application from this repository to your device.
2. Ensure you have python installed in your device. You can check for python in your device by typing `python` or `python3` in your **terminal**  or **command prompt(CMD)**
3. If you have **python 2** or **python 3** installed in your device, ignore this step. If you dont, refer to the installation process by clicking here [Installing Python](https://www.python.org/downloads/) for Windows, Linux/Unix and MasOs
4. If you have pip installed in your device, skip this step. You can check whether you have **pip** installed in your device by typing **pip** in your **terminal** or **command prompt**. To install **pip**, follow the following guidelines [pip installation](https://pip.pypa.io/en/stable/installing/)
5. Enable the virtual environment by accessing the location you cloned the application and typing the following command in your terminal or command prompt: `virtualenv venv`. This will create a virtual enviromnent with the name `venv`.
6. Activate the virtual environment by typing `source venv/bin/activate` in your terminal.
7. Once activated, run the following command to install all the dependencies needed in the application `pip install -r requirements.txt`.
8. The application is configured to work with `sqlite` on the fly. However, you can change the database type using the following guidelines: [Django Database](https://docs.djangoproject.com/en/3.0/ref/databases/)

9.Run the command `python3 manage.py migrate` to create the tables in your database.

10. Run the command `python3 manage.py runserver` to run the application. Check in your browser by typing `127.0.0.1:8000`.


***

Hooray , the application is now running!!

To learn more on django, refer to the documentation [Django Documentation](https://docs.djangoproject.com/en/3.0/)
