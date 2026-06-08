# Excelerateweek1-internship
DATA CLEANING AND EXPLORATORY DATA ANALYSIS REPORT
Submitted By
Name: Rishika Chunduru
Team no:- 8
________________________________________
ABSTRACT
Data is one of the most valuable resources in modern organizations. However, raw datasets often contain missing values, duplicate records, and irrelevant information that can negatively impact analysis results. Therefore, data cleaning and preprocessing are essential steps before performing any analytical task.
This project focuses on cleaning and analyzing a dataset containing applicant and university-related information. The dataset was examined for missing values, duplicate records, and unnecessary attributes. After cleaning, exploratory data analysis (EDA) techniques were applied to understand patterns and trends within the data. Various visualizations such as bar charts, pie charts, and histograms were generated to gain insights from the dataset.
The final outcome is a cleaned dataset that is more structured, reliable, and suitable for further analysis and decision-making.
________________________________________
1. INTRODUCTION
Data analysis is the process of examining, transforming, and modeling data to discover useful information and support decision-making. Before analysis can be performed effectively, the dataset must be cleaned to ensure quality and consistency.
In real-world scenarios, datasets frequently contain incomplete information, redundant fields, and missing records. Such issues can reduce the accuracy of analytical results and create challenges during interpretation.
The purpose of this project is to perform data cleaning and exploratory data analysis on the provided dataset using Python. The project aims to identify data quality issues, improve the dataset structure, and generate meaningful visual insights.
________________________________________
2. OBJECTIVES
The main objectives of this project are:
1.	To understand the structure of the dataset.
2.	To identify missing values and duplicate records.
3.	To remove unnecessary or completely empty columns.
4.	To prepare a clean dataset for analysis.
5.	To perform exploratory data analysis using visualizations.
6.	To identify trends and patterns within the data.
7.	To summarize the findings through graphical representations.
________________________________________
3. TOOLS AND TECHNOLOGIES USED
The following tools and technologies were used during the implementation of this project:
Python
Python was used as the primary programming language because of its simplicity and powerful data analysis capabilities.
Pandas
The Pandas library was used for:
•	Reading Excel files
•	Handling missing values
•	Data cleaning
•	Data manipulation
•	Dataset inspection
Matplotlib
Matplotlib was used for:
•	Bar chart creation
•	Pie chart visualization
•	Histogram generation
•	Data presentation
Visual Studio Code
VS Code was used as the development environment for writing and executing Python scripts.
Microsoft Excel
Excel was used for storing and reviewing the dataset.
________________________________________
4. DATASET DESCRIPTION
The dataset contains applicant-related information including:
•	Applicant details
•	Country information
•	University information
•	Application source details
•	Contact information
•	Admission-related records
Original Dataset Statistics
Total Rows: 7,543
Total Columns: 80
The dataset initially contained several columns with missing values and incomplete information, requiring preprocessing before analysis.
________________________________________
5. DATA CLEANING PROCESS
Data cleaning is one of the most important phases of data analysis. The goal of cleaning is to improve data quality and remove unnecessary information.
5.1 Loading the Dataset
The dataset was imported into Python using the Pandas library.
The structure of the dataset was examined by checking:
•	Number of rows
•	Number of columns
•	Column names
•	Data completeness
________________________________________
5.2 Missing Value Analysis
Missing values were analyzed for every column in the dataset.
The analysis revealed that several columns contained a significant amount of missing data. Some columns contained no information at all.
Examples of columns with complete missing values include:
•	Major
•	Degree_Type
•	Counsler
•	Citizenship
•	Status
•	Major_1st_Choice
•	Category
•	Template
•	Region-2
and several other columns.
These columns provided no analytical value and were therefore removed.
________________________________________
5.3 Removal of Empty Columns
Columns containing 100% missing values were identified and removed.
Result
Number of columns removed: 38
This significantly improved dataset quality and reduced unnecessary complexity.
________________________________________
5.4 Duplicate Record Analysis
The dataset was examined for duplicate rows.
Result
Duplicate Records Found: 0
This indicates that the dataset did not contain any exact duplicate entries.
________________________________________
5.5 Dataset After Cleaning
After performing all cleaning operations:
Before Cleaning
Rows: 7,543
Columns: 80
After Cleaning
Rows: 7,543
Columns: 42
The number of records remained unchanged while irrelevant columns were removed.
The cleaned dataset was saved as:
DePaul_Cleaned.xlsx

________________________________________
6. EXPLORATORY DATA ANALYSIS
Exploratory Data Analysis (EDA) was performed to understand the dataset and discover useful insights.
Several visualizations were created to analyze applicant trends and distributions.
________________________________________
6.1 Country-wise Distribution Analysis
A bar chart was generated to visualize applicant distribution across countries.
Observations
•	India contributed the largest number of records.
•	The United States ranked second.
•	Ghana, Nigeria, and Pakistan also contributed notable numbers of applicants.
Interpretation
The dataset is heavily concentrated around applicants from India. This indicates strong student interest and engagement from that region.
 



________________________________________
6.2 University Distribution Analysis
A university distribution chart was generated.
Observations
•	Most records were associated with DePaul University.
Interpretation
The dataset is primarily focused on applicants connected to DePaul University and its admission process.
University Distribution Chart:-
 
________________________________________
6.3 Application Source Analysis
A pie chart was generated to analyze application sources.
Observations
•	Non Study Group: 86.5%
•	Study Group: 13.5%
Interpretation
Most applicants used Non Study Group channels for application submission. This indicates that direct application methods are considerably more common than Study Group channels.
Application Source Pie Chart:-

 
________________________________________
6.4 Attempts Distribution Analysis
A histogram was generated to analyze the Attempts column.
Observations
•	Most records were concentrated within a narrow range.
•	Very little variation was observed.
Interpretation
The Attempts variable shows limited diversity and may have a relatively small impact on further analysis.
Attempts Distribution Histogram:-






 
________________________________________
7. KEY FINDINGS
The major findings of this analysis are:
1.	The original dataset contained 80 columns and 7,543 records.
2.	A total of 38 columns were completely empty.
3.	No duplicate records were identified.
4.	India accounted for the highest number of applicants.
5.	DePaul University dominated the university-related records.
6.	Non Study Group channels represented the majority of application submissions.
7.	Data cleaning improved dataset quality while preserving all records.
________________________________________
8. CONCLUSION
This project successfully completed data cleaning and exploratory data analysis on the provided dataset.
The original dataset contained several empty columns that reduced data quality and analytical usefulness. Through systematic preprocessing, 38 completely empty columns were removed, resulting in a cleaner dataset with 42 meaningful attributes.
Exploratory analysis provided valuable insights regarding applicant distribution, university representation, and application sources. India emerged as the leading contributor of applicants, while DePaul University represented the majority of university-related records. Additionally, most applications originated from Non Study Group channels.
Overall, the project demonstrates the importance of data cleaning and exploratory analysis in transforming raw data into meaningful information. The cleaned dataset is now ready for advanced analytics, reporting, and decision-making applications.

