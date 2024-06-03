# Automation Projects and Capabilities

The SAP LinuxLab Open-Source Initiative include many Automation Projects, with various functionality for provisioning, installing and operating SAP Systems.

Overall, the initiative's automation projects seek to assist SAP-run enterprises to achieve various business-focused outcomes, such as:

- **SAP S/4HANA Greenfield/Re-Implementation**, *e.g. install from SAP Maintenance Planner*
- **SAP S/4HANA Brownfield/Conversion**, *e.g. System Copy and DMO for SUM*
- **SAP S/4HANA Selective Data Transition**, *e.g. System Copy and Shell Conversion or Mix&Match*
- **Datacenter Exit / Cloud Service Provider switch Compute Re-locate**, *e.g. System Copy to new Infrastructure*
- **Enterprise re-structures with Spin-offs and Divestitures**, *e.g. System Copy and carve-out*
- **Enterprise re-structures with Mergers and Acquisitions**, *e.g. System Copy and merge*
- **Daily SAP Operations / Maintenance**, *e.g. Start/Stop SAP Systems, RFC / BAPI / Task List runs, Backup scheduled runs, SAP Kernel patching*

<h3>Automated tasks and functionality include:</h3>

<div style="font-size: 12px;">

<ul>
<li>Provision SAP Virtual Machines (Day 0) to Infrastructure Platforms
<ul>
  <li>AWS EC2 Virtual Server instances</li>
  <li>Google Cloud Compute Engine Virtual Machines</li>
  <li>IBM Cloud, Intel Virtual Servers and Power Virtual Servers</li>
  <li>Microsoft Azure Virtual Machines</li>
  <li>IBM PowerVM Virtual Machines (LPARs)</li>
  <li>OVirt (e.g. Red Hat Enterprise Linux KVM)</li>
  <li>KubeVirt (e.g. Red Hat OpenShift Virtualization, SUSE Rancher with Harvester HCI)</li>
  <li>VMware vSphere Virtual Machines</li>
</ul>
</li>
<li>Download SAP Installation Media (Day 0)
<ul>
  <li>SAP User ID SSO login</li>
  <li>Search and download by filename</li>
  <li>Maintenance Planner stack download</li>
</ul>
</li>
<li>Operating System preparation for SAP (Day 0)
<ul>
  <li>Preconfigure and tune Red Hat Enterprise Linux for SAP Solutions</li>
  <li>Preconfigure and tune SUSE Linux Enterprise Server for SAP Applications</li>
</ul>
<li>SAP Installations (Day 1)
<ul>
  <li>Install SAP HANA via HDBLCM, any combination</li>
  <li>Install SAP Software via SWPM, any combination</li>
  <li>Install SAP High Availability with Linux Pacemaker</li>
  <li>Pre-completed Ansible Playbooks include:
  <ul>
    <li>SAP HANA - Scale-Up, Scale-Up High Availability (Performance Optimized), Scale-Out</li>
    <li>SAP S/4HANA Foundation</li>
    <li>SAP S/4HANA - including Distributed High Availability with Maintenance Planner Stack</li>
    <li>SAP BW/4HANA - including Scale-Out</li>
    <li>SAP ECC - including SAP HANA, IBM Db2, Oracle DB, SAP ASE, SAP MaxDB</li>
    <li>SAP ECC IDES</li>
    <li>SAP NetWeaver AS (ABAP/JAVA)</li>
    <li>SAP SolMan (ABAP/JAVA)</li>
    <li>SAP WebDispatcher</li>
  </ul>
  </li>
</ul>
</li>
<li>SAP Operations (Day 2)
<ul>
  <li>Post-Install of SAP Software OS configuration</li>
  <li>SAP System Copy Export / Import Restore</li>
  <li>SAP Systems Start/Stop</li>
  <li>SAP Profile updates</li>
  <li>SAP HANA Backint backup scheduling and execution</li>
  <li>SAP RFC / BAPI / Task List runs</li>
  <li>SAP Kernel patching [WIP]</li>
  <li>SAP SolMan Diagnostics Agent (SDA) installation</li>
</ul>
</li>


</div>

<h3>Automation Projects within the SAP LinuxLab Open-Source Initiative include:</h3>

| Project Repository | Project Description |
|:---|:---|
| [ansible.playbooks_for_sap](https://github.com/sap-linuxlab/ansible.playbooks_for_sap) | Top-level Pre-built Ansible Playbooks using the Ansible Collections for SAP; uses Ansible to provision, with optional Ansible > Terraform |
| [terraform.templates_for_sap](https://github.com/sap-linuxlab/terraform.templates_for_sap) |  Top-level Pre-built Terraform Templates for deployment of various SAP solution scenarios, for every Cloud and Hypervisor |
| | |
| [community.sap_install](https://github.com/sap-linuxlab/community.sap_install) | Ansible Collection of Ansible Roles for various SAP software installation |
| [community.sap_operations](https://github.com/sap-linuxlab/community.sap_operations) | Ansible Collection of Ansible Roles for various operational tasks with SAP Systems |
| [community.sap_infrastructure](https://github.com/sap-linuxlab/community.sap_infrastructure) | Collection of Ansible Roles for infrastructure-related tasks for SAP |
| [community.sap_launchpad](https://github.com/sap-linuxlab/community.sap_launchpad) | Ansible Collection of Ansible Roles and Ansible Modules for various tasks using SAP Launchpad APIs |
| [community.sap_libs](https://github.com/sap-linuxlab/community.sap_libs) | Collection of Ansible Modules for SAP for low-level activities which are highly reusable |
| [terraform.modules_for_sap](https://github.com/sap-linuxlab/terraform.modules_for_sap) | Terraform Modules for each Cloud and Hypervisor and dynamic Ansible Playbooks for SAP installations. Subcomponent of the Terraform Templates for SAP |
| [demo.sap_install](https://github.com/sap-linuxlab/demo.sap_install) | Demonstration usage of Build-your-Own community.sap_install Ansible Collection, using Ansible AWX |
