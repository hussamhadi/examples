# discussion on https://www.linkedin.com/feed/update/urn:li:activity:7412082602788032513?utm_source=share&utm_medium=member_ios&rcm=ACoAAAB9xjMBXVDVuK_7JNnnRC_PTM9yUGRcEP0

def draw_hourglass(n):
    height = n * 2

    for i in range(height+1):
        num = abs(i - n)
        print(("#" * (num * 2 + 1)).center(height+1, " "))


if __name__ == '__main__':
    height = input('Height of hourglass:')
    draw_hourglass(int(height))