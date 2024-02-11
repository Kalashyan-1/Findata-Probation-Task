from src.dataAnalyzer import QuarterDataAnalyzer

def main():
    companyName = input("Enter the company name (CompanyA or CompanyB): ")
    analyser = QuarterDataAnalyzer(companyName)
    results = analyser.analyzData()

    formatted_results = {key: f"{value:.2f}" for key, value in results.items()}
    print(formatted_results)

main()