import sys
from pathlib import Path

# Add the workspace root directory to python path for proper module imports on Streamlit Cloud
root_dir = Path(__file__).parent.absolute()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

# Execute the main application file
main_py = root_dir / "main.py"
if main_py.exists():
    with open(main_py, encoding="utf-8") as f:
        code = f.read()
    # Execute the code in the global scope of this entry point file
    # so that Streamlit runs it on every widget interaction/rerun.
    exec(code, globals())
else:
    raise FileNotFoundError("main.py not found in the application root.")
