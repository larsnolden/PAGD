import numpy as np
import scipy as sp
import cv2


def generateCurve(antenna_representation, padding):
    # hash the antenna representation to get a unique name
    antenna_hash_name = hash(antenna_representation.data.tobytes())

    upscaled_image = sp.ndimage.zoom(antenna_representation, 200, order=0)

    # add padding zeros
    upscaled_image = np.pad(
        upscaled_image, [(padding, padding), (padding, padding)], mode="constant"
    )
    # use this to cut extrude
    inverted_image = np.logical_not(upscaled_image)

    # make integer value for cv2
    upscaled_image_uint8 = (inverted_image * 255).astype(np.uint8)

    # calculate the kernel size to achieve the desired fillet radius
    fillet_radius = 11  # radius in nm
    image_size = np.size(
        upscaled_image_uint8[0]
    )  # number of pixels on one side of the image
    substrate_size = 500  # nm, the sidelength of our simulation boundaries

    pixel_per_nm = image_size / substrate_size
    kernel_size = int(2 * fillet_radius * pixel_per_nm)

    # create the structuring element
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

    # dilate and then erode the image
    rounded_image = cv2.morphologyEx(upscaled_image_uint8, cv2.MORPH_OPEN, kernel)
    rounded_image = cv2.morphologyEx(rounded_image, cv2.MORPH_CLOSE, kernel)

    # save the image for visualization later
    cv2.imwrite(f"./images/{antenna_hash_name}.png", rounded_image)

    # convert image to contours for COMSOL
    ret, threshold = cv2.threshold(cv2.bitwise_not(rounded_image), 127, 255, 0)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # convert contours to COMSOL contour file format
    output_contours = []
    for contour in contours:
        output_contour = [[int(point[0][0]), int(point[0][1])] for point in contour]
        output_contours.append(output_contour)

    filename = f"./contours/{antenna_hash_name}.txt"
    contours = output_contours
    with open(filename, "w") as f:
        f.write("%Coordinates\n")
        total_points = 0
        for contour in contours:
            for point in contour:
                f.write(f"{point[0]} {point[1]}\n")
                total_points += 1

        f.write("\n%Elements\n")
        start_point = 1
        for contour in contours:
            contour_len = len(contour)
            for i in range(start_point, start_point + contour_len - 1):
                # connect each point with the next within the same contour
                f.write(f"{i} {i+1}\n")
            # connect the last point with the first of the same contour
            f.write(f"{start_point + contour_len - 1} {start_point}\n")
            start_point += contour_len

    return filename
