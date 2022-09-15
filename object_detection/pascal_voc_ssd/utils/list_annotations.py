import os

maindir=r'C:\Users\mkm_i\PycharmProjects\innov-active-learning-remote\LL4AL_ObjectDetection\object_detection\pascal_voc_ssd\media\disk_drive\datasets\VOCdevkit\VOC2012'
imdir=os.path.join(maindir,'JPEGImages')
dest_file=os.path.join(maindir,'ImageSets','Main','trainval.txt')

print(imdir)


imnames=os.listdir(imdir)

#Create a trainval script

names=[]
for imname in imnames:
    names.append(os.path.splitext(imname)[0])

with open(dest_file, 'w') as f:
    f.write('\n'.join(names))



