# Reservoir water-storage forecasting at Vajiralongkorn Dam (CNN)

Forecasting models for the reservoir water storage of EGAT's Vajiralongkorn (VRK) Dam in Kanchanaburi, Thailand, built at the dam between 2017 and 2020. Convolutional neural networks (Keras) are trained on plant-historian data for four forecast horizons. Each horizon has its own folder with a training notebook and a real-time notebook that produces rolling forecasts.

| Folder | Horizon | Training | Real-time forecast |
|---|---|---|---|
| [`model1_2Day`](model1_2Day) | 2 days | `main1.ipynb` | `2daysRT.ipynb` |
| [`model2_weekly`](model2_weekly) | 1 week | `Train.ipynb`, `train.py` | `RealTime.ipynb`, `RealTimeWeek.py` |
| [`model5_monthly`](model5_monthly) | 1 month | `EGAT_Paper1_Train_02.ipynb` | `RealTime_CNN.ipynb`, `EGAT_Paper1_03_RT*.ipynb` |
| [`model5_yearly`](model5_yearly) | 1 year | `EGAT_Paper1_Train_02.ipynb`, `EGAT_Paper1_Train_03_Resample.ipynb` | `EGAT_Paper1_03_RT_2*.ipynb` |

Each folder also holds its helper modules (`func1.py` or `Func_Paper1.py` for the models, `db1.py`, `query1.py` and `query2.py` for the SQL queries), trained weights (`.hdf5`) and CSV extracts of inputs, predictions and actual values.

## Running it

The code dates from a Python 3.7 stack: TensorFlow/Keras, scikit-learn, pandas, numpy, matplotlib and MySQLdb. The query modules read the dam's historian database, whose connection details are placeholders (`YOUR_DB_HOST` and so on), so the notebooks do not run end to end outside EGAT. The CSV files show the data layout and the results.

Larger files are in this [Google Drive folder](https://drive.google.com/drive/folders/1lWuZYY6k5mH-mo7bbKzj_kcSyc2-TUcf?usp=sharing).

## Related work

Other AI projects from the same period, such as generator-meter reading with YOLOv3, are listed on the [profile page](https://github.com/SukritJaAIproject).
