class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("not supported")
        else:
            print("read from",src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("123")