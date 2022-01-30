# Generate_Documents
This repository focuses on automating creation of commonly used document, which can be required in quantity and contains predefined templates.
i.e. The user can create documents in bulk as per requirements

## Pre-Requisites :
> The user needs to create his customized template using the guide, Which can be dowloaded using the API

> OS should be Windows having Python3 installed

## Tech stack :
> OS used : Windows

> Programming Language : Python3

> Framework : Flask

> Storage : File storage ( Can be switched to database with modifications )

> Python Packages used : flask, connexion, pandas, docxtpl, docx2pdf, zipfile

<br>
Here are the some steps for user to follow :

1. download the template using an API 
2. Create his customized template as per the requirement
3. prepare the data in excel format 
4. upload the template and data to download the documents 

<br>
Just like we know **"Every coin has 2 sides"** this project also has some advantages and disadvantages which are also highlighted below 

### Advantages :

1. The user can create documents in bulk in optimum amount of time
2. The format of the document remains same for all the created documents
3. Non-required columns present in the excel will be auto-ignored
4. The user can download the created documents in word/pdf format 
5. Template guide needs to be created only once   

### Disadvantages :

1. Does not handle missing data as it focuses only on document creation 
2. requires windows operating system
3. User needs to create his customized template 
