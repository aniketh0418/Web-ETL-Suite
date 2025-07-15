import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"

def logs(msg):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + "," + msg + "\n")

def extract_data_csv(file):
    df = pd.read_csv(file)
    return df

def extract_data_json(file):
    df = pd.read_json(file, lines=True)
    return df

def extract_data_xml(file):
    df = pd.DataFrame(columns=["name", "height", "weight"])
    xml_parser = ET.parse(file)
    xml_content = xml_parser.getroot()
    for item in xml_content:
        name = item.find("name").text
        height = item.find("height").text
        weight = item.find("weight").text
        df = pd.concat([df, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
    return df

def extract_data():
    logs("Extract Phase Started")
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])
    for csvfile in glob.glob("*.csv"):
        if csvfile != target_file:
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_data_csv(csvfile))], ignore_index=True)
    for jsonfile in glob.glob("*.json"):
        if jsonfile != target_file:
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_data_json(jsonfile))], ignore_index=True)
    for xmlfile in glob.glob("*.xml"):
        if xmlfile != target_file:
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_data_xml(xmlfile))], ignore_index=True)
    logs("Extract Phase Ended")
    return extracted_data

def transform_data(data):
    logs("Transform Phase Started")
    data["height"] = round(pd.to_numeric(data["height"], errors="coerce") * 0.0254, 2)
    data["weight"] = round(pd.to_numeric(data["weight"], errors="coerce") * 0.45359237, 2)
    logs("Transform Phase Ended")
    return data

def load_data(target_file, transformed_data):
    logs("Load Phase Started")
    transformed_data.to_csv(target_file)
    logs("Load Phase Ended")

logs("ETL Job Started")

extracted_data = extract_data()
print("Data Extracted!")

transformed_data = transform_data(extracted_data)
print("Data Transformed!")

load_data(target_file, transformed_data)
print("Data Loaded!")

logs("ETL Job Ended!")