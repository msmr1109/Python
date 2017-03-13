import sys
import os.path

class JpegImage:
    def __init__ (self):    #객체를 생성할 때 자동 호출
        self.name = None
        self.image = None
        self.thumbnail = None 
        self.checked_thumbnail_exsistence = False

    def open(self, name):
        if not os.path.exists(name):
            return False

        self.name = name 
        return True

    def has_thumbnail(self):
        if self.checked_thumbnail_exsistence:
            return self.thumbnail != None
     
        self.checked_thumbnail_exsistence = True

        beg_pattern = '\xFF\xD8\xFF'
        end_pattern = '\xFF\xD9'
        beg = self._search(self.image, beg_pattern, 1)
        end = self._search(self.image, end_pattern, 3)

        if beg != -1 and end != -1:    #썸네일이 있을 때
            self.thumbnail = self.image[beg : end + 2]
            return True

        return False

    def save_to(self, path):
        if not self.checked_thumbnail_exsistence:
            self.image = self._read_file()
            result = self.has_thumbnail()
            if not result:
                return False

        f = open(path, 'wb+')
        f.write(self.thumbnail)
        f.close()

        return True

    def _read_file(self):
        f = open(self.name, 'rb+')
        image = f.read()  
        f.close()

        return image

    def _search(self, image, pattern, offset):
        if len(image) < len(pattern):
            return -1

        for i in xrange(offset, len(image) - len(pattern)):
            image_block = image[i: i + len(pattern)]
            if pattern == image_block:
                return i

        return -1

if __name__ == "__main__":
    jpeg = JpegImage()

    in_path = "C:/Users/gayeongpark/Desktop/1.jpg"
    if not jpeg.open(in_path):
        print("cannot file open")
        exit(1)

    out_path = "C:/Users/gayeongpark/Desktop/thumbnail_of_1.jpg"
    jpeg.save_to(out_path)
