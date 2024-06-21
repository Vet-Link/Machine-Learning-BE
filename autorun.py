import papermill as pm
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now().strftime('%d-%m-%y_%H-%M-%S')

# Path to your input notebook
input_path = 'doc_recom.ipynb'

# Execute the notebook
pm.execute_notebook(input_path, None)
