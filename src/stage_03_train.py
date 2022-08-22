from re import L
from tkinter import E
import pandas as pd
import argparse
from src.utils.common_utils import read_param,create_dir,save_local_df,saved_reports
from sklearn.linear_model import ElasticNet
import joblib


def train(config_path):
    config=read_param(config_path)

    artifacts=config["artifacts"]

    split_data=artifacts["split_data"]
    processed_data_dir=split_data["processed_data_dir"]
    test_data_path=split_data["test_path"]
    train_data_path=split_data["train_path"]


    base=config["base"]
    random_state=base["random_state"]
    target_column=base["traget_col"]
    reports=artifacts["reports"]
    reports_dir=reports["reports_dir"]
    param_file=reports["params"]

    ElasticNet_Params=config["estimators"]["ElasticNet"]["params"]
    alpha=ElasticNet_Params["alpha"]
    l1_ratio=ElasticNet_Params["l1_ratio"]

    train=pd.read_csv(train_data_path,sep=',')
    train_y=train[target_column]
    train_x=train.drop([target_column],axis=1)
    test=pd.read_csv(test_data_path,sep=',')

    lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
    lr.fit(train_x,train_y)


    model_dir=artifacts["model_dir"]
    model_path=artifacts["model_path"]

    create_dir([model_dir,reports_dir])

    params={
        "alpha":alpha,
        "l1_ratio":l1_ratio
    }


    saved_reports(param_file,params)

    joblib.dump(lr,model_path)
    scores_file=reports["scores"]


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args=args.parse_args()

    try:
        data=train(config_path=parsed_args.config)
    except Exception as e:
        raise e