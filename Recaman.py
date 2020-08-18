from tkinter import *
import PIL
from PIL import Image, ImageDraw

def recaman_step(S, n, step):
   low = n - step
   high = n + step
   if low <= 0 or low in S:
      S.add(high)
      return high
   else:
      S.add(low)
      return low

def iterate_recaman(step_list):
   n = 1
   used = [1]
   S = set(used)
   for i in range(len(step_list)):
      if i % 10000 == 0:
         print(str(round(i / len(step_list) * 100, 2)) + '%')
      step = step_list[i]
      n = recaman_step(S, n, step)
      used.append(n)
      step += 1
   return used

def generate_primes(natural_numbers):
   primes = [2]
   n = 2
   while len(primes) <= len(natural_numbers):
      n += 1
      for p in primes:
         if p**2 > n:
            primes.append(n)
            break
         if n%p == 0:
            break
   return primes

def generate_composite(natural_numbers):
   composite = []
   n = 3
   while len(composite) <= len(natural_numbers):
      n += 1
      for c in range(2, n):
         if c**2 > n:
            break
         if n%c == 0:
            composite.append(n)
            break
   return composite

def draw_recaman(iterations, space_between, just_last = False):
   root = Tk()

   print('Creating Series Now')
   natural_numbers = range(1, iterations + 1)
   #base_series = iterate_recaman(natural_numbers)
   base_series = generate_primes(natural_numbers)
   series = iterate_recaman(base_series)
   '''for n in range(len(natural_numbers)):
      print(natural_numbers[n], base_series[n], series[n])'''
   print('Series Created')
   print()

   max_jump = 0
   for i in range(len(series) - 1):
      n1 = series[i]
      n2 = series[i + 1]
      jump = abs(n2 - n1)
      if jump > max_jump:
         max_jump = jump

   if just_last:
      draw_iteration(series, iterations, max_jump, space_between)
   else:
      for i in range(iterations):
         print (round(i/iterations*100, 2))
         draw_iteration(series, i, max_jump, space_between)


def draw_iteration(series, iteration, max_jump, space_between):

   buff = 3 + ((max_jump * space_between)// 16)
   pixel_start = buff
   start = 1
   end = max(series)
   span = end - start
   pixel_span = span * space_between
   above = True
   width = int(pixel_span + buff * 2)
   height = int((max_jump * space_between) + buff * 2)
   y = height // 2
   image = Image.new("1", (width, height))
   canvas = ImageDraw.Draw(image)

   for i in range(iteration):
      n1 = series[i]
      n2 = series[i + 1]
      percent1 = (n1 - 1) / span
      percent2 = (n2 - 1) / span
      first = percent1 * pixel_span + buff
      second= percent2 * pixel_span + buff
      d = abs(first - second)
      if first < second:
         if above:
            canvas.arc([first, y - d//2, second, y + d//2], start = 180, end = 0, fill = 'White')
         else:
            canvas.arc([first, y - d//2, second, y + d//2], start = 0, end = 180,  fill = 'White')
      else:
         if above:
            canvas.arc([second, y - d//2, first, y + d//2], start = 180, end = 0,  fill = 'White')
         else:
            canvas.arc([second, y - d//2, first, y + d//2], start = 0, end = 180,  fill = 'White')
      if above:
         above = False
      else:
         above = True

   image.save("Images/Recaman" + str(iteration) + ".png")

def find_iterations_until(i):
   step = 1
   n = 1
   used = [1]
   count = 0
   while i not in used:
      count += 1
      n = recaman_step(used, n, step)
      step += 1
      if count % 1000 == 0:
         print (count//1000)
   
   return len(used)

def create_until_list(start, end):
   L = []
   for i in range(start, end + 1):
      m = find_iterations_until(i)
      L.append(m)
      print(i, m)


draw_recaman(10000, .1, just_last = True)




