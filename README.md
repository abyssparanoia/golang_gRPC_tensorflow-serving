# prototyping of tensorflow-serving

====

## Overview
- tensorflow-serving + golang + gRPC

## How to use

- dockerfile の build

```bash
> docker image build -t tf-serving .
```

- run

```bash
> docker run --name tf-serving -d -v `pwd`:/root/tf-serving -p 8500:8500 -it tf-serving
```

- saved_model の生成
- 今回は prototyping なので簡単な足し算を返す saved_model を生成

```bash
> mkdir saved_model
> python make_pb.py
```

- gRPC リクエストを投げる

```bash
> go run request.go
```

## TODO

- gin で API サーバーを立てて、そこから gRPC を投げれるようにする
- react で SPA 書いて、fetch する
- 上記のサーバー込みの k8s で構築する
- GKE に deploy してみる
