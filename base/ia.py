
import os
import joblib
import pandas as pd

class IA:
    model_paths = {
        "Death": "de.joblib",
        "Binary diagnosis": "bd.joblib",
        "Necessity of transplantation": "nr.joblib",
    }
    inpp=[
        'Age at diagnosis',
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
        'Leukocytosis',
        'Leukopenia',
        'LDH',
        'ALT',
        'AST',
        'ALP',
        'GGT',
        'Transaminitis',
        'Cholestasis',
        'FVC (L) at diagnosis',
        'FVC (%) at diagnosis',
        'DLCO (%) at diagnosis',
        'RadioWorsening2y',
        '1st degree relative',
        '2nd degree relative',
        'More than 1 relative',
        'Genetic mutation studied in patient',
        'Severity of telomere shortening',
        'Progressive disease'
    ]
    inp=[
        'Age at diagnosis',
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
        'Leukocytosis',
        'Leukopenia',
        'LDH',
        'ALT',
        'AST',
        'ALP',
        'GGT',
        'Transaminitis',
        'Cholestasis',
        'FVC (L) at diagnosis',
        'FVC (%) at diagnosis',
        'DLCO (%) at diagnosis',
        'RadioWorsening2y',
        '1st degree relative',
        '2nd degree relative',
        'More than 1 relative',
        'Genetic mutation studied in patient',
        'Severity of telomere shortening',
        'Progressive disease'
    ]
    _instance = None
    _models=[]
    def __init__(self):
        if not self._instance:
            # cls._instance = super(IA, cls).__new__(cls, *args, **kwargs)
            self._models = self.load_models()
        return self._instance



    # def test(self, dict):
    #     r = {k: 0 for k in self.inp}
    #     return {k: dict[k] if k in dict else v for k, v in r.items()}
    def test(self, dict):
        r = {k: 0 for k in self.inp}
        result = {k: dict[k] if k in dict else v for k, v in r.items()}
        print("Test Result:", result)  # Debugging
        return result

    def load_models(self):
        return [self.load_best_model(_, self.model_paths) for _ in self.model_paths.keys()]
    
    def load_best_model(self, target, model_paths):
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
    # model = load_best_model("Death", model_paths)
    def predict(self, input_data):
        # Prepare data
        processed_data = self.test(input_data)
        input_df = pd.DataFrame([processed_data])  # Convert to DataFrame

        # Run predictions
        predictions = {}
        for model_name, model in zip(self.model_paths.keys(), self._models):
            if model:
                predictions[model_name] = model.predict(input_df)
            else:
                predictions[model_name] = None
        return predictions

    
    def predict_with_model(self, input_data, target, model_dir="best_models"):

        # Comprovar si el target és vàlid
        valid_targets = ["Death", "Binary diagnosis", "Necessity of transplantation"]
        if target not in valid_targets:
            print(f"Error: El target '{target}' no és vàlid. Ha de ser un de: {valid_targets}")
            return None
        
        # Carregar el model
        model = self.load_best_model(target, model_dir=model_dir)
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