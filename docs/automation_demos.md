# Automation Demos

Within the SAP LinuxLab Open-Source Initiative, there are various [Automation Projects](automation_projects.md); these range from upper-level Ansible Playbooks and Terraform Templates down to the lower-level Ansible Roles within Ansible Collections and Terraform Modules etc.

The below demos focus on the upper-level, Ansible Playbooks or Terraform Templates that coordinate many activities in an end-to-end deployment.


## Ansible Playbooks for SAP

The following are end-to-end deployments using a single pre-defined Ansible Playbook for each SAP Software Solution Scenario, that can be quickly edited and customized for the target Infrastructure Platform and Operating System. There are 40+ SAP Software Solution Scenarios, with different SAP Software Release Versions, for 9 Infrastructure Platforms, with many versions of SLES and RHEL - see [README and Detailed Documentation of Ansible Playbooks for SAP](https://github.com/sap-linuxlab/ansible.playbooks_for_sap) for more information.

This includes complex scenarios with multiple hosts, High Availability, and other Ansible Playbooks for Day 2 scenarios (e.g. run SAP RFC, System Copy Export / Import) - with optional use of either:

- Ansible to provision hosts
- Ansible-to-Terraform to create a minimal landing zone and provision hosts


### SAP S/4HANA Distributed HA installation

<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1a-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on AWS</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1b-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_msazure.cast')">Show Demo on MS Azure</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on GCP</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on IBM Cloud</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on IBM PowerVM</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on OVirt VM</button>
<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo1-wrapper','/assets/asciicast/ansible_playbooks_s4hana_dist_ha_aws.cast')">Show Demo on VMware VM</button>

<div id="ansible-demo1a-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%; height: 500px;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP S/4HANA Distributed installation (with HA)</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 8.8</strong></li>
<li>Infrastructure Platform: <strong>AWS EC2 Virtual Server</strong></li>
<li>Recording Date: <strong>2024-05-26</strong></li>
<li>Code Version: Ansible Playbooks for SAP <strong>v1.0.3</strong></li>
</ul>
</div>

<div id="ansible-demo1b-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%; height: 500px;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP S/4HANA Distributed installation (with HA)</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 9.2</strong></li>
<li>Infrastructure Platform: <strong>MS Azure Virtual Machine</strong></li>
<li>Recording Date: <strong>2024-12-01</strong></li>
<li>Code Version: Ansible Playbooks for SAP <strong>v1.0.5</strong></li>
</ul>
</div>

### SAP ECC installation

<button class="md-button" style="width: 315px;" onclick="unhide_div('ansible-demo2-wrapper','/assets/asciicast/ansible_playbooks_ecc_ibmdb2_dist_aws.cast')">Show Demo on AWS</button>
<div id="ansible-demo2-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%; height: 500px;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP Business Suite (ECC EhP8) with IBM Db2, Distributed installation (no HA)</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 8.8</strong></li>
<li>Infrastructure Platform: <strong>AWS EC2 Virtual Server</strong></li>
<li>Recording Date: <strong>2024-05-26</strong></li>
<li>Code Version: Ansible Playbooks for SAP <strong>v1.0.3</strong></li>
</ul>
</div>


## DIY Ansible Playbook using AWX

For end-users that want to understand how to build a tailored Ansible Playbook using AWX using the functionality of the `community.sap_install` Ansible Collection, a detailed step-by-step demonstration guide is available:

[demo.sap_install using Ansible AWX for DIY deployments](https://sap-linuxlab.github.io/demo.sap_install/)


## Terraform Templates for SAP

The following are end-to-end deployments using a single pre-defined Terraform Template for each SAP Software Solution Scenario. Multiple Infrastructure Platforms and Operating Systems are provided, but this project is more restrictive (limited to Sandboxes) than the Ansible Playbooks for SAP.

For More information, see [README of Terraform Templates for SAP](https://github.com/sap-linuxlab/terraform.templates_for_sap).

### SAP HANA installation

<button class="md-button" style="width: 315px;" onclick="unhide_div('terraform-demo1-wrapper','/assets/asciicast/sap_01-ascii.cast')">Show Demo on MS Azure</button>
<div id="terraform-demo1-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP HANA 2.0 SPS06, single-node</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 8.4</strong></li>
<li>Infrastructure Platform: <strong>Azure VM (ARM only, not Classic/ASM)</strong></li>
<li>Recording Date: <strong>2022-03-22</strong></li>
<li>Code Version: Terraform Templates for SAP <strong>v0.6.0</strong></li>
</ul>
</div>

### SAP S/4HANA installation using SAP Maintenance Planner

<button class="md-button" style="width: 315px;" onclick="unhide_div('terraform-demo2-wrapper','/assets/asciicast/sap_02-ascii.cast')">Show Demo on AWS</button>
<div id="terraform-demo2-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP S/4HANA Distributed installation (with HA)</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 8.8</strong></li>
<li>Infrastructure Platform: <strong>AWS EC2 instance (VPC environment only, not Classic)</strong></li>
<li>Recording Date: <strong>2022-06-14</strong></li>
<li>Code Version: Terraform Templates for SAP <strong>v0.6.0</strong></li>
</ul>
</div>

### SAP S/4HANA System Copy (Homogeneous with SAP HANA Backup / Recovery)

<button class="md-button" style="width: 315px;" onclick="unhide_div('terraform-demo3-wrapper','/assets/asciicast/sap_03-ascii.cast')">Show Demo on IBM Cloud</button>
<div id="terraform-demo3-wrapper" style="display:none; z-index: 1; position: relative; max-width: 80%;">
<ul>
<li>SAP Software Solution Scenario: <strong>SAP S/4HANA 2021, One Host System Copy (Homogeneous) using SAP HANA complete data backup file</strong></li>
<li>Operating System: <strong>RHEL for SAP Solutions 8.4</strong></li>
<li>Infrastructure Platform: <strong>IBM Cloud Virtual Server (VPC environment only, not Classic)</strong></li>
<li>Recording Date: <strong>2022-06-14</strong></li>
<li>Code Version: Terraform Templates for SAP <strong>v0.6.0</strong></li>
</ul>
</div>
