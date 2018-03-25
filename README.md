## Setup

Follow the below steps to setup the project: 

1) Install project dependencies by executing command `pip install -r requirements.txt` from the project root. 

The project is now ready to use. To run existing tests, read the below section on **Testing**

## Testing

The tests for this project are located in the `vibration_device_tests.py` file. The tests are run using the `nosetests` command that is available after installing the requirements in `requirements.txt`.  To run the tests, type `nosetests` in the terminal at the project root. Note that if you are running the application in a virtualenv `nosetests` will instead be installed in the bin/ folder of the virtual environment meaning you will instead have to type the path to that executable to run the tests. 
