<h2>Export from one Tenancy and  Create the same infra in another tenancy </h2>

Set Up the CD3 containers and connect them to Source Tenancy and Target tenancy using steps mentioned in https://oracle-devrel.github.io/cd3-automation-toolkit/install-cd3/
Note - Same process can be used to replicate 

**Method 1: Using the excel sheet of source tenancy**
<h3> Identity Components </h3>
1. Execute the toolkit to export Identity Components(Compartments, Groups, Policies, Users, Network Sources) from source tenancy. 
2. There is no need to execute shell script containing the terraform import commands.
3. Use the exported excel. Make appropriate changes to Identity tabs (Compartments, Groups, Policies, Users, Network Sources) like region name as per the new tenancy.
4. Execute the toolkit to create Identity components in target tenancy using above excel sheet.
5. Execute terraform init, plan and apply for 'identity' service directory of home region in target tenancy container.

<h3> Network Components </h3>
1. Execute the toolkit to export all Network Compnents (Option - 'Export all Network Components' under 'Network') from source tenancy.
2. It will export the data into excel template networking tabs and also create obj_names.safe file in 'network' service directory of each region.
3. There is no need to execute shell script containing the terraform import commands.
4. Use the exported excel. Make appropriate changes if any (eg Region name, VCN name or CIDR block etc) to Network tabs. eg If VCN name needs to be changed for target tenancy, it will need to be changed in 'VCN Name' column of VCNs, SubentsVLANs, DHCP, SecRulesinOCI, RouteRulesinOCI tabs and 'Attached To' column of DRGs tab.
5. Move obj_names.safe from source region's 'network' directory  to target region's 'network' directory. If any changes are done to to VCN name/DRG name/DRG RT name attached to VCN in the excel, make sure to update corresponding obj_names.safe file as well.
6. Execute the toolkit for Create Workflow using above excel sheet in target tenancy container. Chose 'Network' in main options and then 'Create Network', 'Security Rules', 'Route Rules', 'DRG Route Rules' from child-options. Chose 'Customer Connectivity' also in case there are RPCs also which need to be established. Chose 'Add/Modify/Delete Security Rules (Reads SecRulesinOCI sheet)', 'Add/Modify/Delete Route Rules (Reads RouteRulesinOCI sheet)', 'Add/Modify/Delete DRG Route Rules (Reads DRGRouteRulesinOCI sheet)', 'Create Remote Peering Connections' from sub-child-options).
7. Execute terraform init, plan and apply for 'network' service directory of each region in target tenancy container. This will create networking components in target OCI console.
8. Execute terraform init, plan and apply for 'global/rpc' service directory in target tenancy container. This will create RPCs between regions in target OCI console.

9. If the source tenancy contains NSGs or VLANs and need to be replicated to target tenancy, then re run the toolkit in target tenancy and Chose 'Network' in main options and then 'Network Security Groups' and 'Add/Modify/Delete VLANs' from chid-options. Chose 'Add/Modify/Delete NSGs (Reads NSGs sheet)' from sub-child-options.
10. Execute terraform init, plan and apply for 'nsg' and 'vlan' service directory of each region in target tenancy container. This will create NSGs and VLANs in target OCI console.

<h3> Use the same procedure to replicae any other resources in OCI </h3>

**Method 2: Usning the terraform code of source tenancy**
<h3> Identity Components </h3>
1. Execute the toolkit to export Identity Components(Compartments, Groups, Policies, Users, Network Sources) from source tenancy. 
2. There is no need to execute shell script containing the terraform import commands.
3. Copy the generated *.auto.tfvars from 'identity' service folder of home region in source tenancy container.
4. Paste the files to identity' service folder of home region in target tenancy container.
5. Make appropriate changes in tfvars 
   