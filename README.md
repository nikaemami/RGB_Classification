# RGB_Classification
Classification of an image dataset using their **RGB values**.

Given a dataset of pictures from **Manchester United** and **Chelsea** football teams, the goal is to implement a model which determines what team a player in the field belongs to, based on the color of his clothes.

First, I read the images using the os library:

```ruby
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
```

Next, I get the rgb values of each image as below:

```ruby
channels.append(cv2.mean(img))
channels_rgb.append([channels[i][2], channels[i][1], channels[i][0]])
```

Finally, I classify the images whether their channel R values is greater than channel B or not:

```ruby
if (image_list[i][0] < image_list[i][2]):
  label_list.append('Chelsea')
else:
  label_list.append('Manchester United')
```

Calculating the evaluation metrics on the test set, the results are as follows:

Confusion Matrix =  [[46, 18], [1, 58]]

accuracy =  0.8455284552845529

precision =  0.9787234042553191

recall =  0.71875
