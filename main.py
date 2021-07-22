#importing modules
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.responses import FileResponse
import random
import numpy as np

from fastapi.middleware.cors import CORSMiddleware
    
measurement_adc = [{"owner":"Johan", "datetime":"14/07/2021 11:15:10", "value": 3},
                  {"owner":"Johan", "datetime":"14/07/2021 11:17:10", "value": 2},
                  {"owner":"Johan", "datetime":"14/07/2021 11:19:10", "value": 1},
                  {"owner":"Johan", "datetime":"14/07/2021 11:20:10", "value": 2},
                  {"owner":"Johan", "datetime":"14/07/2021 11:21:10", "value": 2},
                  {"owner":"Johan", "datetime":"14/07/2021 11:21:13", "value": 1},
                  {"owner":"Johan", "datetime":"14/07/2021 11:22:14", "value": 4},
                  {"owner":"Johan", "datetime":"14/07/2021 11:22:15", "value": 2},
                  {"owner":"Johan", "datetime":"14/07/2021 11:23:01", "value": 0},
                  {"owner":"Johan", "datetime":"14/07/2021 11:23:10", "value": 2},
                  {"owner":"Johan", "datetime":"14/07/2021 11:24:10", "value": 4},
                  {"owner":"Johan", "datetime":"14/07/2021 11:24:11", "value": 4},
                  {"owner":"Johan", "datetime":"14/07/2021 11:25:10", "value": 1}
                  
                  ]

measurement_acel = [{"owner":"Johan", "datetime":"14/07/2021 11:15:10", "valueX": 100, "valueY": 200, "valueZ": 140},
                  {"owner":"Johan", "datetime":"14/07/2021 11:17:10", "valueX": 120, "valueY": 210, "valueZ": 160},
                  {"owner":"Johan", "datetime":"14/07/2021 11:19:10", "valueX": 140, "valueY": 120, "valueZ": 109},
                  {"owner":"Johan", "datetime":"14/07/2021 11:22:10", "valueX": 150, "valueY": 169, "valueZ": 42},
                  {"owner":"Johan", "datetime":"14/07/2021 11:22:14", "valueX": 160, "valueY": 120, "valueZ": 122},
                  {"owner":"Johan", "datetime":"14/07/2021 11:22:15", "valueX": 110, "valueY": 160, "valueZ": 42},
                  {"owner":"Johan", "datetime":"14/07/2021 11:23:01", "valueX": 100, "valueY": 124, "valueZ": 142},
                  {"owner":"Johan", "datetime":"14/07/2021 11:23:10", "valueX": 160, "valueY": 50, "valueZ": 202},
                  {"owner":"Johan", "datetime":"14/07/2021 11:24:10", "valueX": 220, "valueY": 60, "valueZ": 180},
                  {"owner":"Johan", "datetime":"14/07/2021 11:24:11", "valueX": 40, "valueY": 100, "valueZ": 150},
                  {"owner":"Johan", "datetime":"14/07/2021 11:25:10", "valueX": 100, "valueY": 120, "valueZ": 145}
                  ]

class Item(BaseModel):
    owner: str
    sensor: str
    value_measured_mem: str

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    #return df.to_dict("index")
    return measurement_adc

@app.get("/test_react")
async def root():
    #return df.to_dict("index")
    return measurement_adc

@app.get("/rand_continue_adc")
async def root():
    now = datetime.now()
    return {"datetime":now, "value":random.randint(1, 4)}

@app.get("/rand_continue_acel")
async def root():
    now = datetime.now()
    return {"datetime":now, "valueX":random.randint(1, 255),"valueY":random.randint(1, 255),"valueZ":random.randint(1, 255)}

@app.get("/last_adc")
async def root():
    now = datetime.now()
    return {"datetime":measurement_adc[-1]["datetime"], "value":measurement_adc[-1]["value"]}

@app.get("/last_acel")
async def root():
    now = datetime.now()
    return {"datetime":measurement_acel[-1]["datetime"],
            "valueX":measurement_acel[-1]["valueX"], 
            "valueY":measurement_acel[-1]["valueY"], 
            "valueZ":measurement_acel[-1]["valueZ"]}

@app.get("/init_adc")
async def root():
    temp_time = [k["datetime"] for k in measurement_adc]
    temp_y = [k["value"] for k in measurement_adc]
    return {"datetime":temp_time, "value":temp_y}

@app.get("/init_acel")
async def root():
    temp_time = [k["datetime"] for k in measurement_acel]
    temp_x = [k["valueX"] for k in measurement_acel]
    temp_y = [k["valueY"] for k in measurement_acel]
    temp_z = [k["valueZ"] for k in measurement_acel]
    return {"datetime":temp_time, "valueX":temp_x, "valueY":temp_y, "valueZ":temp_z}


@app.get("/post_data_ADC/{owner}/{value}")
async def post_data(owner: str, sensor: str, value: str):
    now = datetime.now()
    dict_temp = {"owner":owner, "datetime":now, "value": int(value)}
    measurement_adc.append(dict_temp)
    if(len(measurement_adc) > 40):
        measurement_adc.pop(0)
    return dict_temp

@app.get("/post_data_ACEL/{owner}/{valueX}/{valueY}/{valueZ}")
async def post_data(owner: str, valueX: str, valueY: str, valueZ: str):
    now = datetime.now()
    dict_temp = {"owner":owner, "datetime":str(now), "valueX": int(valueX), "valueY": int(valueY), "valueZ": int(valueZ)}
    measurement_acel.append(dict_temp)
    if(len(measurement_acel) > 40):
        measurement_acel.pop(0)
    return dict_temp
