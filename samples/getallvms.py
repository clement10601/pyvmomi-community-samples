#!/usr/bin/env python
from pyVim import connect
from pyVmomi import vim, vmodl
content = connect.SmartConnect(host="<>",
                               user="vsapi",
                               pwd="vsapiVSAPI",
                               port=int("443"))
containerView = content.viewManager.CreateContainerView(
    container, viewType=[vim.VirtualMachine], recursive=True)
children = containerView.view
for child in children:
    summary = child.summary
    print("Name       : ", summary.config.name)
