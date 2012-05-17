#!/usr/bin/env python

"""
@package  ion.services.sa.resource_impl.platform_agent_impl
@author   Ian Katz
"""

#from pyon.core.exception import BadRequest, NotFound
from pyon.public import PRED, RT

from ion.services.sa.resource_impl.resource_simple_impl import ResourceSimpleImpl

class PlatformAgentImpl(ResourceSimpleImpl):
    """
    @brief resource management for PlatformAgent resources
    """

    def _primary_object_name(self):
        return RT.PlatformAgent

    def _primary_object_label(self):
        return "platform_agent"

    def link_model(self, platform_agent_id='', platform_model_id=''):
        return self._link_resources(platform_agent_id, PRED.hasModel, platform_model_id)

    def unlink_model(self, platform_agent_id='', platform_model_id=''):
        return self._unlink_resources(platform_agent_id, PRED.hasModel, platform_model_id)

    def find_having_model(self, platform_model_id):
        return self._find_having(PRED.hasModel, platform_model_id)

    def find_stemming_model(self, platform_agent_id):
        return self._find_stemming(platform_agent_id, PRED.hasModel, RT.PlatformModel)
