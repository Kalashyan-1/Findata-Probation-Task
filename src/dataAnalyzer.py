from .dataReader import QuarterDataReader, Dict

class QuarterDataAnalyzer:
    
    """
    A class for analyzing quarterly data for a specific company.

    Attributes:
    - filepath1 (str): The path to the file containing data for Quarter 1.
    - filepath2 (str): The path to the file containing data for Quarter 2.
    """

    def __init__(self, companyName: str) -> None:
        self.filepath1 = f"assets/{companyName}_Quarter1.txt"
        self.filepath2 = f"assets/{companyName}_Quarter2.txt"

    def analyzData(self) -> Dict[str, float]:
        q1 = QuarterDataReader(self.filepath1)
        q2 = QuarterDataReader(self.filepath2)
        q1.readData()
        q2.readData()
        res = {}
        q1Data = q1.getData()
        q2Data = q2.getData()

        for key in q1Data:
            res[key] = round(q2Data[key] - q1Data[key], 2)

        return res