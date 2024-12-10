from recbole.quick_start import run_recbole

models = [
    'Random','Pop', 'ItemKNN', 'BPR', 'ENMF', 'DMF', 'NNCF','MultiDAE', 'MultiVAE', 'NCEPLRec', 'RecVAE', 'CDAE', 'LINE','SGL', 'DiffRec', 'RaCT', 'SimpleX'
]

# Datasets to loop through
datasets = [
    "ModCloth",
    "ml-100k",
    "ml-1m",
    "eqinions"
]

for dataset in datasets:
    # Open a separate file for each dataset
    with open(f"./Res/{dataset}_Res.txt", "w") as file:
        for model in models:
            # Run the model and get the result
            print(f"Running model: {model} on dataset: {dataset}")
            result = run_recbole(model=model, dataset=dataset, config_file_list=['example2.yaml'])

            # Write model name and results to the file for the current dataset
            file.write(f"Model: {model}\n")
            for metric, value in result.items():
                file.write(f"{metric}: {value}\n")
            file.write("\n")  # Add a newline for separation between models
