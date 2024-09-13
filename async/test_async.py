# import time
# import json

# def do_something():
#     for i in range(10000):
#         data = None
        
#         with open(f'test/f1/file_{i}.json','r') as outfile:
#             data = json.load(outfile)
#         with open(f'test/f2/file_{i}.json','w') as outfile:
#             json.dump(data,outfile)    


# start = time.perf_counter()
# do_something()
# end = time.perf_counter()
# time = end- start

# print(f"time taken {time:.2f} Sec")

# import time
# import json

# def do_something(i):
#     data = None
#     with open(f'test/f1/file_{i}.json','r') as outfile:
#         data = json.load(outfile)
#     with open(f'test/f2/file_{i}.json','w') as outfile:
#         json.dump(data,outfile)    

# start = time.perf_counter()

# for i in range(10000):
#     do_something(i)

# end = time.perf_counter()
# time = end- start

# print(f"time taken {time:.2f} Sec")

# import time
# import json

# async def do_something(i):
#     try:
#         with open(f'test/f1/file_{i}.json', 'r') as infile:
#             data = json.load(infile)
#     except FileNotFoundError:
#         print(f"File not found: test/f1/file_{i}.json")
#         return

#     with open(f'test/f2/file_{i}.json', 'w') as outfile:
#         json.dump(data, outfile, indent=4)

# async def main():
#     start = time.perf_counter()

#     for i in range(10000):
#         await do_something(i)

#     end = time.perf_counter()
#     total_time = end - start
#     print(f"Time taken: {total_time:.2f} seconds")

# # Run the main function
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())

import concurrent.futures
import time
import json
# import threading
# import multiprocessing

# def do_something(i):
#     data = None
#     print(i)
#     with open(f'test/f1/file_{i}.json','r') as outfile:
#         data = json.load(outfile)
#     with open(f'test/f2/file_{i}.json','w') as outfile:
#         json.dump(data,outfile)    
#     return f"Done.....{i}!!!"
    
# start = time.perf_counter()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_something,1) for _ in range(10)]
    
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
  

# end = time.perf_counter()
# time = end - start

# print(f"Finished in {time:.2f} Secound(s)")



# import time
# import concurrent.futures
# from PIL import Image, ImageFilter

# img_names = [
#     'photo-1516117172878-fd2c41f4a759.jpg',
#     'photo-1532009324734-20a7a5813719.jpg',
#     'photo-1524429656589-6633a470097c.jpg',
#     'photo-1530224264768-7ff8c1789d79.jpg',
#     'photo-1564135624576-c5c88640f235.jpg',
#     'photo-1541698444083-023c97d3f4b6.jpg',
#     'photo-1522364723953-452d3431c267.jpg',
#     'photo-1513938709626-033611b8cc03.jpg',
#     'photo-1507143550189-fed454f93097.jpg',
#     'photo-1493976040374-85c8e12f0c0e.jpg',
#     'photo-1504198453319-5ce911bafcde.jpg',
#     'photo-1530122037265-a5f1f91d3b99.jpg',
#     'photo-1516972810927-80185027ca84.jpg',
#     'photo-1550439062-609e1531270e.jpg',
#     'photo-1549692520-acc6669e2f0c.jpg'
# ]

# t1 = time.perf_counter()

# size = (1200, 1200)


# def process_image(img_name):
#     print(f'test/img/{img_name}')
#     img = Image.open(f'test/img/{img_name}')

#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)
#     img.save(f'test/img/processed/{img_name}')
#     print(f'{img_name} was processed...')



# with concurrent.futures.ProcessPoolExecutor() as executor:
#     executor.map(process_image, img_names)


# t2 = time.perf_counter()

# print(f'Finished in {t2-t1} seconds')


import time
from multiprocessing import Pool
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    print(f'test/img/{img_name}')
    img = Image.open(f'test/img/{img_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'test/img/processed/{img_name}')
    print(f'{img_name} was processed...')



with Pool(1) as pool:
    pool.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')