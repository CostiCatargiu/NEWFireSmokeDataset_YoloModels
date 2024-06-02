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

`Dataset Improvements`

a) The FireAndSmoke dataset encompasses a wide range of images from various real-world scenes, including  $\color{green}{\textsf{buildings on fire, cars on fire, vegetation fires, wildfires, trash fires, and interior fires.}}$ 

b) The dataset contains  $\color{orangered}{\textsf{aerial views from drones, close-up and distant shots of fires}}$, as well as images captured from below when the $\color{orangered}{\textsf{fire is at a higher altitude}}$. Additionally, the fires vary in $\color{orangered}{\textsf{magnitude and size and may be obscured by vegetation or other objects}}$.

c) The dataset includes a diverse selection of fire and smoke images, captured at $\color{yellow}{\textsf{different times throughout the day — from early morning to late at night}}$. Additionally, the images were taken under a $\color{yellow}{\textsf{variety of weather conditions, including sunny, cloudy, rainy, and foggy scenarios}}$, to showcase how fires and smoke behave and appear in different atmospheric settings. 

$\color{cyan}{\textsf{Overall, the comprehensive nature of the FireAndSmoke dataset, with its wide range of scenes, perspectives, sizes, and environmental conditions, }}$ 
$\color{cyan}{\textsf{makes it highly suitable for training robust machine learning models that can accurately and reliably detect and analyze fires in any situation.}}$ 

d) The dataset contains three classes: fire, smoke and other. The 'other' category assists models in differentiating fire and smoke instances from other elements that could be mistaken for fire or smoke. Instances marked as 'other' also include natural and artificial light sources such as $\color{red}{\textsf{sunsets/sunrises, street lamps, bonfire glows, reflections,vehicle headlights, emergency lights on firefighter vehicles}}$ $\color{red}{\textsf{ and lights from electronic screens, all of which could be mistaken for fire.}}$ 

`YOLO models performnce comparison`

- Based on this dataset, I trained several YOLO models and conducted comparison metrics to evaluate their performance in terms of $\color{red}{\textsf{speed and accuracy.}}$ To train, evaluate, and infer using YOLO, I utilized another repository of mine, [`ALLYoloModels`](https://github.com/CostiCatargiu/AllYoloModels). This repository allows for easy switching between models depending on the task at hand. I have provided detailed instructions there on how to use it.

- I created a script that generate a detailed metric after each inference task to evaluate the performance of each model by examining the $\color{red}{\textsf{snumber of detections and the average confidence level for each class.}}$ This method enables a thorough analysis of which model has the highest detection count and provides a clear measure of the overall accuracy for each class.

`Lastly, but no less important, is the advantage that all my training, inference, and evaluation results, along with the dataset, are publicly accessible. This allows anyone to access and utilize them in their own projects.  
`


## Dataset

$\color{red}{\textsf{Dataset Composition:}}$
  
  a) Frames extracted and annotated from approximately`1200 videos`.
  
  b) Images manually downloaded from the internet.
       
  c)`4312`images sourced from various public datasets.
  
  From a) and b) i collected `22970` images.
  
$\color{red}{\textsf{Repartition of scenes in dataset (22970 in total)}}$

a) 11234 day images.
<details>
  <summary>- 1234 only smoke images</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/7397724e-70d5-4455-a3b2-765a8b373d09)
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/3027c815-8fd0-4395-8520-a6c7cc7a2557)
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/9a30f0af-42a6-4813-9516-5c4fd1b941f5)

</details>

<details>
  <summary>- 1234 only fire images</summary>
  
  ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/175e314b-43dd-4fc0-b78f-73388f6251c1)
  
  ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/e27c67db-6d38-4e53-bd40-c25d29d5f10a)
  
 ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/096b2702-990f-4b52-a090-e51efa15eed1)

</details>

<details>

 <summary>- 1234 only other images</summary>

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/a2115951-15da-4a27-857d-be7b0ca601eb)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/7f98140e-f733-4b68-90c7-c51fdbd05eab)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/4313db0b-a8e2-457c-8fef-bd861864a3a9)

</details>

<details>
  <summary>- 493 fire and smoke images</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/507ff035-7aa0-4016-9e42-e3be0f8c63ed)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/7967e974-12e7-42ed-855c-c71e160f84a8)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/3e7a5ac5-afc2-4d9a-9eab-2847257d02fa)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/5ebabf77-94a1-4fb9-90b5-cf6739058c91)

<details>
  <summary> 213 images captured from drons which contains (fire and smoke scenes or just smoke scenes)</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/8dbdb022-fd90-404c-8142-5ff0c975353c)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/78e1aa8b-d58f-435c-9b67-16fdb1847ccd)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/f4853339-5c1e-466c-a8d1-aceef9807806)

</details>

b) 10000 night images.

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

## Training task

To train the models I used the code from the repository [`ALLYoloModels`](https://github.com/CostiCatargiu/AllYoloModels). From there $\color{orange}{\textsf{YoloModelsTrain.sh script}}$ shall be used,

Syntax:

./YoloModelsTrain.sh  <<select_model>> --[weights] val --[datasetPath] val --[epochs] val --[batchSize] val

Usage example:
  ```bash
./YoloModelsTrain.sh yolov5m  --epochs 100 --batchSize 100
./YoloModelsTrain.sh yolov6m  --epochs 100 --batchSize 100
./YoloModelsTrain.sh yolov7   --epochs 100 --batchSize 100
./YoloModelsTrain.sh gelan-c  --epochs 100 --batchSize 100
./YoloModelsTrain.sh yolov9-c --epochs 100 --batchSize 100
```

Parameters: 
 << >> = required parameter; [ ]=optional parameter

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/94099433-bacf-48bd-8dc0-e6688992fbf4)

If a value is not provided for the optional parameters then the default values will be used.

The dataset path is seted in $\color{orange}{\textsf{parameters.yaml}}$ file like in image bellow. Here we set also the path to the testing videos used for inference task.

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/1f3cad7b-9e80-4dc3-953b-5818b8ea07c8)

From the image above we can observe also that the training results are stored at path $\color{orange}{\textsf{ExperimentaResults/YoloV.../train/exp...}}$

## Experimental results

The experimental results are stored on [`Google Drive`](https://drive.google.com/drive/folders/1yrOg-DV_fkiu2aWtRi6ftH_v4MGoTtEd?usp=drive_link) and are publicly accessible.

 [`yolov5`](https://drive.google.com/drive/folders/1jltoslzNQDlfKtWE5hHKj3R1x6tCDNsS?usp=drive_link)[`yolov6`](https://drive.google.com/drive/folders/1ks4Pfyn_z3I1cvNHvnJAq22F9X5dNxL5?usp=drive_link)[`yolov7`](https://drive.google.com/drive/folders/1nT1yJqUUFXabUhIQt55M9sS3ruuDs0ez?usp=drive_link)[`yolov8`](https://drive.google.com/drive/folders/1UJlGiR7NXNlk90iQqo96yg9rAd0PsICh?usp=drive_link)[`yolov9`](https://drive.google.com/drive/folders/1sj3SSUyJdlphLDI0y9E3IcpCQN-AKiVz?usp=drive_link)[`yoloNAS`](https://drive.google.com/drive/folders/1QWV3czwYHLIuxVuwPFIeiJ1TSyriS_LF?usp=drive_link)

`Configuration setup used for trainig and testing the proposed Yolo models.`

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/6e9d917a-23f5-42f2-ada7-d42ddd500d9c)

`Models hyperparameters used for training process.`

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/13bf1153-c8bb-4ef7-b164-cc0d64b2c22f)

`Results obtained after evaluation on Test Dataaset.`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/30ef6620-7ad6-4d14-aff0-3de45ac4d352)


