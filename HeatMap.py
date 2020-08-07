from PIL import Image, ImageDraw
from numpy import mean
class Hole:
    size_x = 365
    size_y = 523
    par = 3
    teepad_x = 222
    teepad_y = 495
    cage_x = 127
    cage_y = 116
    image = "/Users/rchesla/Downloads/Hole3WillamettePark.JPG"

class HeatMap:
    image = ''

class Shots:
    lon = [173, 150, 245, 171, 130, 40, 170, 137, 155, 91, 89, 123, 127, 139, 113, 214, 144, 146]
    lat = [351, 130, 255, 250, 260, 400, 130, 127, 188, 212, 150, 152, 130, 113, 118, 96, 139, 65]
    score = [5, 2, 5, 3, 4, 7, 3, 2, 3, 4, 3, 2, 2, 2, 2, 3, 2, 3]

# birdie = (255, 250, 0)
# par = (255, 175, 0)
# bogey = (255, 100, 0)
# db = (255, 25, 0)
# tb = (255, 0, 0)
# worse = (255, 50, 0)
worse = (255, 255, 0)
tb = (255, 255, 0)
db = (255, 225, 0)
bogey = (255, 150, 0)
par = (255, 75, 0)
birdie = (255, 0, 0)

Dict = {}
im1 = Image.open(Hole.image);
im2 = Image.new('RGB', (Hole.size_x, Hole.size_y), color = 'white')
for i in range(len(Shots.lon)):
    for j in range(-25, 25):
        for k in range(-25, 25):
            if (j*j) + (k*k) < 625:
                if Shots.score[i] <= 2:
                    if (Shots.lon[i] + k, Shots.lat[i] + j) not in Dict:
                        Dict[Shots.lon[i] + k, Shots.lat[i] + j] = birdie
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), birdie)
                    else:
                        colors = (Dict[Shots.lon[i] + k, Shots.lat[i] + j], birdie)
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tuple(list(map(int,tuple(map(mean, zip(*colors)))))))

                elif Shots.score[i] == 3:
                    if (Shots.lon[i] + k, Shots.lat[i] + j) not in Dict:
                        Dict[Shots.lon[i] + k, Shots.lat[i] + j] = par
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), par)
                    else:
                        colors = (Dict[Shots.lon[i] + k, Shots.lat[i] + j], par)

                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tuple(list(map(int,tuple(map(mean, zip(*colors)))))))
                elif Shots.score[i] == 4:
                    if (Shots.lon[i] + k, Shots.lat[i] + j) not in Dict:
                        Dict[Shots.lon[i] + k, Shots.lat[i] + j] = bogey
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), bogey)
                    else:
                        colors = (Dict[Shots.lon[i] + k, Shots.lat[i] + j], bogey)
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tuple(list(map(int,tuple(map(mean, zip(*colors)))))))
                elif Shots.score[i] == 5:
                    if (Shots.lon[i] + k, Shots.lat[i] + j) not in Dict:
                        Dict[Shots.lon[i] + k, Shots.lat[i] + j] = db
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), db)
                    else:
                        colors = (Dict[Shots.lon[i] + k, Shots.lat[i] + j], db)
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tuple(list(map(int,tuple(map(mean, zip(*colors)))))))
                else:
                    if (Shots.lon[i] + k, Shots.lat[i] + j) not in Dict:
                        Dict[Shots.lon[i] + k, Shots.lat[i] + j] = tb
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tb)
                    else:
                        colors = (Dict[Shots.lon[i] + k, Shots.lat[i] + j], tb)
                        im2.putpixel((Shots.lon[i] + k, Shots.lat[i] + j), tuple(list(map(int,tuple(map(mean, zip(*colors)))))))





result = Image.blend(im1, im2, alpha=0.4)
result.show()

#result.save('testheatmap1.png')
