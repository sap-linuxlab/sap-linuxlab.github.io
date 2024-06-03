# Automation Demos

Within the SAP LinuxLab Open-Source Initiative, there are various [Automation Projects](automation_projects.md); these range from upper-level Ansible Playbooks and Terraform Templates down to the lower-level Ansible Roles within Ansible Collections and Terraform Modules etc.

The below demos focus on the upper-level, Ansible Playbooks or Terraform Templates that coordinate many activities in an end-to-end deployment.




## Ansible Playbooks for SAP

The following are end-to-end deployments using a single pre-defined Ansible Playbook for each SAP Software Solution Scenario, that can be quickly edited and customized for the target Infrastructure Platform and Operating System.

This includes complex scenarios with multiple hosts, High Availability, and other Ansible Playbooks for Day 2 scenarios (e.g. run SAP RFC, System Copy Export / Import) - with optional use of Ansible to provision hosts or using Ansible-to-Terraform to create a minimal landing zone.


## DIY Ansible Playbook using AWX

For end-users that want to understand how to build a tailored Ansible Playbook using AWX using the functionality of the `community.sap_install` Ansible Collection, a separate guide exists:

[demo.sap_install using Ansible AWX for DIY deployments](https://sap-linuxlab.github.io/demo.sap_install/)


## Terraform Templates for SAP

The following are end-to-end deployments using a single pre-defined Terraform Template for each SAP Software Solution Scenario. Multiple Infrastructure Platforms and Operating Systems are provided, but this project is more restrictive (limited to Sandboxes) than the Ansible Playbooks for SAP.

### SAP HANA installation

- SAP Software Solution Scenario: **SAP HANA 2.0 SPS06, single-node**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure Platform: **Azure VM (ARM only, not Classic/ASM)**

<button class="md-button" onclick="unhide_div('terraform-demo1-wrapper','/assets/asciicast/sap_01-ascii.cast')">Show Demo</button>
<div id="terraform-demo1-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;"></div>


### SAP S/4HANA installation using SAP Maintenance Planner

- SAP Software Solution Scenario: **SAP S/4HANA 2021, One Host**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure Platform: **AWS EC2 instance (VPC environment only, not Classic)**

<button class="md-button" onclick="unhide_div('terraform-demo2-wrapper','/assets/asciicast/sap_02-ascii.cast')">Show Demo</button>
<div id="terraform-demo2-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;"></div>


### SAP S/4HANA System Copy (Homogeneous with SAP HANA Backup / Recovery)

- SAP Software Solution Scenario: **SAP S/4HANA 2021, One Host System Copy (Homogeneous) using SAP HANA complete data backup file)**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure Platform: **IBM Cloud Virtual Server (VPC environment only, not Classic)**

<button class="md-button" onclick="unhide_div('terraform-demo3-wrapper','/assets/asciicast/sap_03-ascii.cast')">Show Demo</button>
<div id="terraform-demo3-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;"></div>

