import argparse
import urllib.request
import zipfile
import io
import os
import shutil


def convert_bytes_to_mb(size_in_bytes):
    # Function to convert bytes to megabytes
    return size_in_bytes / (1024 * 1024)


def download_progress(count, block_size, total_size):
    # Function to track download progress
    downloaded_size = count * block_size
    if total_size > 0:
        progress = (downloaded_size / total_size) * 100
        downloaded_mb = convert_bytes_to_mb(downloaded_size)
        total_mb = convert_bytes_to_mb(total_size)
        print(f"\rDownloading... {progress:.2f}% ({downloaded_mb:.2f}/{total_mb:.2f} MB)", end="", flush=True)
    else:
        print("\rDownloading...", end="", flush=True)


def modify_data_yaml(merged_path):
    # Modify the data.yaml file
    data_yaml_path = os.path.join(merged_path, "data.yaml")
    if os.path.exists(data_yaml_path):
        with open(data_yaml_path, 'r') as file:
            lines = file.readlines()

        lines[0] = f"train: {os.path.join(merged_path, 'train', 'images')}\n"
        lines[1] = f"val: {os.path.join(merged_path, 'valid', 'images')}\n"
        lines[2] = f"test: {os.path.join(merged_path, 'test', 'images')}\n"

        with open(data_yaml_path, 'w') as file:
            file.writelines(lines)


def download_dataset(model, base_dir):
    # Define URLs and corresponding paths for different models
    model_info = {
        'yolov9': [
            ("https://universe.roboflow.com/ds/klVg64GeWg?key=DzL6TWxOFl", os.path.join(base_dir, "yolov9_dataset1/")),
            ("https://universe.roboflow.com/ds/edIyY3IfA8?key=phR9i3LWHE", os.path.join(base_dir, "yolov9_dataset2/"))],

        'yolov8': [
            ("https://universe.roboflow.com/ds/7dbfrMSkjo?key=2yEW8dC3nG", os.path.join(base_dir, "yolov8_dataset1/")),
            ("https://universe.roboflow.com/ds/1Nnbo5Oo3S?key=9ILdaTHMjy", os.path.join(base_dir, "yolov8_dataset2/"))],

        'yolov7': [
            ("https://universe.roboflow.com/ds/QM5sEcJFjV?key=7DLUgHlmpf", os.path.join(base_dir, "yolov7_dataset1/")),
            ("https://universe.roboflow.com/ds/MUQEr0FPf0?key=2XZbBsvl1p", os.path.join(base_dir, "yolov7_dataset2/"))],

        'yolov6': [
            ("https://universe.roboflow.com/ds/cFEO3GMMfQ?key=TEjabhH1fw", os.path.join(base_dir, "yolov6_dataset1/")),
            ("https://universe.roboflow.com/ds/Eaziz3FwLV?key=MtS8hbLDfF", os.path.join(base_dir, "yolov6_dataset2/"))],

        'yolov5': [
            ("https://universe.roboflow.com/ds/AHuqXQ8OIz?key=ilVN6CwW4Y", os.path.join(base_dir, "yolov5_dataset1/")),
            ("https://universe.roboflow.com/ds/1QF2rntPyc?key=bgvfEkUxB2", os.path.join(base_dir, "yolov5_dataset2/"))]

    }

    # Check if the specified model is valid
    if model not in model_info:
        print("Error: Invalid model name.")
        return

    # Loop through each (URL, path) tuple for the specified model
    for url, save_path in model_info[model]:
        # Create the directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        try:
            # Get the size of the dataset
            dataset_size = urllib.request.urlopen(url).info().get('Content-Length', -1)
            dataset_size = int(dataset_size) if dataset_size != -1 else -1

            # Download the zip file with progress tracking
            urllib.request.urlretrieve(url, save_path + "download.zip", reporthook=download_progress)
            print("\n")

            # Extract the contents to the specified path
            with zipfile.ZipFile(save_path + "download.zip", 'r') as zip_ref:
                zip_ref.extractall(save_path)

            # Remove the downloaded zip file
            os.remove(save_path + "download.zip")

            print("Dataset downloaded and extracted successfully at:", save_path)
            # print("Size of dataset:", f"{convert_bytes_to_mb(dataset_size):.2f} MB")

            # Define the name of the merged folder
            merged_folder_name = model
            merged_path = os.path.join(base_dir, merged_folder_name)

            # Create new folder for the merged dataset
            os.makedirs(merged_path, exist_ok=True)

            # Define subfolders in the merged dataset
            subfolders = ['train', 'valid', 'test']
            subsubfolders = ['images', 'labels']

            # Copy files from original folders to merged dataset folder
            for folder in subfolders:
                folder_path = os.path.join(merged_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                for subfolder in subsubfolders:
                    subfolder_path = os.path.join(folder_path, subfolder)
                    os.makedirs(subfolder_path, exist_ok=True)
                    # Copy files from original folders to merged dataset folder
                    src_path = os.path.join(save_path, folder, subfolder)
                    if os.path.exists(src_path):
                        for file in os.listdir(src_path):
                            shutil.copy(os.path.join(src_path, file), subfolder_path)

            # Copy data.yaml file to merged dataset folder
            data_yaml_src = os.path.join(save_path, "data.yaml")
            if os.path.exists(data_yaml_src):
                shutil.copy(data_yaml_src, merged_path)

            # Modify the data.yaml file
            modify_data_yaml(merged_path)

            print("Files copied to merged dataset successfully at:", merged_path)

            # Delete original folders
            # shutil.rmtree(save_path)

            print("Original folders deleted successfully.")

        except Exception as e:
            print("Error occurred:", e)


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Download dataset based on model")

    # Add model argument
    parser.add_argument('model', choices=['yolov9', 'yolov8', 'yolov7', 'yolov6', 'yolov5'],
                        help="Specify YOLO model (yolov9, yolov8, yolov7, yolov6 or yolov5)")

    # Add base directory argument
    parser.add_argument('--base-dir', type=str, required=True,
                        help="Base directory to create subfolders for extraction")

    # Parse arguments
    args = parser.parse_args()

    # Call download_dataset function with the specified model and base directory
    download_dataset(args.model, args.base_dir)


if __name__ == "__main__":
    main()
