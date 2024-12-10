# Bi-ReIRT Framework

## Files and Descriptions

1. **irt.py** is the backbone of the Bi-ReIRT framework.
   - `irt.py` is used for general settings, i.e., the beta IRT model.

2. **run_Amazon01.py** and **run_dataset01.py** are used for generating the matrix STS.
   - run_Amazon01 -> models = ['Random','Pop','ItemKNN','BPR','ENMF','DMF','NNCF','MultiDAE','MultiVAE','NCEPLRec','RecVAE','CDAE','LINE','SGL','DiffRec','RaCT','SimpleX']
   - run_Amazon01 -> datasets = ["Amazon_All_Beauty","Amazon_Magazine_Subscriptions","Amazon_Handmade_Products","Amazon_Subscription_Boxes","Amazon_Digital_Music","Amazon_Gift_Cards","Amazon_Health_and_Personal_Care"]
   - run_dataset01 -> models = ['Random','Pop','ItemKNN','BPR','ENMF','DMF','NNCF','MultiDAE','MultiVAE','NCEPLRec','RecVAE','CDAE','LINE','SGL','DiffRec','RaCT','SimpleX']
   - run_dataset01 -> datasets = ["ModCloth","ml-100k","ml-1m","eqinions"]
   
3. **transfer.py** is used for converting TXT files to CSV format.

4. **show.ipynb** demonstrates Direction 1 of the Bi-ReIRT framework using nDCG as the evaluation metric.
   - **show_hit.ipynb** demonstrates Direction 1 of the Bi-ReIRT framework using hit as the evaluation metric.
   - **show_mrr.ipynb** demonstrates Direction 1 of the Bi-ReIRT framework using mrr as the evaluation metric.
   - **show_precision.ipynb** demonstrates Direction 1 of the Bi-ReIRT framework using precision as the evaluation metric.
   - **show_recall.ipynb** demonstrates Direction 1 of the Bi-ReIRT framework using recall as the evaluation metric.

5. **show2.ipynb** demonstrates Direction 2 of the Bi-ReIRT framework using nDCG as the evaluation metric.
   - **show2_hit.ipynb** demonstrates Direction 2 of the Bi-ReIRT framework using hit as the evaluation metric.
   - **show2_mrr.ipynb** demonstrates Direction 2 of the Bi-ReIRT framework using mrr as the evaluation metric.
   - **show2_precision.ipynb** demonstrates Direction 2 of the Bi-ReIRT framework using precision as the evaluation metric.
   - **show2_recall.ipynb** demonstrates Direction 2 of the Bi-ReIRT framework using recall as the evaluation metric.