# create tiles from image

# python3 create-tiles-from-image.py ./big-image.jpg 10 30

# import modules
import os
import sys
import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.text as text
import matplotlib.ticker as ticker
import base64


# define functions
def create_tiles(image, tile_size, tile_dir, lines, columns, print_code=False):
    # get image size
    image_size = image.shape
    # get number of tiles
    num_tiles = int(np.ceil(image_size[0] / tile_size[0]) * np.ceil(image_size[1] / tile_size[1]))
    # create tiles
    final_counter = 0
    for i in range(num_tiles):
        # get tile coordinates
        tile_x = i % int(np.ceil(image_size[0] / tile_size[0]))
        tile_y = int(np.floor(i / int(np.ceil(image_size[0] / tile_size[0]))))
        # get tile size
        tile_size_x = min(tile_size[0], image_size[0] - tile_x * tile_size[0])
        tile_size_y = min(tile_size[1], image_size[1] - tile_y * tile_size[1])
        if tile_x >=  lines:
            continue
        if tile_y >=  columns:
            continue
        # get tile image
        tile_image = image[tile_x * tile_size[0]:tile_x * tile_size[0] + tile_size_x, tile_y * tile_size[1]:tile_y * tile_size[1] + tile_size_y]
        # save tile image
        # cv2.imwrite(tile_dir + '/tile_' + str(tile_x) + '_' + str(tile_y) + '.jpg', tile_image)
        if print_code:
            # print(encode_image(tile_image))
            print(tile_x, tile_y)
        final_counter += 1


def create_tiles_by_lines_and_columns(image, lines, columns, tile_dir, print_code=False):
    # get image size
    image_size = image.shape
    # get tiles size
    tile_size = (int(image_size[0] / lines), int(image_size[1] / columns))
    print("Tile size:", tile_size)
    # create tiles
    create_tiles(image, tile_size, tile_dir, lines, columns, print_code)

# encode image in base64
def encode_image(image):
    # encode image in base64
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    # return image base64
    return str(jpg_as_text)[2:-1]

# define main function
def main():
    # get image path
    image_path = sys.argv[1]
    # get tile size
    lines = int(sys.argv[2])
    columns = int(sys.argv[3])
    # get tile directory
    tile_dir = "./tiles"
    # check if tile directory exists
    if not os.path.exists(tile_dir):
        os.makedirs(tile_dir)
    # read image
    image = cv2.imread(image_path)
    print("Image size:", image.shape)
    # create tiles
    create_tiles_by_lines_and_columns(image, lines, columns, tile_dir, True)
    
    # create smaller version of image
    image_small = cv2.resize(image, (int(image.shape[1] / 4), int(image.shape[0] / 4)))
    # get thumbs directory
    thumbs_dir = "./tiles/thumbs"
    # check if tile directory exists
    if not os.path.exists(thumbs_dir):
        os.makedirs(thumbs_dir)
    # create tiles
    create_tiles_by_lines_and_columns(image_small, lines, columns, thumbs_dir, True)


    # # create smallest version of image
    image_smallest = cv2.resize(image, (int(image.shape[1] / 6), int(image.shape[0] / 6)))
    # get thumbs directory
    thumbs_dir = "./tiles/thumbs2"
    # check if tile directory exists
    if not os.path.exists(thumbs_dir):
        os.makedirs(thumbs_dir)
    # create tiles
    create_tiles_by_lines_and_columns(image_smallest, lines, columns, thumbs_dir, True)



# run main function
if __name__ == '__main__':
    main()

