# CKAN-API-Dataset Eexport
The script accesses datasets from a [CKAN](https://ckan.org/) catalog using the [CKAN API](https://docs.ckan.org/en/2.9/api/). 
Python scripts for exporting CKAN datasets.

## Functionality

### CKAN API Export Script Functionality
By running the python script `ckan_API_export.py` the CKAN datasets will be exported localy in `json` format in a folder called `export`. 

#### Description of the CKAN API Script Export Functionality

By running script, the user is asked to enter the URL page of the catalog from which he wants to export the data.

When the code is executed, the user will be asked whether all datasets should be exported.
There are three options: 
- to export ***all*** datasets
- to specify the ***number*** of datasets which should be exported
- to select ***specific*** dataset which should be exported.

The selected datasets can be exported as a single json file or separately for each dataset. The results will be exported to a separate folder (name of the folder `export`).

### How to export *all* datasets
The following image shows a prompt example for exporting all data records to a single file:
![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/b5f2d845-9f05-4df0-9c98-92fe4edf1f16)

The following figure shows an example of a json file and the location where the export file is saved:
![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/97e3044d-1071-4581-8162-ecaae29bb465)


The exported json file has the name of the catalog, indicates that all data is exported in the json file and the date and time of export (the following image is as example):

![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/8a96c829-5ee6-4797-b100-1e9e45733b2a)

In the prompt, it is possible to select the export of the data set as separate json files.


### How to export *specific number* of datasets
If not all data sets needs to be exported, the user needs to give the number of datasets that needs to be exported. It will be exported the lates updated/created datasets.


Here is an example of the tool's dialog:
![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/72222212-5a5d-4e5c-aef5-797b3dfa705f)


In the following image is possible to see the folder `export` with few exported datasets:

![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/817d4609-a58f-452d-ae01-c601680b57a5)

The name of the dataset will be the titel defined in the catalog and the date and time of export.
In the prompt is possible to export defined number of the dataset as one json file.

### How to export *specific* datasets
In the prompt for exporting *specific* datasets, the user can select which dataset to export. The dialog lists the datasets available in the catalog and the user has to enter the index of the datasets that he wants to export.

In the following image is shown the example from prompt:
![image](https://github.com/MarijaKnezevic/CKAN-API-Dataset_import_export/assets/93824048/def470cb-76e8-4cb2-9908-38d5349fa5bc)

The name of the data set is the title defined in the catalog as well as the date and time of the export.
In the prompt, it is possible to export selected datasets either as separate files or as a one json file.