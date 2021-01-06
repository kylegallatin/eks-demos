import json
import grpc
import numpy as np
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

hostport="localhost:8500"
channel = grpc.insecure_channel(hostport)

stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
request = predict_pb2.PredictRequest()
request.model_spec.name = 'model'
request.model_spec.signature_name = 'serving_default'

x = [1.0, 2.0, 5.0]
proto = tf.make_tensor_proto(np.array(x), dtype=float)
request.inputs['x'].CopyFrom(proto)
result_future = stub.Predict.future(request, 10.25)

response = np.array(result_future.result())

print(response)
