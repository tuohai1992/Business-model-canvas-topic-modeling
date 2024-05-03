


# Automatic-business-model-canvas-analysis-pipeline
This is the code repository for the paper 'High-performance computing in healthcare: Identifying business model evolution via large language model and topic modeling'

## 1. 10-K report link extraction:

Extract all 10-K report links from 2000-2022 by executing 10-K report link extraction.py.

## 2. HPC related 10-k report filtering :

Execute HPC 10-k report extraction.py to Identify HPC related business report by detecting HPC associated keywords related keywords in the business section of 10-K reports.


## 3. Extract business model canvas from HPC-related 10-k report using GPT3.5 :

Business_model_canvas_extraction_prompt.py contains the prompt to Extract business model canvas (BMC) from HPC-related 10-k report in dictionary format using GPT3.5 or GPT 4 API:
The extracted BMCs are saved in csv file 10K_report_BM_cleaned_all.csv.


## 4. Dentify healthcare related business model canvas:

Dentify_healthcare_related_business_model_canvas_prompt.py contains the prompt of Dentifing healthcare related business model canvas using GPT3.5 API

## 5. Topic modeling:

Topic modeling.py implements Topic modeling using Top2Vec algorithm for each business model canvas perspective.

## 5. Visualization of the Business model transition:

Execute Chord diagram.py to visualize the transition of each business model canvas perspective.
