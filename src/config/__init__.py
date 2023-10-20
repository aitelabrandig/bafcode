# config/__init__.py

from .app_config import AppConfig
from .tools_config import ToolsConfig
from .llms_config import LLMsConfig
from .master_agent_config import MasterAgentConfig
from .responder_config import ResponderConfig

class Config(AppConfig, ToolsConfig, LLMsConfig, MasterAgentConfig, ResponderConfig):
    pass
