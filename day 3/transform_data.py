import pandas as pd

def extract_rank(rank_str):
    """Extracts the numerical part from the district_rank string."""
    if isinstance(rank_str, str):
        try:
            return int(rank_str.split(' ')[0])
        except ValueError:
            return None
    return None

def transform_data(input_file_path, output_file_path):
    print(f"Loading data from {input_file_path}...")
    df = pd.read_csv(input_file_path)
    
    print("Initial Data Shape:", df.shape)
    
    # 1. Drop missing values in specific columns (e.g., gender)
    print("Dropping rows with missing gender...")
    df_cleaned = df.dropna(subset=['gender']).copy()
    
    # 2. Drop duplicate rows
    print("Dropping duplicate rows...")
    df_cleaned = df_cleaned.drop_duplicates().copy()
    
    # 3. Extract numerical district rank
    print("Extracting numerical district ranks...")
    df_cleaned['district_rank_numeric'] = df_cleaned['district_rank'].apply(extract_rank)
    
    print("Final Data Shape after transformations:", df_cleaned.shape)
    
    # Save the transformed dataset
    print(f"Saving transformed data to {output_file_path}...")
    df_cleaned.to_csv(output_file_path, index=False)
    print("Transformation complete! 🚀")

if __name__ == "__main__":
    # Define file paths (Change these if running in Colab/Drive)
    INPUT_FILE = "2020_al_data_kaggle_upload_new_old_syllabi.csv"
    OUTPUT_FILE = "cleaned_al_data.csv"
    
    transform_data(INPUT_FILE, OUTPUT_FILE)
