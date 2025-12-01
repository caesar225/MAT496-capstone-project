from dotenv import load_dotenv
import os

load_dotenv()

from graph.build_graph import run_graph
from graph.state import BiasState


def get_user_articles():
    print("\n📰 Welcome to the News Bias Checker!")
    print("====================================")
    print("How would you like to provide articles?")
    print("1. Paste article text into the terminal")
    print("2. Provide file paths to .txt files")

    choice = input("\nEnter 1 or 2: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Please enter 1 or 2: ").strip()

    articles = []

    if choice == "1":
        num = int(input("\nHow many articles will you paste? "))
        for i in range(num):
            print(f"\n--- Paste article #{i+1} ---")
            print("Finish your article with a blank line.")
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            content = "\n".join(lines)
            source = input("Enter the source name (optional): ")
            articles.append({"source": source or "Unknown Source", "content": content})

    elif choice == "2":
        num = int(input("\nHow many file paths will you provide? "))
        for i in range(num):
            path = input(f"\nEnter path for file #{i+1}: ").strip()
            source = input("Enter the source name (optional): ")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                articles.append({"source": source or path, "content": content})
            except FileNotFoundError:
                print(f"❌ Error: Could not find file: {path}")
                exit(1)

    return articles


if __name__ == "__main__":
    articles = get_user_articles()

    if not articles:
        print("❌ No articles provided. Exiting.")
        exit()

    print("\n⏳ Running bias analysis... This may take a moment.\n")

    initial_state = BiasState(articles=articles)
    final_state = run_graph(initial_state)

    print("\n=== FINAL BIAS REPORT ===\n")
    print(final_state.final_report)
