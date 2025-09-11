import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_files_from_folder(folder_path):
    Loads all text files from a given folder.
    Returns dictionary {filename: text_content}.
    """
    files_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Only check text files
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                files_data[filename] = f.read()
    return files_data


def check_plagiarism(files_data):
    """
    Takes dictionary {filename: text} and checks plagiarism using cosine similarity.
    Prints similarity score between each pair of files.
    """
    # Convert text documents to TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(files_data.values())
    vectors = vectorizer.toarray()

    # Compare each pair
    file_list = list(files_data.keys())
    plagiarism_results = []

    for i in range(len(file_list)):
        for j in range(i + 1, len(file_list)):
            similarity = cosine_similarity([vectors[i]], [vectors[j]])[0][0]
            plagiarism_results.append((file_list[i], file_list[j], similarity))

    return plagiarism_results


if __name__ == "__main__":
    folder = "documents"  # 📂 folder where your text files are stored
    files_data = load_files_from_folder(folder)

    if not files_data:
        print("⚠️ No text files found in the folder!")
    else:
        results = check_plagiarism(files_data)

        print("\n🔎 Plagiarism Report:")
        for file1, file2, score in results:
            print(f"{file1} ↔ {file2} : {score * 100:.2f}% similarity")
