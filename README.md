# My Project

This is a Python project that does something cool.

## Installation

1. Clone the repository:
```
git clone https://github.com/carlitos-206/robinhood_interface.git
```

2. Navigate to the root directory of the project:

```
cd robinhood_interface.git
```

3. Create a virtual environment (optional but recommended):

```
python -m venv venv
``` 
Unix/Linux
```
source venv/bin/activate
```
Windows
```
call venv\Scripts\activate
```

GitBash
```
source venv/Scripts/Activate
```

Creating a virtual environment is recommended to avoid conflicts with other Python projects on your system.

4. Install the dependencies:

```
pip install -r requirements.txt
```

This will install all the required packages and their dependencies listed in the `requirements.txt` file.

If you encounter any errors during the installation, make sure you have the latest version of pip installed by running:
```
pip install --upgrade pip
```

5. Once the installation is complete, create .env file
6. Add fields to .env files
```
RH_USERNAME = your_username
RH_PASSWORD = your_password
```
7. Call functions as needed at the bottom of the script
```
sample: print(getSharePrice('AAPL'))
```
8. Run Script
```
python rh_interface.py
```

## Dependencies

The following packages are required to run this project:

- pandas==1.2.4
- matplotlib==3.4.2
- numpy==1.21.0

These packages are included in the `requirements.txt` file, and can be installed using `pip`. You can also use a different package manager, such as `conda`, to install these packages.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local machine.

2. Create a new branch for your changes:
```
git checkout -b my-feature-branch
```
3. Make your changes and commit them:
```
git add .
git commit -m "Add a new feature"
```
4. Push your changes to your forked repository:
```
git push origin my-feature-branch
```
5. Open a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.