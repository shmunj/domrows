This script calculates the most dominant color in every row of pixels in given image and creates a new image by painting every row in its dominant color.

For nicer effect, it detects background color by simply looking at pixels on vertical edges of the image, and tries to avoid it unless it's the only color present in a row.

It is most effective with png images with small number of "clean" colors (like in cartoons), photos of landscapes, portraits with simple background etc.

Usage:
- only show:    domrows.py <*image*>
- show & save:  domrows.py <*input image*> <*output image*>

![input](https://i.imgur.com/gtT3DrE.png) ![output](https://i.imgur.com/uyQNzj8.png)
