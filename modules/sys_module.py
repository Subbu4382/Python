import sys

# Shows the Python version 
print(f"Python version: {sys.version}")

# Show the path of the currently running script
print(f"Script name: {sys.argv[0]}")

# List all arguments passed to the script
# sys.argv is a list: [script_name, arg1, arg2, ...]
if len(sys.argv) > 1:
    print(f" Arguments passed: {sys.argv[1:]}")
else:
    print(" No arguments were passed!")

# Show the platform Python is running on
print(f" Platform: {sys.platform}")

#  Show the path where Python looks for modules
print("Python module search paths:")
for path in sys.path:
    print(f"   - {path}")

# Exit the script gracefully (status code 0 means success)
# sys.exit(0)
