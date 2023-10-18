# config/__init__.py

from .app_config import AppConfig
from .commands_config import CommandsConfig
from .llms_config import LLMsConfig
from .master_agent_config import MasterAgentConfig
from .responder_config import ResponderConfig

class Config(AppConfig, CommandsConfig, LLMsConfig, MasterAgentConfig, ResponderConfig):
    pass
