# **Getting Started**
---

<img width="1049" alt="CD3 Toolkit Process" src="images/CD3-Process.png">

<br>
!!! tip
    CD3 Automation toolkit can be used either via CLI or Jenkins.   
    📖 Detailed documentation and videos are provided for both options. Please check the left    panel for navigation.

<style>
    .grid.cards {
        border-top-color: #5c926c;
        border-radius: 0.5rem;
    }
</style>

<div class="grid cards" style="border-top-color: #5c926c; border-radius: 1.5rem;" markdown>


-   :material-clock-fast:{ .lg .middle } __Overview__

    ---
    [Introduction](cd3-overview.md)<br>
    [Architecture](architecture.md)<br>
    [Services Supported](supportedservices.md)<br>
    [Excel Templates](ExcelTemplates.md)<br>

-   :material-hammer-screwdriver:{ .lg .middle } __Installing CD3__

    ---
    [Prerequisites](prerequisites.md)<br>
    [Launch the container](launch-container.md)<br>
    [Launch Resource Manager Stack](launch-from-rmstack.md)<br>
    [Launch from Local Desktop](launch-from-local.md)<br>
    [Connect CD3 Container to OCI](connect-container-to-oci-tenancy.md)<br>

-   :material-monitor-screenshot:{ .lg .middle } __Create, Update or Export TF with CD3 - CLI__

    ---
    [Before you Begin](workflows-cli.md)<br>
    [Create Resources from OCI using CLI (Greenfield Workflow)](greenfield-cli.md)<br>
    [Examples - Create Network](createnetwork-cli.md)<br>
    [Examples - Create Compute](createcompute-cli.md)<br>
    [OPA integration](opa-integration.md)<br>
    [Export Resources from OCI using CLI (Non-Greenfield Workflow)](nongreenfield-cli.md)<br>
    [Examples - Export Network](exportnetwork-cli.md)<br>
    [Examples - Export Compute](exportcompute-cli.md)<br>

-   :material-monitor-screenshot:{ .lg .middle } __Create, Update or Export TF with CD3 - Jenkins__

    ---

    [Before You Begin](workflows-jenkins.md)<br>
    [Overview](jenkinsintro.md)<br>
    [Create Resources from OCI using Jenkins (Greenfield Workflow)](GreenField-Jenkins.md)<br>
    [Examples - Create Network](createnetwork-jenkins.md)<br>
    [Examples - Create Compute/OKE/SDDC/Database]( createcompute-jenkins.md)<br>
    [Provision multiple Services Together](multiple-services-jenkins.md)<br>
    [Export Resources from OCI using CLI (Non-Greenfield Workflow)](NonGreenField-Jenkins.md)<br>
    [Examples - Export Network](nongreenfield-jenkins.md)<br>
    [Synchronize Changes between CLI and Jenkins](sync-cli-jenkins.md)<br>   
    

-   :material-lightbulb-auto:{ .lg .middle } __Upgrade CD3__

    ---
    [Steps to Upgrade Toolkit](upgrade-toolkit.md)<br>

-   :material-feather:{ .lg .middle } __Additional Features__

    ---
    [Grouping generated TF files](group-tf-files.md)<br>
    [OCI Resource Manager Upload](resource-manager-upload.md)<br>
    [Support for Additional Attrs](additional-attributes.md)<br>
    [CIS Compliance Features](cisfeatures.md)<br>
    [CD3 Validator](cd3validator.md)<br>
    [Migrate jobs to user's Jenkins](jobs-migration.md)<br>
    [Remote Management of Terraform State](remotestate.md)<br>

-  :material-information:{ .lg .middle } __Troubleshooting__

    ---
    [Expected Behaviour](knownbehaviour.md)<br>
    [Common Issues](commonissues.md)<br>
    [FAQs](FAQ.md)<br>

-  :material-school:{ .lg .middle } __External References__

    ---
    [Learning Videos](learningvideos.md)<br>
    [Tutorials](tutorials.md)<br>
</div>