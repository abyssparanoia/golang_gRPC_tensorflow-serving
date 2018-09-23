package main

import (
	"context"
	"log"
	tf_core_framework "tensorflow/core/framework"
	pb "tensorflow_serving/apis"

	google_protobuf "github.com/golang/protobuf/ptypes/wrappers"
	"google.golang.org/grpc"
)

func main() {

	var x int64 = 20
	var y int64 = 10

	request := &pb.PredictRequest{
		ModelSpec: &pb.ModelSpec{
			Name:          "default",
			SignatureName: "add_fn",
			Version: &google_protobuf.Int64Value{
				Value: int64(0),
			},
		},
		Inputs: map[string]*tf_core_framework.TensorProto{
			"x": &tf_core_framework.TensorProto{
				Dtype:    tf_core_framework.DataType_DT_INT64,
				Int64Val: []int64{x},
			},
			"y": &tf_core_framework.TensorProto{
				Dtype:    tf_core_framework.DataType_DT_INT64,
				Int64Val: []int64{y},
			},
		},
	}
	conn, err := grpc.Dial("localhost:8500", grpc.WithInsecure())
	if err != nil {
		log.Fatalln(err)
	}
	defer conn.Close()

	client := pb.NewPredictionServiceClient(conn)
	resp, err := client.Predict(context.Background(), request)
	if err != nil {
		log.Fatalln(err)
	}

	log.Println(resp)
}
