
import os
import joblib
import pandas as pd

class IA:
    model_paths = {
        "Death": "de.joblib",
        "Binary diagnosis": "bd.joblib",
        "Necessity of transplantation": "nr.joblib",
    }
    _instance = None
    _models=[]

    def __init__(self):
        if not self._instance:
            # cls._instance = super(IA, cls).__new__(cls, *args, **kwargs)
            self._models = self.load_models()
        return self._instance


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

    def predict(self, input_data):
        print(input_data)
        """
        Runs predictions for all models using input_data.
        """
        try:
            # Ensure input_data is a dictionary-like structure
            if isinstance(input_data, dict):
                input_df = pd.DataFrame([input_data])  # Convert to DataFrame
            else:
                input_dict = vars(input_data) if hasattr(input_data, '__dict__') else dict(input_data)
                input_df = pd.DataFrame([input_dict])  # Convert to DataFrame
        except Exception as e:
            print(f"Error creating DataFrame from input data: {e}")
            return None

        # Convert DataFrame to numpy array for compatibility with models
        input_array = input_df.to_numpy()

        # Run predictions
        predictions = {}
        for model_name, model in zip(self.model_paths.keys(), self._models):
            if model:
                try:
                    predictions[model_name] = model.predict(input_array)  # Pass numpy array
                except Exception as e:
                    print(f"Error predicting with model '{model_name}': {e}")
                    predictions[model_name] = None
            else:
                predictions[model_name] = None
        return predictions


