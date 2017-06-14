import os
import sys


def main(args):
    fd = sys.stdout.fileno()
    bs = os.fstat(fd).st_blksize * 1024
    buf = b"y\n" * int(round(bs / 2))

    try:
        while True:
            offset = os.write(fd, buf)
            while offset < bs:
                offset += os.write(fd, buf[offset:])

        return 0
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main(sys.argv))
