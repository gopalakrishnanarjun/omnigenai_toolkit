
# utils.py
def load_config(config_path: str):
    """
    Loads configuration settings from a file.
    """
    return f"Loaded config from {config_path}"

def log_event(event: str, log_path: str):
    """
    Logs an event to the specified file.
    """
    with open(log_path, 'a') as log_file:
        log_file.write(f"{event}\n")
    return f"Event logged: {event}"
