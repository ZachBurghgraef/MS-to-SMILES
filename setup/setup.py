import kagglehub

def get_data_set():
    # Download latest version of the enveda-CASMI26 dataset ~ 3 GB in size
    print("Downloading dataset...")
    path = kagglehub.competition_download('enveda-CASMI26-molecule-id-mass-spectra')
    
    with open(r"setup/path_to_dataset.txt", 'w') as f:
        f.write(str(path))

    print("Path to competition files:", path)

def main():
    get_data_set()

if __name__ == "__main__":
    main()
