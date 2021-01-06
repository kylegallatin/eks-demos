import json
import grpc
import numpy as np
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow_serving.apis import get_model_status_pb2
from tensorflow_serving.apis import get_model_metadata_pb2
from google.protobuf.json_format import MessageToJson

hostport="localhost:8500"
channel = grpc.insecure_channel(hostport)

stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
request = get_model_metadata_pb2.GetModelMetadataRequest()
request.model_spec.name = "model"
request.metadata_field.append("signature_def")
result = stub.GetModelMetadata(request, 5)  # 5 secs timeout
result = json.loads(MessageToJson(result))
print("Model metadata:")
print(result)
