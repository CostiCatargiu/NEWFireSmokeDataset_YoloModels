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

a) 15812 day images.
<details>
  <summary>- 2121 only smoke scenes</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/83bf5bb8-f660-4ba5-93d7-890d8493ce91)


</details>

<details>
  <summary>- 2475 only fire scenes</summary>
  
  ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/d9d71090-fd7a-446a-a6e2-1f67efb70030)

</details>

<details>

 <summary>- 645 only other scenes</summary>

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/08544060-3068-4ba2-b2cd-045f2551d1d0)


</details>

<details>
  <summary>- 4312 fire and smoke scenes</summary>

  ![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/66bb7935-834c-46ab-9fc4-ee8a7dd4401d)


</details>

<details>
  <summary>- 3138 images captured from drones which contains (fire and smoke scenes or just smoke scenes)</summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/fd19f3e8-29f3-4c55-81ce-fdfb35685a37)


</details>


<details>
  <summary>- 3121 vegetation fire </summary>

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/60c1e864-aa1d-4181-b9ee-8b3ac7d602de)

</details>

b) 7158 night images.

<details>
  <summary>- 2657 fire and smoke scenes </summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/838b715c-0c7f-4866-a78c-0f01efd3d17b)

</details>

<details>
  <summary>- 1852 fire, smoke, other night scenes </summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/622b4bc1-e902-4e79-bbdc-84eae0dd6293)


</details>

<details>
  <summary>- 1228 only fire scenes </summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/2b96c00b-c1f1-4178-ad96-6e9b4f0f735b)

</details>

<details>
  <summary>- 1421 only other scenes </summary>
  
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/5a1ed23c-c890-45df-b5d4-1596382ab5f9)

</details>


The dataset is hosted on the Roboflow platform and consists of two projects. This dataset is public and can be downloaded and utilized for your own applications if desired. The links to the projects are: [`FireSmokeDataset_part1`](https://universe.roboflow.com/catargiuconstantin/firesmokedataset/dataset/2) and [`FireSmokeDataset_part2`](https://universe.roboflow.com/catargiuconstantin2/firesmokenewdataset/dataset/1).

<details>
  <summary>Dataset details</summary>


`FireSmokeDataset_part1`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/82d91027-216f-4f9c-ada6-41c4431cc51b)

`FireSmokeDataset_part2`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/adb582b8-6d95-4fc3-9f66-855ca31b4742)

</details>

The distribution of the dataset for Training, Validation, and Testing tasks is illustrated in the figure below.

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/034cd2bc-3528-453a-bf51-483ea49e8c84)


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

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/d3579f58-27ab-443e-941d-9d934dc56b55)

`Results obtained after evaluation on Test Dataset.`
![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/a96369b1-29d3-4155-9089-726d0bd4f650)


## Models Comparison Performance metrics

`Results obtain after inference on VideoDayMixt`

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/14956439-fdab-414c-8058-e6bb973c1ded)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/8dae8e65-1f19-4650-ac09-8c0c4086475c)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/c86e69c8-c32e-4ced-9f05-9c53f200b810)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/6b0b0d2b-6600-4380-bb34-08ae9ed97a4a)

`Results obtain after inference on VideoNightMixt`

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/0c455003-66dc-415d-ba73-8229b7998cc8)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/72c8a9d3-da6f-4936-8e1c-bdc3472d2f8c)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/93a96f22-c8dd-4522-985e-5d4422ce0f73)

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/f4b87a91-494a-4feb-bff3-7a1e42fddd05)


<details>
  <summary>YoloV6 wrong prediction (predict other to be fire) </summary>
  
![yolov6_missmatch_fire_other](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/487af181-f7c5-4c93-9e98-1c4ed8fa65bd)

  </details>

  <details>
  <summary>YoloV5,V6 and V7 wrong prediction (predict other to be fire) </summary>
    
![yolov567_missmatch_fire_other](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ea2381a8-8f3a-4fcc-9a76-dddbc216cadc)

  </details>
    
`Results obtain after inference on VideoNightMixt`

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ea5491c7-85be-40fc-b8de-5d45da1f387c)

![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/2a3c7472-a5bc-4dc4-be0b-c14238947982)

  <details>
  <summary>YoloV7 and Gelan-c wrong prediction (predict smoke to be fire) </summary>
    
![Yolov7ANDgelan_missmatch_fire_smoke](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/69fd3629-a9a2-4f9a-a8a1-f7301da4c886)

  </details>
    
<details>
  <summary>YoloV8 and V9 miss detection</summary>
    
![Frame 9728_screenshot_02 06 2024](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ff812f14-752b-4c14-97ef-3a8d9f5b9834)

  </details>

  <details>
  <summary>YoloV5, V8 and Gelan-c wrong prediction (predict other to be fire)</summary>
    
![Frame 9728_screenshot_02 06 2024](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ff812f14-752b-4c14-97ef-3a8d9f5b9834)

  </details>
<details>
  <summary>All models wrong prediction (predict other to be fire)</summary>
    
![Frame 2717_screenshot_02 06 2024](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/3ec4dc42-1d15-4782-af31-3de6099f671e)


  </details>

<details>
  <summary>Smoke detected just by YoloV5,V6 and V8 (difficult scene) </summary>
    

![Frame 6384_screenshot_03 06 2024](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/ab92d8b3-f937-46c7-984f-4dd8cd229dfe)


  </details>
  
