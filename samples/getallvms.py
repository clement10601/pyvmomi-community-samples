#!/usr/bin/env python
from pyVim import connect
from pyVmomi import vim, vmodl
content = connect.SmartConnect(host="vCenter.cc.cs.nctu.edu.tw",
                               user="vsapi@vsphere.local",
                               pwd="vsapiVSAPI",
                               port=int("443"))
containerView = content.viewManager.CreateContainerView(
    container, viewType=[vim.VirtualMachine], recursive=True)
children = containerView.view
for child in children:
    summary = child.summary
    print("Name       : ", summary.config.name)
