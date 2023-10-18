# config/__init__.py

from . import app_config
from . import commands_config
from . import llms_config
from . import master_agent_config
from . import responder_config

# Add attributes from each module to the config's namespace
for attr in dir(app_config):
    if not attr.startswith('__'):
        setattr(globals(), attr, getattr(app_config, attr))

for attr in dir(commands_config):
    if not attr.startswith('__'):
        setattr(globals(), attr, getattr(commands_config, attr))



for attr in dir(llms_config):
    if not attr.startswith('__'):
        setattr(globals(), attr, getattr(llms_config, attr))


for attr in dir(master_agent_config):
    if not attr.startswith('__'):
        setattr(globals(), attr, getattr(master_agent_config, attr))


for attr in dir(responder_config):
    if not attr.startswith('__'):
        setattr(globals(), attr, getattr(responder_config, attr))

        
