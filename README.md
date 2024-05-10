<details>
  <summary>Demo Videos</summary>

https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/1eb16936-a51d-4670-9938-d00686cfc406

https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ad516cfb-a181-413b-9a38-334d733e8d0d

</details>


![Yolov7NightVideoInference](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/5ada6deb-499a-45fa-85dc-131497da6ed1) ![Yolov5DayVideoInference](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/b3382b28-b251-498b-af8b-2b39b46878dc)



:fire::fire::fire::fire::dash::dash::dash::fire::fire::fire::fire:
# NEW Fire and Smoke Dataset for Object Detection
:fire::fire::fire::fire::dash::dash::dash::fire::fire::fire::fire:

## Short Introduction

In this repository, I introduce a  $\color{red}{\textsf{NEW Fire and Smoke Dataset}}$, designed for object detection tasks. I utilize this dataset to train several YOLO models, including   $\color{magenta}{\textsf{ YoloV5, YoloV6, YoloV7, YoloV8, YoloV9, and YoloNAS}}$.


⭐⭐ $\color{orange}{\textsf{Key Features of this repository}}$ ⭐⭐

a) The FireAndSmoke dataset encompasses a wide range of images from various real-world scenes, including  $\color{green}{\textsf{buildings on fire, cars on fire, vegetation fires, wildfires, trash fires, and interior fires.}}$ 

b) The dataset contains  $\color{orangered}{\textsf{aerial views from drones, close-up and distant shots of fires}}$, as well as images captured from below when the $\color{orangered}{\textsf{fire is at a higher altitude}}$. Additionally, the fires vary in $\color{orangered}{\textsf{magnitude and size and may be obscured by vegetation or other objects}}$.

c) The dataset includes a diverse selection of fire and smoke images, captured at $\color{orangered}{\textsf{different times throughout the day — from early morning to late at night}}$. Additionally, the images were taken under a $\color{orangered}{\textsf{variety of weather conditions, including sunny, cloudy, rainy, and foggy scenarios}}$, to showcase how fires and smoke behave and appear in different atmospheric settings. 

Overall, the comprehensive nature of the FireAndSmoke dataset, with its wide range of scenes, perspectives, sizes, and environmental conditions, makes it highly suitable for training robust machine learning models that can accurately and reliably detect and analyze fires in any situation.


## Dataset
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/30dba36b-ffca-45e7-8ae5-619a376bcbe2) ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/608103f3-dc1c-41b6-b6f8-b715cfb1af9e)

The dataset is hosted on the Roboflow platform and consists of two projects. This dataset is public and can be downloaded and utilized for your own applications if desired. The links to the projects are: [`FireSmokeDataset_part1`](https://universe.roboflow.com/catargiuconstantin/firesmokedataset/dataset/2) and [`FireSmokeDataset_part2`](https://universe.roboflow.com/catargiuconstantin2/firesmokenewdataset/dataset/1).


<details>
  <summary>Dataset details</summary>


`FireSmokeDataset_part1`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/82d91027-216f-4f9c-ada6-41c4431cc51b)

`FireSmokeDataset_part2`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/adb582b8-6d95-4fc3-9f66-855ca31b4742)

</details>

The distribution of the dataset for Training, Validation, and Testing tasks is illustrated in the figure below.

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/1e02db0a-0ff6-4f60-ab93-9ba791481e00)

Dataset Composition:
  
  a) Frames extracted and annotated from approximately 1200 videos.
  
  b) Images manually downloaded from the internet.
       
  c)`4312`images sourced from various public datasets.
  
  From a) and b) i collected `22970` images.

To simplify the process, I created a Python script that enables efficient downloading of the dataset for a specific YOLO model. The script is named $\color{red}{\textsf{DownloadFireDataset.py}}$. The script requires two arguments: the first is the model for which you want to download the dataset, and the second is the location where you wish to store the dataset.
 
  ```bash
  #model can be: yolov5, yolov6, yolov7, yolov8, yolov9
  python3 DownloadFireDataset.py yolov5 --base-dir  /path/to/location/where/the/dataset/will/be/stored

  ```
{\textsf{GetDatasetStatistics.py}}$. It will output informations related to the number of images and instances for each class that is included in Training, Testing and Validation dataset. 

Another useful script you can use to examine the distribution of images within the dataset is  $\color{orange}{\textsf{GetDatasetStatistics.py}}$. This script outputs information regarding the number of images and instances for each class included in the Training, Testing, and Validation datasets.

   ```bash
python3 GetDatasetStatistics.py --path /path/to/dataset
  ```

<details>
  <summary>Output</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/7c254050-130e-4c27-87bc-1cc491280620)
</details>




## Experimental results

The experimental results are stored on [Google Drive](https://drive.google.com/drive/folders/1yrOg-DV_fkiu2aWtRi6ftH_v4MGoTtEd?usp=drive_link) and are publicly accessible.



Configuration setup used for trainig and testing the proposed Yolo models

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/6e9d917a-23f5-42f2-ada7-d42ddd500d9c)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/13bf1153-c8bb-4ef7-b164-cc0d64b2c22f)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/0038819e-31d0-4f22-a014-c531fe6a8dc3)
