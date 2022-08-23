import json
import yaml
import os 
import shutil
import logging
import json


def read_param(config_path:str)-> dict:
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    logging.info("read parameters")
    return config

def clean_prev_dir_if_exists(dir_path:str):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    logging.info(f"cleaned existing artifacts director at {dir_path}")

def create_dir(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        logging.info(f"created directory at {dir_path}")


def save_local_df(df,df_path,header=False):
    if header:
        new_cols=[col.replace(" ","_") for col in df.columns]
        df.to_csv(df_path,index=False,header=new_cols)
        logging.info(f"dataframe saved at {df_path} with new headers")
    else:
        df.to_csv(df_path,index=False)
        logging.info(f"dataframe saved at {df_path}")

def saved_reports(file_path:str,report:dict):
    with open(file_path,"w") as f:
        json.dump(report,f,indent=4)
    logging.info(f"reports saved at {file_path}")