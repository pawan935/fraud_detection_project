import os
import kagglehub
import pandas as pd


def download_dataset():
    """Download credit card fraud dataset using KaggleHub and save locally."""
    file_name = "creditcard.csv"
    save_path = os.path.join("data", file_name)

    # If already downloaded, skip
    if os.path.exists(save_path):
        print(f"✅ Dataset already exists at {save_path}")
        return pd.read_csv(save_path, encoding="latin1")

    print("⬇️ Downloading dataset from Kaggle...")
    dataset_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
    source_path = os.path.join(dataset_path, file_name)

    # Load with Pandas (safe encoding)
    df = pd.read_csv(source_path, encoding="latin1")

    # Save a local copy
    df.to_csv(save_path, index=False)
    print(f"✅ Dataset saved to {save_path}")

    return df


def main():
    df = download_dataset()
    print("\n📊 Dataset Info")
    print("Shape:", df.shape)
    print(df.head())
    print("\nClass distribution:")
    print(df["Class"].value_counts())


if __name__ == "__main__":
    main()
