from src.dataAnalyzer import QuarterDataAnalyzer


def main():

    """
    Main function to analyze quarterly data for a company.
    """
    companyName = input("Enter the company name: ")
    analyser = QuarterDataAnalyzer(companyName)
    results = analyser.analyzData()

    print(results)

main()