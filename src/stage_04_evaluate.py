
import pandas as pd
import numpy as np
import argparse
from src.utils.common_utils import read_param,saved_reports
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import logging

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
logging.basicConfig(level=logging.DEBUG,format=logging_str)

def eval_metrics(actual,predicted_val):
    rmse=np.sqrt(mean_squared_error(actual,predicted_val))
    mae=mean_absolute_error(actual,predicted_val)
    r2=r2_score(actual,predicted_val)
    return rmse,mae,r2


def evaluate(config_path:str):
    config=read_param(config_path)
    artifacts=config["artifacts"]
    test_data_path=artifacts["split_data"]["test_path"]
    model_path=artifacts["model_path"]
    target_col=config["base"]["traget_col"]
    scores_file=artifacts["reports"]["scores"]

    test=pd.read_csv(test_data_path,sep=',')
    test_y=test[target_col]
    test_x=test.drop(target_col,axis=1)

    lr=joblib.load(model_path)

    logging.info(f'model loaded from  {model_path}')
    predicted_values=lr.predict(test_x)

    rmse, mae, r2=eval_metrics(predicted_values,test_y)

    scores={
        "rmse":rmse,
        "mae":mae,
        "r2_score":r2
    }
    saved_reports(scores_file,scores)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args=args.parse_args()

    try:
        data=evaluate(config_path=parsed_args.config)
        logging.info('evaluation stage completed')
    except Exception as e:
        logging.error(e)