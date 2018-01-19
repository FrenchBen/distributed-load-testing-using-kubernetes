#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task
import json
import time


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    #@task(1)
    #def post_state(self):
    #    payload = {"documentId": str(uuid.uuid4()), "generationTime:": #time.time(),"pageInstanceID":"ProductDetailPageNikonCamera-Staging","page":{"pageInfo":{"pageID":"NikonCamera","destinationURL":"http://mysite.com/products/NikonCamera.html"},"category":{"primaryCategory":"Cameras","subCategory1":"Nikon","pageType":"ProductDetail"},"attributes":{"Seasonal":"Christmas"}},"product":[{"productInfo":{"productName":"NikonSLRCamera","sku":"sku12345","manufacturer":"Nikon"},"category":{"primaryCategory":"Cameras"},"attributes":{"productType":"SpecialOffer"}}]}
    #    headers = {'content-type': 'application/json'}
#        self.client.post("/pubsub/push?token=1234", data=json.dumps(payload), headers=headers)

    @task(1)
    def post_state(self):
        self.client.get("/")



class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
