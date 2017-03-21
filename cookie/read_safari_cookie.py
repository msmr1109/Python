
from struct import *

def read_int4_be(f):
    return unpack(">i", f.read(4))[0]

def read_int4_le(f):
    return unpack("<i", f.read(4))[0]

class Cookie:
    def __init__(self, f, pos):
        self.f   = f
        self.f.seek(pos)
        self.pos = pos

        self.cookie_size = read_int4_le(f)
        unknown1         = [read_int4_le(f) for i in range(3)]
        string_offset    = [read_int4_le(f) for i in range(4)]
        unknown2         = [read_int4_le(f) for i in range(2)]
        self.expiration_date = self.get_date()
        self.created_date    = self.get_date()
        self.url   = self.get_string_from(string_offset[0])
        self.name  = self.get_string_from(string_offset[1])
        self.path  = self.get_string_from(string_offset[2])
        self.value = self.get_string_from(string_offset[3])

    def get_date(self):
        return unpack("d", self.f.read(8))[0]

    def get_string_from(self, from_):
        self.f.seek(self.pos + from_)
        string = ""
        while True:
            ch = self.f.read(1)
            if ch == '\x00':
                break
            string += ch    
        
        return string

class Page:
    def __init__(self, f, pos):
        self.f   = f
        self.pos = pos #page시작위치

        f.seek(pos)
        header = read_int4_be(f)
        if header != 256:
            return False

        self.cookie_count  = read_int4_le(f)
        self.cookie_offset = self.get_cookie_offset()
        self.cookie_pos    = self.cookie_position(self.cookie_count)
        self.cookies       = self.read_cookie()

    def get_cookie_offset(self):
        cookie_offset = []
        for i in range(self.cookie_count + 1):
            cookie_offset.append(read_int4_le(self.f))
        return cookie_offset

    def read_cookie(self):
        cookies = []
        for i in range(self.cookie_count):
            cookies.append(Cookie(self.f, self.cookie_pos[i]))

        return cookies

    def cookie_position(self, count):
        cookie_pos = []
        for i in range(count):
            cookie_pos.append(self.pos + self.cookie_offset[i])

        return cookie_pos        

class SafariCookie:
    def __init__(self, path):
        self.f = open(path, 'rb')
        self.page_count = 0
        self.start_page = 0
        self.page_pos   = []
        self.pages      = []

    def read_page_size(self, count):
        page_sizes = []
        for i in range(0, count):
            page_sizes.append(read_int4_be(self.f))
        self.start_page = self.f.tell()

        return page_sizes

    def page_position(self, page_sizes):
        page_pos = [self.start_page]
        for i in range(1, self.page_count + 1):
            page_pos.append(page_pos[i-1] + page_sizes[i-1])

        return page_pos

    def read_pages_with(self):
        pages = []    
        for i in range(0, self.page_count):
            pages.append(Page(self.f, self.page_pos[i]))

        return pages        

    def analyze(self):
        sig, self.page_count = unpack(">4si", self.f.read(8))
        page_sizes    = self.read_page_size(self.page_count)
        self.page_pos = self.page_position(page_sizes)            
        self.pages    = self.read_pages_with()

        return True

    def close(self):
        self.f.close()

if __name__ == "__main__":
    def view_cookie(path, n, m):
        safari = SafariCookie(path)
        safari.analyze()
        pa = Page(safari.f, safari.page_pos[n - 1])
        coo = Cookie(safari.f, pa.cookie_pos[m - 1])
        list = [coo.expiration_date, coo.created_date, coo.url, coo.name, coo.path, coo.value]
        safari.close()

        return list

    path = "C:/Users/gayeongpark/Desktop/Cookies.binarycookies"    
    test = view_cookie(path, 1, 1)
    print(test)
