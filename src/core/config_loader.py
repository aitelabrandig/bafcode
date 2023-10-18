import os
import importlib

CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')


def load_config(config_name):
    """
    Dynamically loads a configuration module from the config directory.

    Args:
    - config_name (str): The name of the configuration file without the .py extension.

    Returns:
    - module: The imported configuration module.
    """
    try:
        module_path = f"config.{config_name}"
        module = importlib.import_module(module_path)
        return module
    except ImportError:
        raise ImportError(f"Failed to import configuration module: {config_name}")


def validate_configs():
    """
    Validates the loaded configurations. This can be expanded based on specific 
    validation requirements for each configuration.
    """
    # Here, you can add specific validation checks for each configuration module.
    # For example, ensuring certain keys are present, values are of the expected type, etc.
    pass


# # Example usage:
# if __name__ == "__main__":
#     llms_config = load_config("llms_config")
#     print(dir(llms_config))  # Lists all attributes/methods in the loaded module

#     # Add other configs as needed and validate
#     validate_configs()
