""" Specify the TreeNode object with its action, context-menus """
# Copyright (C) 2009-2010, Ecole Polytechnique Federale de Lausanne (EPFL) and
# University Hospital Center and University of Lausanne (UNIL-CHUV)
#
# Modified BSD License

# Standard library imports
import os

# Enthought library imports
from enthought.traits.api import Instance, Str, Any
from enthought.traits.ui.api import TreeNode
from enthought.traits.ui.menu import Menu, Action, Separator

# ConnectomeViewer imports
from cviewer.plugins.cff2.cdata import CData

# Logging import
import logging
logger = logging.getLogger('root.'+__name__)

class CDataTreeNode(TreeNode):
    
    # The object that contains the container ;^)
    parent = Any

    # the network associated with this node
    node_for=[CData]

    # a default icons
    # Name of group item icon
    icon_group = Str('data.png')
    # Name of leaf item icon
    icon_item=Str('data.png')
    # Name of opened group item icon
    icon_open=Str('data.png')
    
    # labels
    label='dname'

    ###
    # Private Traits
    
    # activate / deactivate logic
    # if the node is activated, this means that there exists a
    # corresponding RenderManager instance
    
    _ShowName = Instance(Action,  
                               kw={'name': 'Show name', 
                                   'action': 'object.show_name',
                                   'tooltip': 'Shows the network name'}, )
    
    # the menu shown after right-click
    menu = Instance(Menu, transient=True)
    
    def get_children(self, object):
        """ Get the object's children. """
        pass
        
    ######################################################################
    # Non-public interface
    ######################################################################

    def _menu_default(self):
        """ Standard menus for network nodes """
        
        menu_actions = [Separator()]
        
        return Menu( *menu_actions)
        
