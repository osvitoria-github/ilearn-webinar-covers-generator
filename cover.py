import numbers
import PIL
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('C:\\Users\\User\\Desktop\\covers\\OpenSans-Bold.ttf', size=54) #path to font file and size of font
""" number_list=['1','2','3','4','5','6','7','8','9','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35'] #array of numbers """

number_list = [str(i) for i in range(1,36)] #generate string array of numbers in (n,m)


""" path_eng="C:\\Users\\User\\Desktop\\covers\\eng\\" #path to folder, where covers will be saved
for number in number_list:
    eng = Image.open('C:\\Users\\User\\Desktop\\covers\\eng.png') #path to original cover without number of webinar
    draw_text = ImageDraw.Draw(eng)
    draw_text.text(
    (565, 592), #coordinates of place where number of webinar will be situated (use Cartesian pixel coordinate system, with (0,0) in the upper left corner)
    number,
    font=font,
    fill='#fff') #font color of webinar number
    eng.save(path_eng + "eng" + number + ".png") #generate name of covers """

""" path_ukr="C:\\Users\\User\\Desktop\\covers\\ukr\\"
for number in number_list:
    ukr = Image.open('C:\\Users\\User\\Desktop\\covers\\ukr.png')
    draw_text = ImageDraw.Draw(ukr)
    draw_text.text(
    (560, 592),
    number,
    font=font,
    fill='#fff')
    ukr.save(path_ukr + "ukr" + number + ".png") """

""" path_hist="C:\\Users\\User\\Desktop\\covers\\hist\\"
for number in number_list:
    hist = Image.open('C:\\Users\\User\\Desktop\\covers\\hist.png')
    draw_text = ImageDraw.Draw(hist)
    draw_text.text(
    (565, 592),
    number,
    font=font,
    fill='#00466e')
    hist.save(path_hist + "hist" + number + ".png") """

""" path_math="C:\\Users\\User\\Desktop\\covers\\math\\"
for number in number_list:
    math = Image.open('C:\\Users\\User\\Desktop\\covers\\math.png')
    draw_text = ImageDraw.Draw(math)
    draw_text.text(
    (565, 592),
    number,
    font=font,
    fill='#fff')
    math.save(path_math + "math" + number + ".png") """

""" path_phy="C:\\Users\\User\\Desktop\\covers\\phy\\"
for number in number_list:
    phy = Image.open('C:\\Users\\User\\Desktop\\covers\\phy.png')
    draw_text = ImageDraw.Draw(phy)
    draw_text.text(
    (570, 592),
    number,
    font=font,
    fill='#fff')
    phy.save(path_phy + "phy" + number + ".png") """

""" path_geo="C:\\Users\\User\\Desktop\\covers\\geo\\"
for number in number_list:
    geo = Image.open('C:\\Users\\User\\Desktop\\covers\\geo.png')
    draw_text = ImageDraw.Draw(geo)
    draw_text.text(
    (565, 592),
    number,
    font=font,
    fill='#fff')
    geo.save(path_geo + "geo" + number + ".png") """

""" path_bio="C:\\Users\\User\\Desktop\\covers\\bio\\"
for number in number_list:
    bio = Image.open('C:\\Users\\User\\Desktop\\covers\\bio.png')
    draw_text = ImageDraw.Draw(bio)
    draw_text.text(
    (565, 595),
    number,
    font=font,
    fill='#fff')
    bio.save(path_bio + "bio" + number + ".png") """

""" path_chem="C:\\Users\\User\\Desktop\\covers\\chem\\"
for number in number_list:
    chem = Image.open('C:\\Users\\User\\Desktop\\covers\\chem.png')
    draw_text = ImageDraw.Draw(chem)
    draw_text.text(
    (565, 595),
    number,
    font=font,
    fill='#00466e')
    chem.save(path_chem + "chem" + number + ".png") """