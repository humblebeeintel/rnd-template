import os
import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Optional

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("config")

PROJECT_ROOT = Path(__file__).parent
CONFIG_DIR = PROJECT_ROOT / "configs"


class Config:
    """Configuration manager for the project."""

    def __init__(self, config_name: str = "default", env: Optional[str] = None):
        """
        Initialize configuration from YAML files.

        Args:
            config_name: Base configuration name (without .yaml extension)
            env: Optional environment name for override configs (e.g., 'dev', 'prod')
        """
        self.config_name = config_name
        self.env = env
        self._config = {}

        self._load_config()

        logger.info(
            f"Loaded configuration: {config_name}"
            + (f" with env: {env}" if env else "")
        )

    def _load_config(self) -> None:
        """Load configuration from base and environment-specific YAML files."""
        # Create configs directory if it doesn't exist
        os.makedirs(CONFIG_DIR, exist_ok=True)

        # Load base config
        base_config_path = CONFIG_DIR / f"{self.config_name}.yaml"
        if base_config_path.exists():
            with open(base_config_path, "r") as f:
                config_data = yaml.safe_load(f) or {}
                self._config.update(config_data)
                logger.info(f"Loaded config from {base_config_path}")
        else:
            logger.warning(f"Config file not found: {base_config_path}")

        # Load environment-specific config if specified
        if self.env:
            env_config_path = CONFIG_DIR / f"{self.config_name}.{self.env}.yaml"
            if env_config_path.exists():
                with open(env_config_path, "r") as f:
                    env_config = yaml.safe_load(f) or {}
                    # Deep merge configs
                    self._deep_update(self._config, env_config)
                    logger.info(f"Loaded environment config from {env_config_path}")
            else:
                logger.warning(f"Environment config file not found: {env_config_path}")

    def _deep_update(self, base_dict: Dict, update_dict: Dict) -> None:
        """Recursively update a dictionary."""
        for key, value in update_dict.items():
            if (
                isinstance(value, dict)
                and key in base_dict
                and isinstance(base_dict[key], dict)
            ):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value by key with optional default."""
        return self._config.get(key, default)

    def get_iter(self, key_path: str, default: Any = None) -> Any:
        """
        Get a config value using dot notation for nested keys.

        Args:
            key_path: Dot-separated key path (e.g., 'database.connection.host')
            default: Default value to return if key path not found

        Returns:
            Config value at the specified path, or default if not found
        """
        if not key_path:
            return default

        # Split the key path by dots
        parts = key_path.split(".")

        # Start with the root config
        current = self._config

        # Traverse the path
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                logger.debug(f"Key path not found: {key_path}")
                return default

        return current

    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-like access to configuration."""
        # Support dot notation in __getitem__ as well
        if "." in key:
            value = self.get_iter(key)
            if value is None:
                raise KeyError(key)
            return value
        return self._config[key]

    def __contains__(self, key: str) -> bool:
        """Check if a key exists in the configuration."""
        if "." in key:
            try:
                return self.get_iter(key) is not None
            except:  # noqa: E722
                return False
        return key in self._config

    def __str__(self) -> str:
        """Return a string representation of the configuration."""

        def format_value(value, indent=0):
            if isinstance(value, dict):
                result = "\n"
                for k, v in value.items():
                    result += f"{' ' * (indent + 2)}{k}: {format_value(v, indent + 2)}"
                return result
            else:
                return f"{value}\n"

        result = f"Configuration ({self.config_name}"
        if self.env:
            result += f", env={self.env}"
        result += "):\n"

        for key, value in self._config.items():
            result += f"  {key}: {format_value(value, 2)}"

        return result

    def __repr__(self) -> str:
        """Return a string representation of the configuration object."""
        return self.__str__()

    @property
    def all(self) -> Dict[str, Any]:
        """Return the entire configuration dictionary."""
        return self._config.copy()

    def display_section(self, section_name: str) -> None:
        """Display a specific section of the configuration."""
        section = self.get_iter(section_name, {})
        print(f"{section_name.capitalize()} Configuration:")
        for key, value in section.items():
            print(f"  - {key}: {value}")
