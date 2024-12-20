import os
import joblib
import pandas as pd
model_paths = {
    "Death": "de.joblib",
    "Binary diagnosis": "bd.joblib",
    "Necessity of transplantation": "nr.joblib",
}

inp=[
    'Sex',
    'FamilialvsSporadic',
    'Age at diagnosis',
    'Binary diagnosis',
    'Final diagnosis',
    'TOBACCO',
    'Comorbidities',
    'Biopsy',
    'Diagnosis after Biopsy',
    'Multidsciplinary committee',
    'Pirfenidone',
    'Nintedanib',
    'Antifibrotic Drug',
    'Prednisone',
    'Mycophenolate',
    'Extrapulmonary affectation',
    'Associated lung cancer',
    'Other cancer',
    'Blood count abnormality at diagnosis',
    'Anemia',
    'Thrombocytopenia',
    'Thrombocytosis',
    'Lymphocytosis',
    'Lymphopenia',
    'Neutrophilia',
    'Neutropenia',
    'Leukocytosis',
    'Leukopenia',
    'Liver abnormality before diagnosis',
    'Liver abnormality',
    'LDH',
    'ALT',
    'AST',
    'ALP',
    'GGT',
    'Transaminitis',
    'Cholestasis',
    'Liver disease',
    'FVC (L) at diagnosis',
    'FVC (%) at diagnosis',
    'DLCO (%) at diagnosis',
    'FVC (L) 1 year after diagnosis',
    'FVC (%) 1 year after diagnosis',
    'DLCO (%) 1 year after diagnosis',
    'RadioWorsening2y',
    'Necessity of transplantation',
    'Death',
    'Cause of death',
    '1st degree relative',
    '2nd degree relative',
    'More than 1 relative',
    'Genetic mutation studied in patient',
    'Severity of telomere shortening',
    'Severity of telomere shortening - Transform 4',
    'Progressive disease',
    'ProgressiveDisease',
    'CHP',
    'CPFE',
    'Dendriform ossification',
    'Dentriform ossification',
    'FP no especificada',
    'Facioscapulohumeral Muscular Dystrophy ',
    'Fascioscapulohumeral muscular dystrophy',
    'GPA',
    'IPAF',
    'IPF',
    'IPF (2)',
    'IPF (3)',
    'IV Sarco',
    'Incipient ILD',
    'Intersticial Pneumonia',
    'Myopathy',
    'NSIP',
    'No history',
    'PF',
    'PF 2ary to cocaine',
    'PF- CTD',
    'PF-CTD',
    'PF-CTD (RA)',
    'PF-CTD (scleroderma)',
    'Pneumoconiosis',
    'RDT induced PF',
    'SRIF',
    'Unspecified PF',
    'Unspecified PF (2)',
    'scleroderma',
    'unspecified PF',
    'Treatment_MMF',
    'Treatment_Nintedanib',
    'Treatment_Nintedanib, Autotaxin inhibitor',
    'Treatment_Nintedanib, G-CSF',
    'Treatment_Nintedanib, Pirfenidone',
    'Treatment_Nintedanib, Pirfenidone, Prednisone, NAC',
    'Treatment_Nintedanib, Pirfenidone, Prednisone, NAC (2)',
    'Treatment_Nintedanib, Prednisone',
    'Treatment_Nintedanib, Prednisone, MMF',
    'Treatment_Nintedanib, Prednisone, MMF (2)',
    'Treatment_Nintedanib, Prednisone, Rituximab',
    'Treatment_Nintedanib, RCT 1305-0012, Autotaxin Inhibitor',
    'Treatment_Nintedanib, Rituximab, Prednisone, Leflunomide',
    'Treatment_Nintedanib, pembrolizumab, pemetrexed',
    'Treatment_Nintedanib, pirfenidone',
    'Treatment_Nintedanib, pirfenidone, prednisone',
    'Treatment_Nintedanib, pirfenidone, prednisone (2)',
    'Treatment_Nintedanib, rituximab',
    'Treatment_No Data',
    'Treatment_No data',
    'Treatment_Pirfenidone',
    'Treatment_Pirfenidone, Lebrikizumab',
    'Treatment_Pirfenidone, Prednisone',
    'Treatment_Pirfenidone, Prednisone, Azathioprine',
    'Treatment_Pirfenidone, Prednisone, MMF',
    'Treatment_Pirfenidone, Prednisone, MMF (2)',
    'Treatment_Pirfenidone, Prednisone, MMF, NAC',
    'Treatment_Pirfenidone, Prednisone, MMF, NAC (2)',
    'Treatment_Pirfenidone, Prednisone, MMF, Rituximab, Tacrolimus',
    'Treatment_Pirfenidone, Prednisone, MMF, Tacrolimus',
    'Treatment_Poor tolerance',
    'Treatment_Prednisone',
    'Treatment_Prednisone, Azathioprine',
    'Treatment_Prednisone, Leflunomide',
    'Treatment_Prednisone, Leflunomide, Abatacept',
    'Treatment_Prednisone, Leflunomide, Rituximab, Methotrexate,Toxcilizumab, Adalimumab, Etanercept',
    'Treatment_Prednisone, MMF',
    'Treatment_Prednisone, MMF (2)',
    'Treatment_Prednisone, MMF (3)',
    'Treatment_Prednisone, MMF, NAC',
    'Treatment_Prednisone, NAC',
    'Treatment_Prednisone, Nintedanib',
    'Treatment_Prednisone, Nintedanib (2)',
    'Treatment_Prednisone, Rituximab, Eculizumab, Azathioprine, NAC, MMF',
    'Treatment_Prednisone, Sulfasalazine',
    'Treatment_RCT 1305-0012',
    'Pathology pattern_0',
    'Pathology pattern_AFOP',
    'Pathology pattern_CHP',
    'Pathology pattern_Granulomatosis',
    'Pathology pattern_NSIP',
    'Pathology pattern_Necrotizing vasculitis',
    'Pathology pattern_OP',
    'Pathology pattern_Probable UIP',
    'Pathology pattern_RB-ILD',
    'Pathology pattern_UIP',
    'Pathology pattern_Unconclusive',
    'Radiological Pattern_Indeterminate UIP',
    'Radiological Pattern_Non UIP',
    'Radiological Pattern_Probable UIP',
    'Radiological Pattern_UIP',
    'Hematologic Disease_ANA 1:80',
    'Hematologic Disease_ANAA 1:80',
    'Hematologic Disease_FR +',
    'Hematologic Disease_Linfoma folicular',
    'Hematologic Disease_No',
    'Hematologic Disease_Polycytemia',
    'Hematologic Disease_Sd mielodisplasico',
    'Hematologic Disease_Thalassemia',
    'Hematologic Disease_Thalassemia minor',
    'Hematologic Disease_Yes'
]

def test(dict):
    r = {k: 0 for k in inp}
    return {k: dict[k] if k in dict else v for k, v in r.items()}

def load_best_model(target, model_paths):
    """
    Carga un modelo guardado para una variable objetivo específica desde rutas específicas.

    Args:
        target: El nombre de la variable objetivo ("Death", "Binary diagnosis", "Necessity of transplantation").
        model_paths: Un diccionario con las rutas de los modelos para cada variable objetivo.

    Returns:
        El modelo cargado o None si hay un error.
    """
    if target in model_paths:
        model_filename = model_paths[target]
        if os.path.exists(model_filename):
            loaded_model = joblib.load(model_filename)
            print(f"Loaded best model for {target} from {model_filename}")
            return loaded_model
        else:
            print(f"Error: Model file not found for {target} at {model_filename}")
            return None
    else:
        print(f"Error: No path specified for target {target}")
        return None

# Diccionario con las rutas de los modelos subidos


# Ejemplo de uso
model = load_best_model("Death", model_paths)


def predict_with_model(input_data, target, model_dir="best_models"):

    # Comprovar si el target és vàlid
    valid_targets = ["Death", "Binary diagnosis", "Necessity of transplantation"]
    if target not in valid_targets:
        print(f"Error: El target '{target}' no és vàlid. Ha de ser un de: {valid_targets}")
        return None
    
    # Carregar el model
    model = load_best_model(target, model_dir=model_dir)
    if model is None:
        return None
    
    # Convertir el diccionari a DataFrame
    try:
        input_df = pd.DataFrame([input_data])
    except Exception as e:
        print(f"Error converting input data to DataFrame: {e}")
        return None
    
    # Fer la predicció
    try:
        prediction = model.predict(input_df)
        print(f"Prediction for target {target}: {prediction}")
        return prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None