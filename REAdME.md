# Financial Data Analysis

This repository contains a console program written in [Python](https://www.python.org/) to read and analyze financial data from text files.


## Table of Contents

- [Task Description](#task-description)
- [File Structure](#file-structure)
- [Data Format](#data-format)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Contributing](#contributing)



## Task Description

Create four text files containing financial data for two companies, Company A and Company B, for the first and second quarters of the year. The program should:

1. Read data from text files.
2. Analyze the data to show the differences between each organization's Q2 and Q1 financial metrics.
3. Allow the user to input the name of the organization and see the difference in the 2nd quarter compared to the 1st quarter.


## File Structure

- `CompanyA_Quarter1.txt`: Contains financial data for Company A in the first quarter.
- `CompanyA_Quarter2.txt`: Contains financial data for Company A in the second quarter.
- `CompanyB_Quarter1.txt`: Contains financial data for Company B in the first quarter.
- `CompanyB_Quarter2.txt`: Contains financial data for Company B in the second quarter.


## Data Format

- Each text file follows the same format.

```shell
Company: [Company Name]
Quarter: [Quarter]
Revenue: [$Revenue]
Expenses: [$Expenses]
Net Income: [$NetIncome]
EPS: [$EPS]
Assets: [$Assets]
Liabilities: [$Liabilities]
Equity: [$Equity]
```

## Dependencies

- Python 3
    ```shell
    brew install python3

    git clone https://github.com/Kalashyan-1/Findata-Probation-Task.git
    ```



## How to Run

1. Clone this repository to your local machine.
    ```shell
    git clone https://github.com/Kalashyan-1/Findata-Probation-Task.git
    ```
2. Ensure you have Python installed.
    ```shell
    python3 --version
    ```
3. Open a terminal or command prompt and navigate to the repository directory.
     ```shell
    cd Findata-Probation-Task
    ```
4. Run the program using the command.
    ```shell
    python3 main.py
    ```
5. After running you should see .
    ```shell
    Enter the company name: 
    ```
    You can enter `CompanyA` or `CompanyB`.
    

## Contributing

if you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request.