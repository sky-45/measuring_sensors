#importing modules
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.responses import FileResponse
import random

from fastapi.middleware.cors import CORSMiddleware


measurement_adc = [{"sensor":"ADC", "datetime":"14/07/2021 11:15:10", "value": 5},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:17:10", "value": 2},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:19:10", "value": 4},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:20:10", "value": 6},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:21:10", "value": 4},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:22:10", "value": 7}
                  ]
measurement_adc_2 = [{"datetime":"14/07/2021 11:15:10", "value": 5},
                  {"datetime":"14/07/2021 11:17:10", "value": 2},
                  {"datetime":"14/07/2021 11:19:10", "value": 4},
                  {"datetime":"14/07/2021 11:20:10", "value": 6},
                  {"datetime":"14/07/2021 11:21:10", "value": 4},
                  {"datetime":"14/07/2021 11:22:10", "value": 7}
                  ]       
measurement_adc_3 = [{"owner":"johan", "datetime":"14/07/2021 11:15:10", "value": 5},
                  {"owner":"johan", "datetime":"14/07/2021 11:17:10", "value": 2},
                  {"owner":"johan", "datetime":"14/07/2021 11:19:10", "value": 4},
                  {"owner":"johan", "datetime":"14/07/2021 11:22:10", "value": 7}
                  ]

#for k in range(1,600):
#    temp = {"sensor":"ADC", "datetime":"14/07/2021 11:{}:{}".format(k%50, random.randint(2, 55)), "value": 5+random.random()}
#    measurement_adc.append(temp)


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
    return measurement_adc_3

@app.get("/rand_continue")
async def root():
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    date_time = day+' '+hour
    return [date_time, random.randint(1, 8)]
    #return [measurement_adc_2[-1]["datetime"], measurement_adc_2[-1]["value"]]

@app.get("/wifi_test")
async def wifi_test():
    return random.randint(1, 8)

@app.get("/wifi_test2")
async def wifi_test2():
    return {"datetime":measurement_adc_2[-1]["datetime"], "value":measurement_adc_2[-1]["value"]}


@app.post("/post_data")
async def post_data(item: Item):
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    measurement_adc_3.append({"owner":item.owner, "sensor":item.sensor, "datetime":day+' '+hour, "value": int(item.value_measured_mem)})
    return item

@app.get("/post_data_test/{owner}/{sensor}/{value}")
async def post_data(owner: str, sensor: str, value: str):
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    dict_temp = {"owner":owner, "sensor":sensor, "datetime":day+' '+hour, "value": int(value)}
    measurement_adc_3.append(dict_temp)
    return dict_temp
