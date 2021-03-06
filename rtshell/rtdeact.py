#!/usr/bin/env python
# -*- Python -*-
# -*- coding: utf-8 -*-

'''rtshell

Copyright (C) 2009-2011
    Geoffrey Biggs
    RT-Synthesis Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
Licensed under the Eclipse Public License -v 1.0 (EPL)
http://www.opensource.org/licenses/eclipse-1.0.txt

Implementation of the command to move a component to the inactive state.

'''


import state_control_base


def deactivate_action(object, ec_index):
    object.deactivate_in_ec(ec_index)


def main(argv=None, tree=None):
    return state_control_base.base_main('Deactivate a component.',
            deactivate_action, argv)


# vim: tw=79

