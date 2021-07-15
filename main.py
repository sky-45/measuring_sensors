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
    value_measured_mem: int

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
    return measurement_adc_2

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
    return measurement_adc_3



@app.post("/post_data")
async def post_data(item: Item):
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    measurement_adc_3.append({"owner":item.owner, "sensor":item.sensor, "datetime":day+' '+hour, "value": item.value_measured_mem})
    #return item



@app.get("/temperature/{last_num}")   #temperature
async def fig_temp(last_num:int):
    pth_img=get_plt_sensor("ADC", last_num, measurement_adc)
    return FileResponse(pth_img)


