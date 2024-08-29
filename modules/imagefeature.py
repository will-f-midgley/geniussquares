from PIL import Image, ImageDraw

# Colour values for all pieces. Obstacles are shown as white
colours = [(255, 255, 255), (255, 0, 0), (131, 248, 131), (102, 51, 0), (255, 153, 0), (102, 255, 255), (129, 129, 131),
           (255, 255, 0), (102, 0, 102), (0, 0, 204)]


def display_image(g):
    im = Image.new('RGB', [160, 160], (0, 0, 0))
    d = ImageDraw.Draw(im)
    for i in range(1, len(g) + 1):
        for j in range(1, len(g) + 1):
            d.rectangle(xy=(20 * j, 20 * i, 20 * j + 20, 20 * i + 20), fill=(colours[g[i - 1][j - 1] - 1]),
                        outline=(50, 50, 50))

    # Row and column values displayed along the sides
    d.text(xy=(28, 8), text="1       2       3       4       5       6", fill=(255, 255, 255), spacing=200)
    d.text(xy=(8, 25), text="A", fill=(255, 255, 255))
    d.text(xy=(8, 45), text="B", fill=(255, 255, 255))
    d.text(xy=(8, 65), text="C", fill=(255, 255, 255))
    d.text(xy=(8, 85), text="D", fill=(255, 255, 255))
    d.text(xy=(8, 105), text="E", fill=(255, 255, 255))
    d.text(xy=(8, 125), text="F", fill=(255, 255, 255))

    im.show()
