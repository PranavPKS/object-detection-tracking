# Real-time Object Detection and Tracking

This project is mainly about developing a high-performance real-time object detection framework in an embedded AI computing device known as Nvidia Jetson TX2.

The .ipynb notebooks are very self-explanatory with many comments and descriptions. Please run them in a Python 2.7 Jupyter kernel.

v1 mainly runs the model in a multi-threaded fashion with KCF tracking alongside detections using two queues externally for receiving frames and visualize the processed ones.

v2 involves testing a split-model speed hack that splits the process into GPU and CPU sessions working in a single thread that does visualization towards the end with the frames that come from either of the CPU or GPU worker. The code additions work only for SSD-MobileNet model but result in a great performance increase. Also added multi-threading for supporting split sessions.

v3 is the merged form of both the previous versions with defined utility helpers.

Have added two types of compilations of KCF tracker that have different dependencies, so it can be used based on our convenience in different platforms.

Also contains two models, where ssd_mobilenet_v11 is a modified version of the ssd_mobilenet_v1_coco with reduced threshold for non_max_suppression(as it is found to be one of main bottlenecks).

For more detailed explanations and references, please check the report in this repository.