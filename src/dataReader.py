import os
from typing import Dict





class QuarterDataReader:
    
    """
    A class for reading data from a quarterly report file.

    Attributes:
    - filePath (str): The path to the file containing quarterly report data.
    - data (Dict[str, float]): A dictionary to store the quarterly report data.
    """
    
    def __init__(self, filePath: str) -> None:
        self.data = {}
        self.path = filePath

    def readData(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                content = file.readlines()
                for i, line in enumerate(content):
                    if i >= 2:
                        key, value = line.strip().split(': ')
                        self.data[key] = float(value.replace('$', '').replace(',', ''))
        else:
            print("Could not open file " + self.path)


    
    def getData(self) -> Dict[str, float]:
        return self.data
     
