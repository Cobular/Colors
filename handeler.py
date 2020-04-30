import datetime

results = 0
num = 10


def callback(a):
    global results
    results = results + 1
    print(results)


if __name__ == '__main__':
    try:
        file2 = open("colorsWritten.txt","r")
        with open("colors.txt", "w") as file1:
            for line in file.readlines:
                if line not in file2.readlines:
                    file1.write(line)
            file1.close()
    except:
        file2 = open("colorsWritten.txt","w")
        file2.write("")
        file2.close()
    file2 = open("colorsWritten.txt","w")
    file2.write("")
    file2.close()
    print("finished comparing files")
    file = open("colors.txt", "r")
    print("finished reading file, starting now")

    starttime = datetime.datetime.now()
    from generate import generate
    import multiprocessing as mp

    print(mp.cpu_count())

    pool = mp.Pool(mp.cpu_count())
    # for i, row in enumerate(range(num)):
    pool.map_async(generate, file, callback=callback)
    pool.close()
    pool.join()
    print(results)
    print(f"Duration: {(datetime.datetime.now() - starttime) / 257}")
