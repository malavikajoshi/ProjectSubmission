import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


API = "https://mocki.io/v1/3e7c5e22-8098-4e7a-a861-3d9776baac4e"

def student_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)
        return []
    
def data_processing(data):
    df = pd.DataFrame(data)
    average_score = df["score"].mean()
    return df, average_score

def visualization(df):
    plt.figure()
    plt.bar(df["name"], df["score"])
    plt.xlabel("Students")
    plt.ylabel("Test Scores")
    plt.title("Student Test Scores")
    plt.tight_layout()
    plt.show()
    input("Press Enter to close the chart...")

def main():
    students= student_data(API)
     
    if not student_data:
        print("No data available to process.")
        return
    
    df, avg_score = data_processing(students)

    print(f"Average Score: {avg_score:.2f}")
    visualization(df)
    
if __name__ == "__main__":
    main()

