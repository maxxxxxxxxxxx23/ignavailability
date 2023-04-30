import requests

# List of usernames to check
usernames = ['serotonin', 'doxycycline', 'aspirin', 'ibuprofen', 'paracetamol', 'morphine', 'insulin', 'adrenaline', 'dopamine', 'noradrenaline', 'oxytocin', 'estrogen', 'testosterone', 'caffeine', 'nicotine', 'amoxicillin', 'codeine', 'penicillin', 'methamphetamine', 'ecstasy', 'cocaine', 'heroin', 'LSD', 'mescaline', 'psilocybin', 'ketamine', 'nitrous', 'marijuana', 'ketoprofen', 'citalopram', 'sertraline', 'fluoxetine', 'venlafaxine', 'olanzapine', 'risperidone', 'quetiapine', 'aripiprazole', 'haloperidol', 'clonazepam', 'diazepam', 'alprazolam', 'lorazepam', 'zolpidem', 'zopiclone', 'temazepam', 'fluconazole', 'itraconazole', 'amphotericin', 'nystatin', 'tetracycline', 'doxorubicin', 'cisplatin', 'paclitaxel', 'carboplatin', 'methotrexate', '5-fluorouracil', 'tamoxifen', 'letrozole', 'anastrozole', 'raloxifene', 'levothyroxine', 'lisinopril', 'losartan', 'atorvastatin', 'simvastatin', 'metformin', 'glyburide', 'pioglitazone', 'liraglutide', 'exenatide', 'sitagliptin', 'ranitidine', 'omeprazole', 'esomeprazole', 'famotidine', 'cimetidine', 'sucralfate', 'misoprostol', 'ondansetron', 'metoclopramide', 'prochlorperazine', 'promethazine', 'diphenhydramine', 'loratadine', 'fexofenadine', 'cetirizine', 'naproxen', 'celecoxib', 'diclofenac', 'meloxicam', 'prednisone', 'hydrocortisone', 'dexamethasone', 'triamcinolone', 'prednisolone', 'methyldopa', 'clonidine', 'hydralazine', 'nifedipine', 'diltiazem', 'verapamil', 'warfarin', 'heparin', 'enoxaparin', 'clopidogrel', 'tadalafil', 'sildenafil', 'vardenafil', 'albuterol', 'ipratropium', 'tiotropium', 'fluticasone', 'budesonide', 'montelukast', 'zafirlukast', 'theophylline', 'ritonavir', 'lopinavir-ritonavir', 'atazanavir', 'darunavir', 'raltegravir', 'etravirine', 'efavirenz', 'nevirapine', 'tenofovir', 'zidovudine', 'abacavir',]

# Loop through each username in the list
for username in usernames:
    # Construct the URL with the username
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}'

    # Make a GET request to the URL
    response = requests.get(url)

    # Check the response status code to determine availability
    if response.status_code == 200:
        print(f"Username {username} is not available")
    else:
        print(f"Username {username} is available!")
